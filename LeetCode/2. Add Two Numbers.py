class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		dummy = ListNode()  # 결과를 저장할 가짜(head) 노드
		current = dummy
		carry = 0

		while l1 or l2 or carry:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0
			total = val1 + val2 + carry

			carry = total // 10  # 올림 값
			current.next = ListNode(total % 10)  # 자리수 계산 후 노드 추가
			current = current.next

			if l1: l1 = l1.next
			if l2: l2 = l2.next

		return dummy.next
