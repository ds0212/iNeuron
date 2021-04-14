# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

nums = [3, 1, 2, 10, 1]

# s = [for i in num]
s = []
h = 0
for i in nums:
    h += i
    s.append(h)
print(s)

#####################################################


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        List = []
        h = 0
        for i in nums:
            h += i
            List.append(h)
        return List
