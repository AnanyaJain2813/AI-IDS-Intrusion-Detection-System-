/* Dashboard JavaScript */

let trafficChart, trendChart;
let alertsData = [];
let refreshInterval;

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard loaded');
    updateTime();
    initCharts();
    loadDashboardData();
    
    // Refresh data every 5 seconds
    refreshInterval = setInterval(loadDashboardData, 5000);
    
    // Update time every second
    setInterval(updateTime, 1000);
});

// Update current time
function updateTime() {
    const now = new Date();
    document.getElementById('time').textContent = now.toLocaleTimeString();
}

// Initialize charts
function initCharts() {
    // Traffic Chart
    const trafficCtx = document.getElementById('trafficChart').getContext('2d');
    trafficChart = new Chart(trafficCtx, {
        type: 'doughnut',
        data: {
            labels: ['Normal', 'Malicious'],
            datasets: [{
                data: [0, 0],
                backgroundColor: ['#2ecc71', '#e74c3c'],
                borderColor: ['rgba(46, 204, 113, 0.2)', 'rgba(231, 76, 60, 0.2)'],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    labels: { color: '#bdc3c7' }
                }
            }
        }
    });

    // Trend Chart
    const trendCtx = document.getElementById('trendChart').getContext('2d');
    trendChart = new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00', '23:59'],
            datasets: [{
                label: 'Alerts',
                data: [0, 0, 0, 0, 0, 0, 0],
                borderColor: '#e94560',
                backgroundColor: 'rgba(233, 69, 96, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { labels: { color: '#bdc3c7' } }
            },
            scales: {
                y: { ticks: { color: '#bdc3c7' } },
                x: { ticks: { color: '#bdc3c7' } }
            }
        }
    });
}

// Load dashboard data
function loadDashboardData() {
    fetch('/api/dashboard-data')
        .then(response => response.json())
        .then(data => {
            if (data.stats) {
                updateStats(data.stats);
            }
            if (data.alerts) {
                updateAlerts(data.alerts);
            }
            if (data.health) {
                updateStatus(data.health);
            }
        })
        .catch(error => console.error('Error loading dashboard data:', error));
}

// Update statistics
function updateStats(stats) {
    document.getElementById('stat-malicious').textContent = stats.malicious_packets || 0;
    document.getElementById('stat-normal').textContent = stats.normal_packets || 0;
    document.getElementById('stat-today').textContent = stats.alerts_today || 0;
    document.getElementById('stat-total').textContent = stats.total_alerts || 0;

    // Update charts
    if (trafficChart) {
        trafficChart.data.datasets[0].data = [stats.normal_packets || 0, stats.malicious_packets || 0];
        trafficChart.update();
    }
}

// Update alerts table
function updateAlerts(alerts) {
    const tbody = document.getElementById('alerts-tbody');
    
    if (!alerts || alerts.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6">No alerts found</td></tr>';
        return;
    }

    tbody.innerHTML = alerts.map(alert => `
        <tr class="${getRiskClass(alert.risk_score)}">
            <td>${formatDate(alert.created_at)}</td>
            <td>${alert.source_ip}</td>
            <td>${alert.destination_ip}</td>
            <td>${alert.protocol}</td>
            <td>${alert.risk_score.toFixed(1)}</td>
            <td><span class="badge badge-danger">${alert.attack_type}</span></td>
        </tr>
    `).join('');
}

// Update system status
function updateStatus(health) {
    const statusDot = document.getElementById('status-dot');
    const statusText = document.getElementById('status-text');
    
    if (health.status === 'healthy') {
        statusDot.classList.add('online');
        statusText.textContent = 'Online';
    } else {
        statusDot.classList.remove('online');
        statusText.textContent = 'Offline';
    }
}

// Get risk-based CSS class
function getRiskClass(riskScore) {
    if (riskScore >= 80) return 'alert-high';
    if (riskScore >= 60) return 'alert-medium';
    return 'alert-low';
}

// Format date
function formatDate(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleTimeString();
}

// Cleanup on page unload
window.addEventListener('beforeunload', function() {
    if (refreshInterval) clearInterval(refreshInterval);
});
