"""
Flask web dashboard for AI IDS
Real-time visualization of network threats and system statistics
"""
from flask import Flask, render_template, jsonify, request
import requests
import json
from datetime import datetime
from pathlib import Path
from config import API_HOST, API_PORT

# Get absolute paths for templates and static files
BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'

app = Flask(__name__, template_folder=str(TEMPLATE_DIR), static_folder=str(STATIC_DIR))
API_BASE_URL = f"http://{API_HOST}:{API_PORT}"

# ============ HELPER FUNCTIONS ============
def get_api_data(endpoint):
    """Fetch data from FastAPI backend"""
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"[ERROR] API request failed: {e}")
        return None

# ============ ROUTES ============
@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/dashboard-data')
def dashboard_data():
    """Fetch all dashboard data"""
    try:
        stats = get_api_data('/api/stats')
        alerts = get_api_data('/api/alerts?limit=10')
        health = get_api_data('/api/health')
        
        return jsonify({
            'stats': stats,
            'alerts': alerts,
            'health': health,
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/alerts-recent')
def alerts_recent():
    """Fetch recent alerts with time filtering"""
    hours = request.args.get('hours', 24, type=int)
    alerts = get_api_data(f'/api/alerts/latest?hours={hours}')
    return jsonify(alerts or [])

@app.route('/api/alerts-all')
def alerts_all():
    """Fetch all alerts with pagination"""
    skip = request.args.get('skip', 0, type=int)
    limit = request.args.get('limit', 50, type=int)
    alerts = get_api_data(f'/api/alerts?skip={skip}&limit={limit}')
    return jsonify(alerts or [])

@app.route('/alerts')
def alerts_page():
    """Alerts management page"""
    return render_template('alerts.html')

@app.route('/statistics')
def statistics_page():
    """Statistics and analytics page"""
    return render_template('statistics.html')

@app.route('/api/delete-alert/<int:alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    """Delete an alert"""
    try:
        response = requests.delete(f"{API_BASE_URL}/api/alerts/{alert_id}")
        return jsonify({'success': response.status_code == 200})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/system-status')
def system_status():
    """Get system health status"""
    health = get_api_data('/api/health')
    return jsonify(health or {'status': 'offline'})

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
