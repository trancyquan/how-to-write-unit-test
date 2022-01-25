def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for idx, val in enumerate(nums):
        if target - val in nums[idx + 1:]:
            return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]