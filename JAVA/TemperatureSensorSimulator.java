import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;
import java.time.Instant;
import java.time.format.DateTimeFormatter;
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;

public class TemperatureSensorSimulator {
    private static final Random random = new Random();
    private static final int TEMP_MIN = 20;
    private static final int TEMP_MAX = 40;
    private static final OperatingSystemMXBean osBean =
        (OperatingSystemMXBean) ManagementFactory.getOperatingSystemMXBean();

    public static void main(String[] args) {
        Timer timer = new Timer();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("\nSensor simulation stopped.");
            timer.cancel(); // optional: stop the timer
        }));

        timer.scheduleAtFixedRate(new TimerTask() {
            public void run() {
                // Simulate temperature
                double temperature = TEMP_MIN + (TEMP_MAX - TEMP_MIN) * random.nextDouble();

                // Get timestamp
                String timestamp = DateTimeFormatter.ISO_INSTANT.format(Instant.now());

                // Memory usage in MB
                Runtime runtime = Runtime.getRuntime();
                double usedMemoryMB = (runtime.totalMemory() - runtime.freeMemory()) / 1024.0 / 1024.0;

                // CPU usage as a percentage (0.0 to 100.0)
                double processCpuLoad = osBean.getProcessCpuLoad(); // returns between 0.0 and 1.0
                double cpuPercent = (processCpuLoad < 0) ? 0.0 : processCpuLoad * 100;

                // Print memory and CPU usage
                System.out.printf("Memory Usage: %.2f MB | CPU Usage: %.2f%%%n", usedMemoryMB, cpuPercent);

                // Print sensor JSON
                System.out.printf(
                    "{\"sensor_id\":\"sensor_01_java\",\"timestamp\":\"%s\",\"temperature\":\"%.2f\u00B0C\"}%n",
                    timestamp, temperature
                );
            }
        }, 0, 1000);
    }
}
