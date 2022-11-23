def WaitingTime(processes, no_pro, bt, wt, quantum):
    remaning_burstTime = [0] * no_pro       
    for i in range(no_pro):
         remaning_burstTime[i] = bt[i]
    currentTime = 0
    while(1):
        ProcessComplete=True
        for i in range(no_pro):
            if ( remaning_burstTime[i] > 0) :
                ProcessComplete= False                  
                if (remaning_burstTime[i] > quantum) :
                    currentTime+= quantum
                    remaning_burstTime [i] -= quantum
                else:
                    currentTime = currentTime + remaning_burstTime [i]
                    wt[i] = currentTime - bt[i]
                    remaning_burstTime [i] = 0
        if (ProcessComplete == True):
            break
def TurnAroundTime(processes, no_pro, bt, wt, tat):
    for i in range(no_pro):
        tat[i] = bt[i] + wt[i]
def avgTime(processes, no_pro, bt, quantum):
    wt = [0] * no_pro
    tat = [0] * no_pro
    WaitingTime(processes, no_pro, bt, wt, quantum)
    TurnAroundTime(processes, no_pro, bt,wt, tat)
    print("Processes    Burst Time     Waiting","Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(no_pro):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i]) 
    print("\nAverage waiting time = %.5f "%(total_wt /no_pro) )
    print("Average turn around time = %.5f "% (total_tat / no_pro))
if __name__ =="__main__":     
    no_pro=(int(input("Enter Number of Process")))
    proc=[]
    for i in range (1,no_pro+1):
        proc.append(i)
    burst_time=[0]*no_pro
    for j in range (no_pro):
         burstT=(int(input("Enter  Process Burst Time")))
         burst_time[j]=burstT
    quantum =2
    avgTime(proc, no_pro, burst_time, quantum)



     



  
