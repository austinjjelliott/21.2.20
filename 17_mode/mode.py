def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    return max(set(nums), key = nums.count)

# Explanation:
# set(nums): This converts the list nums into a set, which removes any duplicate elements. For example, if nums is [1, 2, 2, 3, 3, 3], then set(nums) will be {1, 2, 3}.

# key = nums.count: The key parameter in the max function specifies a function to be called on each element of the iterable before making comparisons. Here, nums.count is a function that counts the occurrences of a given element in the list nums.

# max(set(nums), key = nums.count): The max function iterates over each element in the set and applies the nums.count function to each element. It then returns the element with the highest count.