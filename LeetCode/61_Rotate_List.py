class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # filter un-rotatable conditions
        if not head or not head.next or k == 0:
            return head

        # Count the Node & remember the last
        cnt = 1
        last = head
        while last.next:
            cnt += 1
            last = last.next

        # link the last to the head
        last.next = head

        # un-link the point
        k %= cnt
        point = head
        for _ in range(cnt - k - 1):
            point = point.next
        answer = point.next
        point.next = None

        return answer
