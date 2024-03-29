"""
2. 合并k个生序链表
给你一个链表数组，每个链表都已经按升序排列。 请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1： 输入：lists = [[1,4,5],[1,3,4],[2,6]] 输出：[1,1,2,3,4,4,5,6] 解释：链表数组如下： [ 1->4->5, 1->3->4, 2->6 ] 将它们合并到一个有序链表中得到。 1->1->2->3->4->4->5->6

示例 2： 输入：lists = [] 输出：[]

示例 3： 输入：lists = [[]] 输出：[]

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定义节点的比较方法
    def __lt__(self, other):
        return self.val < other.val


class Solution(object):
   def mergeKLists(self, lists):
       """
       :type lists: List[ListNode]
       :rtype: ListNode
       """

       min_heap = []

       # 将每个链表的头节点加入优先队列
       for node in lists:
           if node:
               heapq.heappush(min_heap, (node.val, node))

       dummy = ListNode()
       curr = dummy

       # 弹出最小的节点，并将其加入到结果链表中
       while min_heap:
           _, node = heapq.heappop(min_heap)
           curr.next = node
           curr = curr.next
           if node.next:
               heapq.heappush(min_heap, (node.next.val, node.next))

       return dummy.next


if __name__ == "__main__":
    """
    因为都是有序链表,因此在合并成为新的有序链表的时候,
    每次只比较链表第一个值,当选择了一个链表的一个值之后,这个链表就向后移动一个节点(记录的首节点变成了next的节点)
    重复进行多链表的首点比较
    """

    # 创建示例链表数组
    lists = []
    lists.append(ListNode(1, ListNode(4, ListNode(5))))
    lists.append(ListNode(1, ListNode(3, ListNode(4))))
    lists.append(ListNode(2, ListNode(6)))

    # 合并链表
    merged_list = Solution().mergeKLists(lists)

    # 输出合并后的链表值
    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
