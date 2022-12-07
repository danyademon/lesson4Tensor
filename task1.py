import random 

work_list = random.sample(range(-1000,1000),100)
print(f' Start list: {work_list}')

for i in range(len(work_list)-1):
    for j in range(len(work_list)-i-1):
        if work_list[j] > work_list[j+1]:
            work_list[j], work_list[j+1] = work_list[j+1], work_list[j]

print(f'Sorted list: {work_list}')