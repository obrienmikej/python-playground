def two_sum_hash_table(numbers: List[int], target_sum: int) -> List[int]:
  """
  Finds the indices of two numbers in the list that add up to the target sum using a hash table.

  Args:
      numbers: The list of integers.
      target_sum: The target sum.

  Returns:
      A list containing the indices of the two numbers that add up to the target sum, or an empty list if not found.
  """
  seen_numbers = {}
  for current_index, number in enumerate(numbers):
    complement = target_sum - number
    if complement in seen_numbers:
      return [seen_numbers[complement], current_index]
    seen_numbers[number] = current_index
  return []