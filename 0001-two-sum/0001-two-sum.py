class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用哈希表存储遍历过的数字及其索引
        num_to_index = {}
        for i, num in enumerate(nums):
            # 计算差值
            complement = target - num
            # 如果差值在哈希表中，直接返回当前索引和差值的索引
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # 否则，将当前数字及其索引添加到哈希表中
            num_to_index[num] = i
        # 如果没有找到解，返回空列表（实际上，题目保证了至少有一个有效答案）
        return []