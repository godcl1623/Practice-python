# def bubble_sort(array):
#   for cycle in range(len(array) - 1):
#     swap = False
#     for index in range(len(array) - cycle - 1):
#       if array[index] > array[index + 1]:
#         array[index], array[index + 1] = array[index + 1], array[index]
#         swap = True
#     if swap == False:
#       break
#   return array

# def select_sort(array):
#   for cycle in range(len(array) - 1):
#     lowest = cycle
#     for index in range(cycle, len(array)):
#       if array[index] < array[lowest]:
#         lowest = index
#     array[cycle], array[lowest] = array[lowest], array[cycle]
#   return array

def insert_sort(array):
  for cycle in range(len(array) - 1):
    for index in range(cycle+1, 0, -1):
      if array[index] < array[index - 1]:
        array[index], array[index - 1] = array[index - 1], array[index]
      else:
        break
  return array

import random;

rand_array = random.sample(range(100), 50)
# print(bubble_sort(rand_array));
# print(select_sort(rand_array));
print(insert_sort(rand_array));