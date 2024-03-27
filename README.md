# 面试题

- 实现的编程语言不限
- 实现的方式不限
- 可选做

[工程算法](#工程算法)
- [二叉树](#1-实现二叉树并回答以下问题)
- [合并链表](#2-合并k个生序链表)
- [LRU缓存](#3-lru-缓存)
- [图论 Union-Find](#4-实现图论中union-find算法)
- [并发处理实现](#并发处理实现)

[机器学习算法](#机器学习算法)
- [神经网络](#1-神经网络实现)
- [Transformer模型](#2-transformer-模型)





## 工程算法


### 1. 实现二叉树，并回答以下问题
- 二叉树的前、中、后序遍历是什么，仅仅是三个顺序不同的列表吗？
- 请分析后续遍历有什么特殊之处？


### 2. 合并k个生序链表

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] 按 升序 排列
- lists[i].length 的总和不超过 10^4

```python
class Solution(object):
   def mergeKLists(self, lists):
       """
       :type lists: List[ListNode]
       :rtype: ListNode
       """
```

### 3. LRU 缓存

请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：

- LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
- int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
- void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
- LRUCache lRUCache = new LRUCache(2);
- lRUCache.put(1, 1); // 缓存是 {1=1}
- lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
- lRUCache.get(1);    // 返回 1
- lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
- lRUCache.get(2);    // 返回 -1 (未找到)
- lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
- lRUCache.get(1);    // 返回 -1 (未找到)
- lRUCache.get(3);    // 返回 3
- lRUCache.get(4);    // 返回 4

提示：

- 1 <= capacity <= 3000
- 0 <= key <= 10000
- 0 <= value <= 105
- 最多调用 2 * 105 次 get 和 put

```python
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### 4. 实现图论中，Union-Find算法

### 5. 并发处理实现
假设你负责开发一个Web服务的后端，该服务需要处理来自客户端的大量请求。每个请求将执行以下操作之一：

数据检索：从某个API获取数据，这个操作可能需要一些时间来完成。
数据处理：对检索到的数据进行一些计算密集型的处理。
日志记录：将处理结果记录到日志文件中。
由于请求量很大，你需要利用Python的多并发特性来优化这三个操作的执行，以提高系统的吞吐量和响应能力。

任务要求
设计一个多并发解决方案：根据上述操作的特点，使用Python编写一个多并发的解决方案。你可以选择使用线程（threading）、进程（multiprocessing）或异步（asyncio）中的一种或几种方法来实现。

解决方案说明：解释你的设计选择。你为何选择特定的并发模型？考虑到操作的特性（如CPU密集型、IO密集型等），这种选择有何优势？

异常处理：展示在你的解决方案中如何处理可能出现的异常情况，例如API请求失败、数据处理错误等。

性能考虑：讨论你的解决方案可能面临的性能瓶颈以及可能的优化方法。



## 机器学习算法
### 1. 神经网络实现
通常，神经网络以“线性变换->激活函数->线性变换->激活函数->线性变化...”的形式进行一系列的变换。
- 一个2层的神经网络如何实现？ 
- 随着层数的增加，参数的管理会变得复杂。请创建一个简化参数管理机制。

```python
# 数据集

# 1. 权重的初始化

# 2. 神经网络的推理
def predict(x):
    pass

# 3. 神经网络的训练 
```

### 2. Transformer 模型
- Transformer模型是如何组成的？
- 你觉得Transformer最难是哪一部分，为什么？
- 实现简易的Transformer

