# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = []

        if k == 0:
            return [target]

        def helper(node, route, target, result, depth=0):
            if node == None:
                return
            # if depth meets level k down from target
            if depth == k:
                result.append(node)
                return
            # recursively search target
            next_route = route.copy()
            next_route.append(node)
            if node == target:
                for i, node in enumerate(route[::-1]):
                    if i == k:
                        result.append(node)
                        break
                helper(node.left, next_route, target, result, depth=depth + 1)
                helper(node.right, next_route, target, result, depth=depth + 1)
            else:
                helper(node.left, next_route, target, result)
                helper(node.right, next_route, target, result)

        helper(root, [], target, answer)

        return answer