# CPU Scheduling Algorithm Simulator

A simple Python-based simulator for classic CPU scheduling algorithms. This project implements First Come First Serve (FCFS), Shortest Job First (SJF Non-Preemptive), and Round Robin (RR) to calculate and display waiting times, turnaround times, and a text-based Gantt chart.

---

## ✨ Features

- **Three Classic Algorithms**: Implements FCFS, Non-Preemptive SJF, and Round Robin.
- **Data from File**: Reads process data (PID, Burst Time, Arrival Time) from an external `processes.txt` file.
- **Performance Metrics**: Automatically calculates and displays the Waiting Time and Turnaround Time for each process.
- **Aggregate Analysis**: Computes the average Waiting Time and Turnaround Time for each algorithm.
- **Gantt Chart**: Displays a simple text-based Gantt Chart to visualize the execution sequence.
- **Quantum Analysis**: Tests Round Robin with multiple quantum values (2, 4, 8) for performance comparison.

---

## 🚀 How to Run

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/ItsMeD4N/cpu-scheduling-simulator.git)
    cd cpu-scheduling-simulator
    ```

2.  **Ensure `processes.txt` is configured:**
    Make sure the `processes.txt` file is in the same directory and contains the process data in the format `PID,BurstTime,ArrivalTime`.

    ```
    # PID,BurstTime,ArrivalTime
    P1,6,0
    P2,8,4
    P3,7,9
    P4,3,12
    ```

3.  **Run the script:**

    ```bash
    python cpu_scheduling.py
    ```

4.  **Check the output:**
    The results will be automatically saved to the `output.txt` file.

---

## 📂 File Structure
