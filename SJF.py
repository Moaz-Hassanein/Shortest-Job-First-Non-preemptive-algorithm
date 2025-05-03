# process = [burst_time , arrival_time , process_id]
def sjf(processesList):
    t=0
    ganttChart=[]
    completedProcesses={} #dictionary of lists
    while processesList :
        availableProcesses=[]
        for process in processesList :
            if process[1] <= t :
                availableProcesses.append(process)
        #if no processes available
        if availableProcesses == []:
            t+=1

        else:
            availableProcesses.sort()
            process = availableProcesses[0]
            burstTime = process[0]
            arrivalTime = process[1]
            process_id = process[2]
            ganttChart.append(process_id)
            t+=burstTime
            turnaroundTime= t - arrivalTime
            waitingTime = turnaroundTime - burstTime
            responseTime = waitingTime #responseTime always equal to waitingTime
            completedProcesses[process_id]=[responseTime,turnaroundTime,waitingTime]
            processesList.remove(process)

    return completedProcesses

def calculateAvgs(completedProcesses):
    waitingSum=0
    turnaroundSum = 0
    Counter=0
    for p in completedProcesses.values():
        waitingSum+= p[0]
        turnaroundSum += p[1]
        Counter+=1
    waitingAvg= waitingSum / Counter
    responseAvg = waitingAvg
    turnaroundAvg = turnaroundSum / Counter

    avgList = [responseAvg,turnaroundAvg,waitingAvg]

    return avgList

if __name__ == "__main__":
    processList=[]
    n=int(input("enter number of processes: "))
    for i in range(n):
        burst = int(input(f"Enter burst time for process p{i + 1}: "))
        arrival = int(input(f"Enter arrival time for process p{i + 1}: "))
        pid = f"p{i + 1}"
        processList.append([burst, arrival, pid])

    completed = sjf(processList)
    averages = calculateAvgs(completed)

    print("\nProcess\tResponse\tTurnaround\tWaiting")
    for pid, data in completed.items():
        print(f"{pid}\t{data[0]}\t\t{data[1]}\t\t{data[2]}")

    print("\nAverages: [Response Avg, Turnaround Avg, Waiting Avg]")
    print(averages)

#processList=[[6,2,"p1"],[2,5,"p2"],[8,1,"p3"],[3,0,"p4"],[4,4,"p5"]]
#processList = [[1, 0, "p1"], [4, 1, "p2"], [7, 2, "p3"], [5, 3, "p4"]]
#processList = [[6, 0, "p1"], [8, 0, "p2"], [7, 0, "p3"], [3, 0, "p4"]]