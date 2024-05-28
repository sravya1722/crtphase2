nums=[21,22,23,24,25]
target=24
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("Not found")
else:
    print("Target found at:",flag)






    
