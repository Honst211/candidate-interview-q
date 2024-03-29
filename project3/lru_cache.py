"""
请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。 实现 LRUCache 类：

LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：

输入 ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] 输出 [null, null, null, 1, null, -1, null, -1, 3, 4]

解释

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1); // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2); // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1); // 返回 -1 (未找到)
lRUCache.get(3); // 返回 3
lRUCache.get(4); // 返回 4
提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
"""


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node: ListNode):
        # 将节点移动到链表头部
        self._remove_node(node)
        self._add_to_head(node)

    def _add_to_head(self, node: ListNode):
        # 添加节点到链表头部
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        # 移除节点
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                # 缓存已满，删除最久未使用的节点
                del_node = self.tail.prev
                self._remove_node(del_node)
                del self.cache[del_node.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


if __name__ == '__main__':
    """
    简单点说就是数据结构设置为一双向链表,一字典
    字典用于快速检索,用于get和put的基本操作
    链表用于记录数据的插入顺序
    当数据get出去之后, 将链表在断开的地方给接起来
    当数据put的时候发现已经满了, 那么根据题意, 直接删除尾节点就可以了
    """
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    print(lRUCache.cache)
    lRUCache.put(2, 2)
    print(lRUCache.cache)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.cache)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.cache)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))

