# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if slow is None or fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    input = [3, 2, 0, -4]
    pos = 1
    node = ListNode(input[0])
    root = node
    save = None
    for i in range(1, len(input)):
        node.next = ListNode(input[i])
        node = node.next
        if pos == i:
            save = node
    node.next = save

    print(obj.hasCycle(root))
    # while root is not None:
    #    print(root.val)
    #    root = root.next

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
