# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # filter: head is None
        if not head:
            return

        # make arr of ListNode
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        # Relink the ListNodes
        N = len(arr)
        cur = arr[0]
        for idx in range(N - 1):
            # find the index
            tmp = idx // 2 + 1
            idx = tmp if idx % 2 else N - tmp
            # link the node
            nxt = arr[idx]
            cur.next = nxt
            cur = nxt
        # handle the last node
        cur.next = None


        

