def load_processes(filename="processes.txt"):
    processes = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                pid, burst, arrival = line.strip().split(',')
                processes.append([pid, int(burst), int(arrival), 0, 0, int(burst)])
    
    processes.sort(key=lambda x: x[2])
    return processes

def format_results(output_string, algorithm_name, processes, gantt_chart):
    total_wt = 0
    total_tat = 0
    
    output_string += f"\n--- {algorithm_name} ---\n"
    output_string += "Process | Arrival | Burst | Waiting | Turnaround\n"
    output_string += "-------------------------------------------------\n"
    
    processes.sort(key=lambda x: x[0])
    
    for p in processes:
        pid, burst, arrival, wt, tat, _ = p
        total_wt += wt
        total_tat += tat
        output_string += f"{pid:<8}| {arrival:<8}| {burst:<6}| {wt:<8}| {tat:<10}\n"

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)
    
    output_string += "\n-------------------------------------------------\n"
    output_string += f"Average Waiting Time: {avg_wt:.2f}\n"
    output_string += f"Average Turnaround Time: {avg_tat:.2f}\n"
    output_string += f"Gantt Chart: {' -> '.join(gantt_chart)}\n"
    output_string += "="*50 + "\n"
    
    return output_string

def fcfs(processes):
    completed_processes = []
    gantt_chart = []
    current_time = 0
    
    for p in processes:
        pid, burst, arrival, _, _, _ = p
        
        if current_time < arrival:
            current_time = arrival
        
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        completed_processes.append([pid, burst, arrival, waiting_time, turnaround_time, 0])
        
        gantt_chart.append(pid)
        current_time += burst
        
    return completed_processes, gantt_chart

def sjf(processes):
    completed_processes = []
    gantt_chart = []
    current_time = 0
    n = len(processes)
    
    remaining_processes = [p[:] for p in processes]
    
    while len(completed_processes) < n:
        ready_queue = [p for p in remaining_processes if p[2] <= current_time]
        
        if not ready_queue:
            current_time = min(p[2] for p in remaining_processes)
            continue
            
        shortest_job = min(ready_queue, key=lambda x: x[1])
        
        pid, burst, arrival, _, _, _ = shortest_job
        
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        completed_processes.append([pid, burst, arrival, waiting_time, turnaround_time, 0])
        
        gantt_chart.append(pid)
        current_time += burst
        
        remaining_processes.remove(shortest_job)
        
    return completed_processes, gantt_chart

def round_robin(processes, quantum):
    completed_processes = []
    gantt_chart = []
    current_time = 0
    n = len(processes)
    
    ready_queue = []
    procs_data = [p[:] for p in processes]
    
    process_idx = 0

    while len(completed_processes) < n:
        while process_idx < n and procs_data[process_idx][2] <= current_time:
            ready_queue.append(procs_data[process_idx])
            process_idx += 1
            
        if ready_queue:
            current_process = ready_queue.pop(0)
            pid, burst, arrival, _, _, remaining_burst = current_process
            
            gantt_chart.append(pid)
            
            exec_time = min(quantum, remaining_burst)
            current_time += exec_time
            remaining_burst -= exec_time
            current_process[5] = remaining_burst

            while process_idx < n and procs_data[process_idx][2] <= current_time:
                ready_queue.append(procs_data[process_idx])
                process_idx += 1

            if remaining_burst == 0:
                turnaround_time = current_time - arrival
                waiting_time = turnaround_time - burst
                completed_processes.append([pid, burst, arrival, waiting_time, turnaround_time, 0])
            else:
                ready_queue.append(current_process)
        else:
            if process_idx < n:
                current_time = procs_data[process_idx][2]
            else:
                break
                
    return completed_processes, gantt_chart

def main():
    output_string = ""
    
    processes_list = load_processes("processes.txt")
    if not processes_list:
        print("File processes.txt not found or is empty.")
        return

    output_string += "Initial Process Data:\n"
    for p in processes_list:
        output_string += f"PID: {p[0]}, Burst: {p[1]}, Arrival: {p[2]}\n"
    output_string += "="*50 + "\n"
    
    fcfs_processes, fcfs_gantt = fcfs(processes_list[:])
    output_string = format_results(output_string, "First Come First Serve (FCFS)", fcfs_processes, fcfs_gantt)
    
    sjf_processes, sjf_gantt = sjf(processes_list[:])
    output_string = format_results(output_string, "Shortest Job First (SJF) Non-Preemptive", sjf_processes, sjf_gantt)
    
    for q in [2, 4, 8]:
        rr_processes, rr_gantt = round_robin(processes_list[:], quantum=q)
        output_string = format_results(output_string, f"Round Robin (Quantum = {q})", rr_processes, rr_gantt)
        
    try:
        with open("output.txt", "w") as f:
            f.write(output_string)
        print("Execution complete. Results have been saved to 'output.txt'")
    except IOError:
        print("Failed to write to output.txt")

if __name__ == "__main__":
    main()