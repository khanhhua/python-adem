numbers = [1, 2, 3]
slice = numbers[0:2]
slice[0] = 10

copy_von_numbers = numbers[:]
copy_von_numbers[0] = 1000000

matrix = [1, 2, 3,  10, 20, 30]
print("ABC"[0:2])
# print(numbers[0])
# print(numbers[0:2])
# print(slice[0:2])


# def sum_me(nums):
# nums = numbers
# nums[0] = 10
# return sum(nums)

print(sum(numbers))
print(numbers)