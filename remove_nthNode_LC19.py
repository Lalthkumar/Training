from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return dummy.next

# Helper to build and print linked list
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Command-line execution
if __name__ == "__main__":
    import sys
    values = list(map(int, sys.argv[1].split(',')))  # e.g., "1,2,3,4,5"
    n = int(sys.argv[2])                             # e.g., "2"
    head = build_linked_list(values)
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)
    print_linked_list(new_head)
