const fs = require('fs');
const path = require('path');

const SENSOR_ID = process.env.SENSOR_ID || 'sensor_03_js';
const INTERVAL_MS = parseInt(process.env.INTERVAL_MS) || 1000;
const LOG_TO_FILE = process.env.LOG_TO_FILE === 'true';

function generateTemperature() {
  // Simulated temperature between 20°C and 40°C
  return (20 + Math.random() * 20).toFixed(2) + '°C';
}

function emitTemperature() {
  const data = {
    sensor_id: SENSOR_ID,
    timestamp: new Date().toISOString(),
    temperature: generateTemperature()
  };

  const output = JSON.stringify(data);

  if (LOG_TO_FILE) {
    const logPath = path.join(__dirname, `${SENSOR_ID}.log`);
    fs.appendFileSync(logPath, output + '\n');
  } else {
    // Print memory and CPU usage before output
    const mem = process.memoryUsage().rss / 1024 / 1024;
    const cpu = process.cpuUsage();
    const cpuUsagePercent = (
      (cpu.user + cpu.system) / 1000 / (INTERVAL_MS)
    ).toFixed(2); // basic approximation

    console.log(`Memory Usage: ${mem.toFixed(2)} MB | CPU Usage: ${cpuUsagePercent}%`);
    console.log(output);
  }
}

// Emit at defined interval
setInterval(emitTemperature, INTERVAL_MS);

// Emit once at start
emitTemperature();
