from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = d

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next

        cur.next = list1 if list1 else list2
        return d.next

# Helper functions
def build_list(values):
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
if __name__ == "__main__":
    list1 = build_list([1, 3, 5])
    list2 = build_list([2, 4, 6])
    merged = Solution().mergeTwoLists(list1, list2)
    print_list(merged)
