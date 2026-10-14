nums = [3,8,12,5,20,7]
count = 0
total = 0

for num in nums:
    if num>6:
        print(num)
        count = count + 1
        total = total + num
print("Count of numbers greater than 6:", count)
print("Sum of numbers greater than 6:", total)
        