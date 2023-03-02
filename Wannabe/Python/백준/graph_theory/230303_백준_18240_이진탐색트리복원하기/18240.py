import sys 
from collections import defaultdict
si = sys.stdin.readline
N = int(si())
nums = [0]*N
order_num = 1
depth_dict = defaultdict(list)
depth_num = [0]*(N+1)
depths = list(map(int, si().split()))

def solution():
    root = Node(0)
    depth_dict[0].append(root)
    depth_num[0] += 1

    for i in range(N-1):
        depth = depths[i]
        depth_num[depth] += 1

        # 불가능
        if depth_num[depth] > depth_num[depth-1]*2:
            print(-1)
            return
        
        parent = (depth_num[depth]-1)//2
        p_node = depth_dict[depth-1][parent]

        node = Node(i+1)
        depth_dict[depth].append(node)

        if depth_num[depth]%2 == 1:
            p_node.left = node
        else:
            p_node.right = node

    inorder(root)
    print(*nums)
        
def inorder(root):
    global order_num
    if root == None:
        return
    inorder(root.left)
    nums[root.val] = order_num
    order_num += 1
    inorder(root.right)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

solution()