import time
start_time = time.time()
##################################################
nums = [1, 3, 5, 7, 9]
target = 10
result = {}
# curr_idx = 0
# while curr_idx < len(nums) - 1:
#   for i in range(len(nums)):
#     if i == curr_idx:
#       continue
#     else:
#       if target - nums[curr_idx] == nums[i]:
#         result.add(curr_idx)
#         result.add(i)
#   curr_idx += 1
# for i in range(len(nums)):
#   if nums[i] in result:
#     print([result[nums[i]], i])
#   else:
#     result[target - nums[i]] = i
for i, n in enumerate(nums):
  m = target - n
  if m in result:
    print([result[m], i])
  else:
    result[n] = i

##################################################
end_time = time.time()
print('time: ', end_time - start_time)