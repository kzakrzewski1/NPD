import os
import random

random.seed(123)

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
times_of_day = ['morning','evening']

parent_dir = "/NPD/Z6/Folders"

paths = []

for day in days:
    for time in times_of_day:
        paths.append(os.path.join(parent_dir, day + '/' + time))


abc = ['A','B','C']

for path in paths:
    os.makedirs(path, exist_ok=True)

    f = open(path + '/Solutions.csv','w')
    f.write("Model; Output value; Time of computation;\n")

    r1 = abc[random.randint(0,2)]
    r2 = random.randint(0,1000)
    r3 = random.randint(0,1000)

    f.write(f"{r1}; {r2}; {r3}")
    f.close()


sum_A=0

for folder in os.listdir(os.path.join(parent_dir)):
    for time in times_of_day:

        f = open(parent_dir + '/' + folder + '/' + time + '/' + 'Solutions.csv', 'r')
        sol = (f.read().splitlines()[1].split())
        f.close()

        if sol[0].replace(";", "") == 'A':
            sum_A += int(sol[2].replace(";", ""))
       

print(f"Total time of computation in model A: {sum_A}")

