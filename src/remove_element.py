def removeElement(nums: int, val: int) -> int:
    # Initialize a pointer for the position to insert elements that are not equal to val
    k = 0    

    for i in range(len(nums)):
        if nums[i] != val:
            # If the current element is not equal to val, keep
            nums[k] = nums[i]
            k += 1
    # Return the elements that are not equal to val
    return k

def removeElementTwoPointers(nums, val):
  # Pointer i: for the current position
  # Pointer j: for the non-val elements
  i, j = 0, 0

  while i < len(nums):
    if nums[i] != val:
      # Swap the non-val element with the current element if they are different
      nums[i], nums[j] = nums[j], nums[i]
      j += 1
    i += 1
  # Return the number of non-val elements
  return j
