class SingleNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SingleLinkList(object):
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def travel(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def append(self, val):
        node = SingleNode(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        


if __name__ == '__main__':
    head = [1, 1, 1, 2, 3]
    l1 = SingleLinkList()
    for num in head:
        l1.append(num)
    l1.travel()
