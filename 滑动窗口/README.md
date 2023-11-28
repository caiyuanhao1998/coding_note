## 滑动窗口

要关注到每一次滑动时发生变化的部分，然后用代码来刻画它


### 例题：
（1）https://leetcode.cn/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

```
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        for i in range(len(nums)-k+1):
            if i == 0:
                sum_max = sum(nums[:k])
                sum_pre = sum_max
            else:
                sum_cur = sum_pre - nums[i-1] + nums[i+k-1]
                if sum_cur > sum_max:
                    sum_max = sum_cur
                sum_pre = sum_cur
        
        mean_max = sum_max / float(k)

        return mean_max
```