/* Alerts Management JavaScript */

let currentPage = 0;
const itemsPerPage = 50;
let allAlerts = [];

// Initialize alerts page
document.addEventListener('DOMContentLoaded', function() {
    console.log('Alerts page loaded');
    loadAlerts();
    setInterval(loadAlerts, 10000); // Refresh every 10 seconds
});

// Load alerts
function loadAlerts() {
    fetch('/api/alerts-all?skip=0&limit=500')
        .then(response => response.json())
        .then(data => {
            allAlerts = data || [];
            displayAlertsPage();
        })
        .catch(error => console.error('Error loading alerts:', error));
}

// Display alerts for current page
function displayAlertsPage() {
    const start = currentPage * itemsPerPage;
    const end = start + itemsPerPage;
    const pageAlerts = allAlerts.slice(start, end);

    const tbody = document.getElementById('alerts-tbody');
    
    if (pageAlerts.length === 0) {
        tbody.innerHTML = '<tr><td colspan="9">No alerts found</td></tr>';
    } else {
        tbody.innerHTML = pageAlerts.map((alert, index) => `
            <tr>
                <td>${alert.id}</td>
                <td>${formatDate(alert.created_at)}</td>
                <td>${alert.source_ip}</td>
                <td>${alert.destination_ip}</td>
                <td>${alert.protocol}</td>
                <td>${alert.attack_type}</td>
                <td><strong>${alert.risk_score.toFixed(1)}</strong></td>
                <td>${alert.packet_size}</td>
                <td><button onclick="deleteAlert(${alert.id})" class="btn-danger">Delete</button></td>
            </tr>
        `).join('');
    }

    updatePaginationInfo();
}

// Update pagination info
function updatePaginationInfo() {
    const totalPages = Math.ceil(allAlerts.length / itemsPerPage);
    document.getElementById('page-info').textContent = `Page ${currentPage + 1} of ${totalPages}`;
}

// Next page
function nextPage() {
    const totalPages = Math.ceil(allAlerts.length / itemsPerPage);
    if (currentPage < totalPages - 1) {
        currentPage++;
        displayAlertsPage();
        window.scrollTo(0, 0);
    }
}

// Previous page
function prevPage() {
    if (currentPage > 0) {
        currentPage--;
        displayAlertsPage();
        window.scrollTo(0, 0);
    }
}

// Apply filters
function applyFilters() {
    const timeFilter = document.getElementById('time-filter').value;
    const riskFilter = document.getElementById('risk-filter').value;
    
    let filtered = allAlerts;

    // Apply time filter
    if (timeFilter !== 'all') {
        const hours = parseInt(timeFilter);
        const cutoffTime = new Date(Date.now() - hours * 60 * 60 * 1000);
        filtered = filtered.filter(alert => new Date(alert.created_at) > cutoffTime);
    }

    // Apply risk filter
    if (riskFilter !== 'all') {
        filtered = filtered.filter(alert => {
            const score = alert.risk_score;
            if (riskFilter === 'critical') return score >= 80;
            if (riskFilter === 'high') return score >= 60 && score < 80;
            if (riskFilter === 'medium') return score >= 40 && score < 60;
            if (riskFilter === 'low') return score < 40;
        });
    }

    allAlerts = filtered;
    currentPage = 0;
    displayAlertsPage();
}

// Delete alert
function deleteAlert(alertId) {
    if (confirm('Are you sure you want to delete this alert?')) {
        fetch(`/api/delete-alert/${alertId}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    loadAlerts();
                } else {
                    alert('Failed to delete alert');
                }
            })
            .catch(error => console.error('Error deleting alert:', error));
    }
}

// Clear all alerts
function clearAllAlerts() {
    if (confirm('Are you sure you want to delete ALL alerts? This cannot be undone!')) {
        allAlerts.forEach(alert => {
            fetch(`/api/delete-alert/${alert.id}`, { method: 'DELETE' })
                .catch(error => console.error('Error deleting alert:', error));
        });
        setTimeout(loadAlerts, 1000);
    }
}

// Format date
function formatDate(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleString();
}
