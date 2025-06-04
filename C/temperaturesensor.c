#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <psapi.h>
#include <stdbool.h>

// Global flag for Ctrl+C detection
volatile bool keep_running = true;

// Ctrl+C handler
BOOL WINAPI handle_ctrl_c(DWORD signal) {
    if (signal == CTRL_C_EVENT) {
        keep_running = false;
        return TRUE;
    }
    return FALSE;
}

// Get timestamp in RFC 3339 format with nanoseconds
void get_timestamp(char *buffer, size_t size) {
    FILETIME ft;
    GetSystemTimePreciseAsFileTime(&ft);

    ULONGLONG t = (((ULONGLONG)ft.dwHighDateTime << 32) | ft.dwLowDateTime) - 116444736000000000ULL;
    time_t seconds = t / 10000000ULL;
    long nanos = (long)((t % 10000000ULL) * 100); // nanoseconds

    struct tm tm_utc;
    gmtime_s(&tm_utc, &seconds);

    snprintf(buffer, size, "%04d-%02d-%02dT%02d:%02d:%02d.%09ldZ",
             tm_utc.tm_year + 1900,
             tm_utc.tm_mon + 1,
             tm_utc.tm_mday,
             tm_utc.tm_hour,
             tm_utc.tm_min,
             tm_utc.tm_sec,
             nanos);
}

// Simulate temperature between 20–40 °C
float simulate_temperature() {
    return 20.0f + ((float)rand() / RAND_MAX) * 20.0f;
}

// Real memory usage using Windows API
float get_memory_usage_mb() {
    PROCESS_MEMORY_COUNTERS pmc;
    if (GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc))) {
        return (float)pmc.WorkingSetSize / (1024.0f * 1024.0f); // in MB
    }
    return -1.0f; // Error fallback
}

// Simulate CPU usage (placeholder)
float simulate_cpu_usage_percent() {
    return (float)(rand() % 50) / 100.0f;
}

int main() {
    SetConsoleOutputCP(1252);  // For proper ° symbol
    SetConsoleCtrlHandler(handle_ctrl_c, TRUE); // Handle Ctrl+C

    srand((unsigned int)time(NULL));
    const char *sensor_id = "sensor_04_c";
    char timestamp[64];

    while (keep_running) {
        get_timestamp(timestamp, sizeof(timestamp));
        float temp = simulate_temperature();
        float mem = get_memory_usage_mb();
        float cpu = simulate_cpu_usage_percent();

        printf("Memory Usage: %.2f MB | CPU Usage: %.2f%%\n", mem, cpu * 100);
        printf("{\"sensor_id\":\"%s\",\"timestamp\":\"%s\",\"temperature\":\"%.2f\xB0""C\"}\n\n",
               sensor_id, timestamp, temp);

        Sleep(1000); // Delay for 1 second
    }

    printf("Sensor simulation stopped.\n");
    return 0;
}
