## 动态规划

动态规划里面有一个很重要的思想，叫做维护到目前为止最小，最大的代价

#### 例题
（1）https://leetcode.cn/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75

```shell
# 一种空间换时间的迭代方法
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        list_tribonacci = []
        for i in range(n):
            if i == 0 or i == 1:
                list_tribonacci.append(i)
            elif i == 2:
                list_tribonacci.append(1)
            else:
                list_tribonacci.append((list_tribonacci[i-1]+list_tribonacci[i-2]+list_tribonacci[i-3]))
        return list_tribonacci[n-1]+list_tribonacci[n-2]+list_tribonacci[n-3]
```

(2) https://leetcode.cn/problems/min-cost-climbing-stairs/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 可以视为0阶段的cost是0，选择走一步或者两步
        # 每一步选择走最小，如果两者相等就走最远的
        # 维护一个表，走到目前所需的最小代价
        min_cost = []
        for i in range(len(cost)+1):
            if i == 0 or i == 1:
                min_cost.append(0)
            else:
                min_cost.append(min(min_cost[i-2]+cost[i-2],min_cost[i-1]+cost[i-1]))
        
        return min_cost[len(cost)]
```

(3) https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75

```shell
# 有时可能需要从过去的两步里面去去找状态转移，妙用 max，min 等函数

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 由前两步递推到下一步，不需要维护偷盗标记
        # max_benefit[i] 表示前 i 个房子最多可以偷到多少钱，不包括第i个房子
        max_benefit = []

        for i in range(len(nums)+1):
            if i == 0:
                max_benefit.append(0)
            elif i == 1:
                max_benefit.append(nums[0])
            else:
                max_benefit.append(max(nums[i-1]+max_benefit[i-2], max_benefit[i-1]))
        return max_benefit[len(nums)]
```