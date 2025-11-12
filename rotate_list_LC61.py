# rotate_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        n = 1
        current = head
        while current.next:
            current = current.next
            n += 1
        tail = current
        tail.next = head
        k %= n

        steps_to_new_tail = n - k - 1
        current = head
        for _ in range(steps_to_new_tail):
            current = current.next

        new_head = current.next
        current.next = None
        return new_head

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python rotate_list.py k val1 val2 val3 ...")
        sys.exit(1)

    k = int(sys.argv[1])
    values = list(map(int, sys.argv[2:]))
    head = build_linked_list(values)

    solution = Solution()
    rotated = solution.rotateRight(head, k)
    print("Rotated List:", rotated)
