def removeElement(nums, val):
    e = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[e] = nums[i]
            e += 1
    return e
