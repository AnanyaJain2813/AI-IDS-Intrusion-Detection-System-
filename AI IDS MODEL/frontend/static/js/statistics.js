/* Statistics JavaScript */

let compositionChart, typeChart, timelineChart, topIpsChart;

// Initialize statistics page
document.addEventListener('DOMContentLoaded', function() {
    console.log('Statistics page loaded');
    initCharts();
    loadStatistics();
    setInterval(loadStatistics, 10000); // Refresh every 10 seconds
});

// Initialize all charts
function initCharts() {
    // Composition Chart (Pie)
    const compositionCtx = document.getElementById('compositionChart').getContext('2d');
    compositionChart = new Chart(compositionCtx, {
        type: 'pie',
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
            plugins: {
                legend: { labels: { color: '#bdc3c7' } }
            }
        }
    });

    // Type Chart (Bar)
    const typeCtx = document.getElementById('typeChart').getContext('2d');
    typeChart = new Chart(typeCtx, {
        type: 'bar',
        data: {
            labels: ['DDoS', 'Malware', 'Anomaly', 'Exploit', 'Scanning'],
            datasets: [{
                label: 'Count',
                data: [0, 0, 0, 0, 0],
                backgroundColor: '#e94560',
                borderColor: 'rgba(233, 69, 96, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            indexAxis: 'x',
            plugins: {
                legend: { labels: { color: '#bdc3c7' } }
            },
            scales: {
                y: { ticks: { color: '#bdc3c7' } },
                x: { ticks: { color: '#bdc3c7' } }
            }
        }
    });

    // Timeline Chart (Line)
    const timelineCtx = document.getElementById('timelineChart').getContext('2d');
    timelineChart = new Chart(timelineCtx, {
        type: 'line',
        data: {
            labels: generateTimeLabels(24),
            datasets: [{
                label: 'Alerts',
                data: Array(24).fill(0),
                borderColor: '#e94560',
                backgroundColor: 'rgba(233, 69, 96, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { labels: { color: '#bdc3c7' } }
            },
            scales: {
                y: { ticks: { color: '#bdc3c7' } },
                x: { ticks: { color: '#bdc3c7' } }
            }
        }
    });

    // Top IPs Chart (Horizontal Bar)
    const topIpsCtx = document.getElementById('topIpsChart').getContext('2d');
    topIpsChart = new Chart(topIpsCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Alerts',
                data: [],
                backgroundColor: '#3498db',
                borderColor: 'rgba(52, 152, 219, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
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

// Load statistics
function loadStatistics() {
    fetch('/api/dashboard-data')
        .then(response => response.json())
        .then(data => {
            if (data.stats) {
                updateStatsOverview(data.stats);
                updateCharts(data.stats);
            }
            if (data.alerts) {
                generateAlertStats(data.alerts);
            }
        })
        .catch(error => console.error('Error loading statistics:', error));
}

// Update stats overview
function updateStatsOverview(stats) {
    document.getElementById('total-alerts').textContent = stats.total_alerts || 0;
    document.getElementById('malicious-detections').textContent = stats.malicious_packets || 0;
    document.getElementById('normal-traffic').textContent = stats.normal_packets || 0;
    document.getElementById('today-alerts').textContent = stats.alerts_today || 0;
}

// Update charts
function updateCharts(stats) {
    // Update composition chart
    if (compositionChart) {
        compositionChart.data.datasets[0].data = [
            stats.normal_packets || 0,
            stats.malicious_packets || 0
        ];
        compositionChart.update();
    }
}

// Generate alert statistics
function generateAlertStats(alerts) {
    if (!alerts || alerts.length === 0) return;

    // Count alerts by type
    const typeCount = {};
    alerts.forEach(alert => {
        const type = alert.attack_type || 'Unknown';
        typeCount[type] = (typeCount[type] || 0) + 1;
    });

    // Update type chart
    if (typeChart) {
        const types = Object.keys(typeCount).slice(0, 5);
        const counts = types.map(t => typeCount[t]);
        typeChart.data.labels = types;
        typeChart.data.datasets[0].data = counts;
        typeChart.update();
    }

    // Count top source IPs
    const ipCount = {};
    alerts.forEach(alert => {
        const ip = alert.source_ip || 'Unknown';
        ipCount[ip] = (ipCount[ip] || 0) + 1;
    });

    const topIps = Object.entries(ipCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);

    if (topIpsChart) {
        topIpsChart.data.labels = topIps.map(ip => ip[0]);
        topIpsChart.data.datasets[0].data = topIps.map(ip => ip[1]);
        topIpsChart.update();
    }

    // Timeline data (simulate)
    const hourCount = Array(24).fill(0);
    alerts.forEach(alert => {
        const date = new Date(alert.created_at);
        const hour = date.getHours();
        hourCount[hour]++;
    });

    if (timelineChart) {
        timelineChart.data.datasets[0].data = hourCount;
        timelineChart.update();
    }
}

// Generate time labels for timeline
function generateTimeLabels(hours) {
    const labels = [];
    for (let i = 0; i < hours; i++) {
        labels.push(`${i}:00`);
    }
    return labels;
}

// Export as CSV
function exportCSV() {
    fetch('/api/alerts-all?limit=10000')
        .then(response => response.json())
        .then(alerts => {
            if (!alerts || alerts.length === 0) {
                alert('No alerts to export');
                return;
            }

            let csv = 'ID,Time,Source IP,Dest IP,Protocol,Attack Type,Risk Score,Packet Size\n';
            alerts.forEach(alert => {
                csv += `${alert.id},"${alert.created_at}","${alert.source_ip}","${alert.destination_ip}","${alert.protocol}","${alert.attack_type}",${alert.risk_score},${alert.packet_size}\n`;
            });

            downloadFile(csv, 'alerts.csv', 'text/csv');
        });
}

// Export as JSON
function exportJSON() {
    fetch('/api/alerts-all?limit=10000')
        .then(response => response.json())
        .then(alerts => {
            if (!alerts || alerts.length === 0) {
                alert('No alerts to export');
                return;
            }

            const json = JSON.stringify(alerts, null, 2);
            downloadFile(json, 'alerts.json', 'application/json');
        });
}

// Download file
function downloadFile(content, filename, type) {
    const element = document.createElement('a');
    element.setAttribute('href', `data:${type};charset=utf-8,` + encodeURIComponent(content));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// Print report
function printStats() {
    window.print();
}
