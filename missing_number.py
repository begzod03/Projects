# # Question : Find the missing number in the array

#              You are given an array of positive numbers from 1 to n, such that all numbers from 1 to
#              n are present except one number x. You have to find x. The input array is not sorted.
#              Look at the below array and give it a try before checking the solution.



# nums = [3, 7, 1, 2, 8, 4, 5]
# y= []
# temp = 0
# x = 0
# for i in range(len(nums) + 1):
#     temp += 1
#     y.append(temp)
#     print(y)
#
# if sum(y) != sum(nums):
#     missing = sum(y) - sum(nums)
#     print("The missing number is " + str(missing))

        #This is not so good because time complexity is O(n^2)

#   OR
        # This is the best case scenario because it has time complexity of O(n) (linear )


nums = [3, 7, 1, 2, 8, 4, 5]

wrong_sum = sum(nums)
x = len(nums) + 1
correct_sum = (x * (x+1)) / 2
print(correct_sum-wrong_sum)
