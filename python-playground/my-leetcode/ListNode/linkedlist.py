"""
https://github.com/keon/algorithms
"""


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


ltm_info1 = {
    'hostname': 'SZASHO-FB4-SDAW',
    'vip': '12.255.25.39',
    'mbr': '10.1.255.23,12.68.6.1'
}
ltm_info2 = {
    'hostname': 'SZASHO-FB4-SDAW',
    'vip': '10.1.255.23',
    'mbr': '11.31.58.69'
}
ltm_info3 = {
    'hostname': 'SZASHO-FB4-SDAW',
    'vip': '11.31.58.69',
    'mbr': '55.1.36.98'
}

store = [ltm_info1, ltm_info2, ltm_info3]


def get_next(node: SingleNode):
    pre_node_mbr = node.val['mbr'].split(',')
    for doc in store:
        if doc['vip'] in pre_node_mbr:
            return SingleNode(doc)
    return False


if __name__ == '__main__':
    node1 = SingleNode(ltm_info1)
    l1 = SingleLinkList()
    l1.head = node1
    cur = l1.head
    while cur:
        cur.next = get_next(cur)
        cur = cur.next
    l1.travel()
