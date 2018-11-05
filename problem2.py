# Question #2:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8 Then, the output should be: 40320

sequence = [8, 5]
results = []
for s in sequence:
    result = 1
    for i in range(1, s + 1):
        result *= i
    results.append(result)
    
print(results)