def setZeroAside(nums):
    pos=0
    for i in range (1,len(nums)):
        if nums[i]!=0:
            nums[pos]=nums[i]
            pos+=1
        
    #set ramining part wiht 0 form pos to lenght
    for i in range(pos,len(nums)):
        nums[i]=0
    return nums

list=[2,0,5,0,0,4,34,4,0]
print("Result is : ",setZeroAside(list))