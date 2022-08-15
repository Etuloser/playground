# 链表定义
class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = self.next


def f(x):
    """
    无终止条件的递归
    """
    return x + f(x-1)


def f1(x):
    """
    加一个终止条件
    """
    if x > 0:
        return x + f1(x-1)
    else:
        return 0


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    print(l1)
