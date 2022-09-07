'''
# 1 + 2 + 3 + 4 + ......... + n

n = int(input("Enter the last number of series: "))
sum = 0

for x in range(1, n+1, 1):
    sum = sum + x

print(sum)

# 2 + 4 + 6 + 8 + ......... + n

n = int(input("Enter the last even number of series: "))
sum = 0

for y in range(2, n+1, 2):
    sum = sum + y
print(sum)

# 1 + 3 + 5 + 7 + ......... + n

n = int(input("Enter the last even number of series: "))
sum = 0

for y in range(1, n+1, 2):
    sum = sum + y

print(sum)

# 4 + 8 + 12 + 16 + ......... + n

n = int(input("Enter the last even number of series: "))
sum = 0

for z in range(4, n+1, 4):
    sum = sum + z

print(sum)
'''


# 1*1 + 2*2 + 3*3 + 4*4 + ......... + n

n = int(input("Enter the last number of series: "))
sum = 0

for x in range(1, n+1, 1):
    sum = sum + x*x
print(sum)