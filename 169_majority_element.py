class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[int(len(nums)/2)]


test = Solution()
print(test.majorityElement('1231231243'))
