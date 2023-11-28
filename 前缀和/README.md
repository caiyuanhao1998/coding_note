在 Python 编程中，"前缀和"是一种常见的技术，主要用于处理数组或列表中的区间求和问题。前缀和的核心思想是提前计算并存储数组中每个位置之前所有元素的和，从而使得任意区间的和可以快速计算。

### 前缀和的原理：

假设有数组 `arr = [a1, a2, a3, ..., an]`，其前缀和数组 `prefixSum` 定义如下：

- `prefixSum[0] = 0`（通常为了方便计算，前缀和数组的第一个元素设置为 0）
- `prefixSum[i] = a1 + a2 + ... + ai` （对于 `i > 0`）

这意味着 `prefixSum[i]` 存储了数组 `arr` 从第一个元素到第 `i` 个元素的总和。

### 使用前缀和的优势：

- **快速计算区间和**：如果要计算 `arr` 中从 `i` 到 `j` 的元素之和，可以简单地用 `prefixSum[j] - prefixSum[i-1]` 计算出来（这里假设 `i > 0`）。
- **降低时间复杂度**：对于多次区间求和的操作，使用前缀和可以将每次求和的时间复杂度从 O(N) 降低到 O(1)。

### Python 实现示例

```
def calculatePrefixSum(arr):
    prefixSum = [0]
    for num in arr:
        prefixSum.append(prefixSum[-1] + num)
    return prefixSum

# 示例数组
arr = [3, 1, 2, 5, 4]

# 计算前缀和
prefixSum = calculatePrefixSum(arr)

# 计算区间 [2, 4]（即索引 1 到 3）的和
intervalSum = prefixSum[4] - prefixSum[1]
print(intervalSum)  # 输出：8 (1 + 2 + 5)
```

### 例题
https://leetcode.cn/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

```
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # 前缀和思想，设置一个新的list，记录走动目前点的海拔
        highest = 0
        height = [0]
        for i in range(len(gain)):
            height_cur = height[i] + gain[i]
            height.append(height_cur)
            if height_cur > highest:
                highest = height_cur
        return highest
```