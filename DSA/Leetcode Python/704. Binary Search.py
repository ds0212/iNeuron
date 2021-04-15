# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


def binarySearch(nums, low, high, target):
    if low == high:
        if nums[low] == target:
            return low
        else:
            return -1

    else:
        mid = (low + high) // 2
        if nums[mid] > target:
            return binarySearch(nums, low, mid - 1, target)
        elif nums[mid] < target:
            return binarySearch(nums, mid + 1, high, target)
        else:
            return mid


nums = [-1, 0, 3, 5, 9, 12]
low = 0
high = len(nums)
target = 9
print(binarySearch(nums, low, high - 1, target))

######################################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, low, high, target):
            if high == low:
                if nums[low] == target:
                    return low
                else:
                    return -1

            else:
                mid = int((high + low) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binarySearch(nums, mid + 1, high, target)
                else:
                    return binarySearch(nums, low, mid, target)

        return binarySearch(nums, 0, len(nums) - 1, target)
