from typing import Optional
import sys

class ListNode:
    def __init__(self, val=0, next=None):  # corrected __init__
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = current.next.next

        return dummy.next

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

if __name__ == "__main__":
    # Example usage: python swap_pairs.py "1,2,3,4"
    values = list(map(int, sys.argv[1].split(',')))
    head = build_linked_list(values)
    solution = Solution()
    new_head = solution.swapPairs(head)
    print_linked_list(new_head)
