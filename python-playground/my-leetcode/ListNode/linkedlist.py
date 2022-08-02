"""
https://github.com/keon/algorithms
"""


class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == '__main__':
    l1 = SinglyLinkedListNode(10)
    l2 = SinglyLinkedListNode(12)
    l1.next = l2
    while l1:
        print(l1.value)
        l1 = l1.next
