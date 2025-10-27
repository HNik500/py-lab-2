n = int(input("Enter no of jobs:"))
jobs = []
          
for i in range(n):
    profit = int(input(f"enter profit for jobs {i+1}:"))
    deadline = int(input(f"enter deadline for jobs {i+1}:"))
    jobs.append([profit,deadline])


max_deadline = max(job[1] for job in jobs)

slots= [0]*max_deadline

jobs.sort(key=lambda x:x[0],reverse=True)

total_profit = 0

for profit,deadline in jobs:
    for j in range(deadline-1,-1,-1):
        if slots[j]==0:
            slots[j]=1
            total_profit+=profit
            break
print("\nTotal profit =", total_profit)