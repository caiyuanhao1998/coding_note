## 二叉树

### 二叉树的数据结构
二叉树一般包含一个 `value`，一个左节点 `left`，和一个右节点 `right`

```shell
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### 例题
（1）https://leetcode.cn/problems/maximum-depth-of-binary-tree/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
# 递归思想
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # 可以直接 is None 的
        if not hasattr(root, 'left') and not hasattr(root, 'right'):
            return 1
        if not hasattr(root, 'left') and hasattr(root, 'right'):
            return self.maxDepth(root=self.right) + 1
        if hasattr(root, 'left') and not hasattr(root, 'right'):
            return self.maxDepth(root=self.left) + 1
        if hasattr(root, 'left') and hasattr(root, 'right'):
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 更加简洁的写法
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归基础情况：空节点的深度为0
        if root is None:
            return 0
        
        # 递归计算左右子树的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 返回最大深度加1（当前节点的深度）
        return max(left_depth, right_depth) + 1
```
