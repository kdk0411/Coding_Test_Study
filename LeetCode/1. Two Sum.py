class Solution(object):
	def twoSum(self, nums, target):
		ret = {}
		for i, num in enumerate(nums):
			diff = target-num
			if diff in ret:
				return [ret[diff], i]
			ret[num] = i
