#Question 4:
# Input 
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Dictionary to store counts
multiples_count = {i: 0 for i in range(1, 10)}

# Count multiples
for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            multiples_count[i] += 1

print(multiples_count)

#Output:

 {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
