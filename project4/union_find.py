"""
4.实现图论中，Union-Find算法
"""


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


# 示例用法
if __name__ == "__main__":
    """
    PS: 没用过这个, 百度查出来copy的
    """

    n = 5
    uf = UnionFind(n)

    # 合并节点
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    # 查找根节点
    print(uf.find(0))  # 输出 1
    print(uf.find(2))  # 输出 1
    print(uf.find(3))  # 输出 3

    # 检查节点是否属于同一个集合
    print(uf.find(0) == uf.find(2))  # 输出 True
    print(uf.find(1) == uf.find(3))  # 输出 False
