start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
  print(square_list)
square_list.sort()

print(start_list)
print(square_list)