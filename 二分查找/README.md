# 二分查找

二分查找是一种在 **有序数组** 中查找特定元素的算法。其基本思想是比较数组中间的元素和目标值，根据比较结果缩小搜索范围，直到找到目标值或确定目标值不存在。

## 算法步骤

1. **初始化**：设定两个指针，分别指向数组的起始位置和结束位置。

2. **循环搜索**：在起始位置不大于结束位置的情况下，执行以下步骤：
   - 找到数组中间的位置。
   - 比较中间元素与目标值：
     - 如果中间元素等于目标值，返回该元素的位置。
     - 如果中间元素大于目标值，移动结束位置指针到中间位置的左侧。
     - 如果中间元素小于目标值，移动起始位置指针到中间位置的右侧。

3. **返回结果**：如果找到目标值，返回其位置；否则返回指示未找到的值（通常为 `-1` 或 `None`）。

## Python 实现

```shell
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 示例
arr = [1, 3, 5, 7, 9]
target = 5
print(binary_search(arr, target))  # 输出: 2
```


## 例题
（1） https://leetcode.cn/problems/guess-number-higher-or-lower/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        left = 1
        right = n
        # 此题并不适用迭代
        while left < right:
            if guess((left+right)//2) == 1:
                left = (left+right)//2 + 1
            if guess((left+right)//2) == -1:
                right = (left+right)//2
            if guess((left+right)//2) == 0:
                return (left+right)//2
```

（2）https://leetcode.cn/problems/find-peak-element/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        if nums[0] > nums[1]:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            # stx()
            mid = left + (right - left) // 2
            if mid == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            if nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]:
                # print('1')
                # stx()
                # 1 - 峰值在右边
                left = mid + 1
            if nums[mid-1]>nums[mid] and nums[mid]>nums[mid+1]:
                # print('2')
                # stx()
                # 2 - 峰值在左边
                right = mid - 1
            if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                # print('3')
                # stx()
                # 3 - 峰值左右皆可
                left = mid + 1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                # print('4')
                # stx()
                # 4 - 直接出峰值
                return mid
        
        return (left+right)//2
```