# Question #1:
# Write a program which will find all such numbers which are 
# divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included in the counter).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

counter = 2000
result = []
while counter < 3200:
  if counter % 7 == 0 and counter % 5 != 0 :
    result.insert(0, counter)
  counter += 1
print(result)
