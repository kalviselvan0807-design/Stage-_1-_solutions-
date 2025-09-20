#Question 3

a = int(input("Enter the a value: "))
if a % 2 == 0:
    a = a - 1
d = a * 2
for i in range(1, d, 2):
    print(i, end=" ")

#Output 1:
Enter the a value: 1
1
Enter the a value: 3
1,3
