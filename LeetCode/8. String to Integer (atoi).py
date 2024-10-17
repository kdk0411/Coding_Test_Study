class Solution(object):
	def myAtoi(self, s):
		# 1. 초기화
		i = 0
		n = len(s)
		INT_MAX = 2 ** 31 - 1
		INT_MIN = -2 ** 31

		# 2. 공백 제거
		while i < n and s[i] == ' ':
			i += 1

		# 3. 부호 확인
		sign = 1  # 1: 양수, -1: 음수
		if i < n and (s[i] == '-' or s[i] == '+'):
			sign = -1 if s[i] == '-' else 1
			i += 1

		# 4. 숫자 변환
		result = 0
		while i < n and s[i].isdigit():
			digit = int(s[i])

			# 5. 오버플로우 체크
			if result > (INT_MAX - digit) // 10:
				return INT_MAX if sign == 1 else INT_MIN

			result = result * 10 + digit
			i += 1

		return sign * result