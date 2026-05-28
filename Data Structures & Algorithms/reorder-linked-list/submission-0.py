class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        dummy = ListNode(0)
        tail = dummy
        count = 0

        while i <= j:
            if count % 2 == 0:
                tail.next = nodes[i]
                i += 1
            else:
                tail.next = nodes[j]
                j -= 1

            tail = tail.next
            count += 1

        tail.next = None