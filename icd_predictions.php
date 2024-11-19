 <!-- Also put the following code in interface/patient_file/summary/demographics.php so that it links to icd_predictions.php 
<!-- <div class="patient-links"> -->
        <!-- Link to ICD Predictions page -->
<!--         <a href="icd_predictions.php" target="_blank">View ICD Predictions</a> -->
<!--     </div>
 -->




<!-- Currently the data are all filler and do not link to anything. --> 

<?php
session_start();

// Ensure patient ID (pid) is set; if not, default to 0
$pid = isset($_GET['pid']) ? intval($_GET['pid']) : 0;
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ICD Predictions</title>
    <!-- Add Chart.js from CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="margin-bottom: 20px;">
        <!-- Navigate back to Patient Summary -->
        <a href="http://localhost:8000/interface/patient_file/summary/demographics.php?pid=<?php echo $pid; ?>" class="css_button_small" style="text-decoration: none;">⬅️ Back to Patient Summary</a>
    </div>


    </div>


    <h2>ICD Predictions for Hospital Stay</h2>
    <!-- Container for Line Chart (Time-series) -->
    <canvas id="timeSeriesChart" width="600" height="400"></canvas>

    <h2>ICD Code Confidence Levels</h2>
    <!-- Container for Bar Chart -->
    <canvas id="confidenceChart" width="600" height="400"></canvas>

    <h2>Predicted ICD Codes and Timestamps</h2>
    <!-- Table for ICD Codes with Confidence Levels and Timestamps -->
    <table id="predictionsTable" border="1">
        <thead>
            <tr>
                <th>ICD Code</th>
                <th>Confidence Level</th>
                <th>Timestamp</th>
            </tr>
        </thead>
        <tbody>
            <!-- Rows will be populated dynamically -->
        </tbody>
    </table>
</body>

</html>
<script>
// Sample data for demonstration purposes; replace with data fetched from your backend
const sampleTimeSeriesData = {
    labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'], // X-axis labels (e.g., days of stay)
    data: [30, 45, 35, 50, 60] // Y-axis values (e.g., predictions over time)
};

const sampleICDConfidenceData = {
    labels: ['ICD Code 1', 'ICD Code 2', 'ICD Code 3'], // X-axis labels (ICD codes)
    data: [0.7, 0.5, 0.9] // Y-axis values (confidence levels)
};

const samplePredictionTableData = [
    { icd_code: 'ICD Code 1', confidence: 0.7, timestamp: '2024-11-01' },
    { icd_code: 'ICD Code 2', confidence: 0.5, timestamp: '2024-11-02' },
    { icd_code: 'ICD Code 3', confidence: 0.9, timestamp: '2024-11-03' }
];

// Line Chart: Time-Series Predictions Over Hospital Stay
const timeSeriesCtx = document.getElementById('timeSeriesChart').getContext('2d');
const timeSeriesChart = new Chart(timeSeriesCtx, {
    type: 'line',
    data: {
        labels: sampleTimeSeriesData.labels,
        datasets: [{
            label: 'Prediction Over Time',
            data: sampleTimeSeriesData.data,
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: false,
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { title: { display: true, text: 'Days' }},
            y: { title: { display: true, text: 'Prediction Value' }}
        }
    }
});

// Bar Chart: ICD Predictions with Confidence Levels
const confidenceCtx = document.getElementById('confidenceChart').getContext('2d');
const confidenceChart = new Chart(confidenceCtx, {
    type: 'bar',
    data: {
        labels: sampleICDConfidenceData.labels,
        datasets: [{
            label: 'Confidence Level',
            data: sampleICDConfidenceData.data,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { title: { display: true, text: 'ICD Code' }},
            y: { title: { display: true, text: 'Confidence Level' }, beginAtZero: true }
        }
    }
});

// Populate Table with ICD Codes, Confidence Levels, and Timestamps
const tableBody = document.getElementById('predictionsTable').getElementsByTagName('tbody')[0];
samplePredictionTableData.forEach(prediction => {
    const row = tableBody.insertRow();
    const cellICDCode = row.insertCell(0);
    const cellConfidence = row.insertCell(1);
    const cellTimestamp = row.insertCell(2);
    cellICDCode.textContent = prediction.icd_code;
    cellConfidence.textContent = prediction.confidence;
    cellTimestamp.textContent = prediction.timestamp;
});
</script>
