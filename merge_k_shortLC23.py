import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):  # corrected __init__ spelling
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        D = ListNode()
        cur = D

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return D.next

# Helper to build linked list from list
def build_linked_list(arr):
    dummy = ListNode()
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

# Helper to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    # Example input: 3 sorted linked lists
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]

    sol = Solution()
    merged = sol.mergeKLists(lists)
    print_linked_list(merged)
