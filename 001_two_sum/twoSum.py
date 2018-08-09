class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]],i]
            else:
                buff_dict[target-nums[i]] = i
    def twoSum2(self,nums,target):
        d = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
    def twoSum3(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
if __name__ == '__main__':
    nums = [2, 72, 2, 15]
    target = 4
    s = Solution()
    res = s.twoSum2(nums,target)
    print (res)