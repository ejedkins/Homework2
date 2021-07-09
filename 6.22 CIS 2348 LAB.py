#Elijah Jedkins PSID: 1786452

#Read in first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

#Read in second equation, dx + ey = f
d = int(input())
e = int(input())
f = int(input())

solution_exist = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            solution_exist = True
#If the solution does not exist
if not solution_exist:
    print("No solution")
