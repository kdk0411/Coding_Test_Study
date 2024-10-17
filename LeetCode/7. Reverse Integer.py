class Solution(object):
	def reverse(self, x):
		x_str = str(x)
		if x_str[0] == '-':
			ret = int('-' + x_str[:0:-1])
		else:
			ret = int(x_str[::-1])

		if ret < -2 ** 31 or ret > 2 ** 31 - 1:
			return 0
		return ret