def performinsertionsort(nums):
    n=len(nums)
    lasteleinsortedarr=0
    for firstindex in range(1,n):
        temp=nums[firstindex]
        previous=lasteleinsortedarr
        while previous>=0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=temp
        lasteleinsortedarr+=1
nums=[11,4,57,2,68,10]
print("before sorting",nums)
performinsertionsort(nums)
print("after sorting",nums)
