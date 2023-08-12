from typing import List


# Subarray/Substring - A subarray is a contiguous non-empty sequence of elements within an array.
def get_subarrays(arr):
    subarrays = []
    n = len(arr)

    # Generate all subarrays
    for start in range(n):
        for end in range(start + 1, n + 1):
            subarray = arr[start:end]
            subarrays.append(subarray)

    return subarrays


# Subsequence - A subsequence maintain relative ordering of elements but may or may not be a contiguous part of an array
def get_subsequences(arr):
    def backtracking(arr, index, path, results):
        results.append(path[:])  # Add a copy of the current subsequence to the results list

        for i in range(index, len(arr)):
            path.append(arr[i])  # Include the current element in the subsequence
            backtracking(arr, i + 1, path, results)  # Recursively backtrack and explore remaining elements
            path.pop()  # Remove the current element from the subsequence

    results = []
    backtracking(arr, 0, [], results)
    return results

# Example usage


# Subsets - A subset MAY NOT maintain relative ordering of elements and can or cannot be a contiguous part of an array
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def backtracking(nums, path):
        res.append(path[:])

        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                path.append(nums[i])
                backtracking(nums[i + 1:], path)
                path.pop()

        return

    backtracking(nums, [])
    return res

my_list = [1, 2, 3]
result = subsetsWithDup(my_list)
print(result)
