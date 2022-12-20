import random 

work_list = random.sample(range(-1000, 1000), 100)
print(f' Start list: {work_list}')

y = len(work_list)

for i in range(y - 1):
    for j in range(y - i - 1):
        if work_list[j] > work_list[j + 1]:
            work_list[j], work_list[j + 1] = work_list[j + 1], work_list[j]

print(f'Sorted list: {work_list}')