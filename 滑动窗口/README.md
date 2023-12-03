## 滑动窗口

要关注到每一次滑动时发生变化的部分，然后用代码来刻画它

滑动窗口算法通常与双指针技巧紧密相关。在这种方法中，两个指针（通常称为 `left` 和 `right`）代表窗口的两端。这些指针在数组或列表上移动，以捕捉或排除特定的元素，从而解决各种问题，如寻找最长子串、最小子数组长度等。滑动窗口与双指针技巧的主要关联点如下：

1. **窗口定义**：`left` 和 `right` 指针定义了窗口的边界。窗口内包含了当前考虑的元素集合。

2. **移动规则**：`right` 指针通常用于扩展窗口（即包含更多的元素），而 `left` 指针用于缩小窗口（即排除一些元素）。这种移动规则取决于问题的特定要求。

3. **条件判断**：在窗口移动的过程中，根据特定的条件（如和、最大值、包含特定元素等），来决定是否需要移动 `left` 或 `right` 指针，或者两者同时移动。

4. **灵活性**：滑动窗口和双指针技巧提供了一种灵活的方式来处理数组和字符串问题，允许以线性时间复杂度解决许多看似复杂的问题。

综上所述，滑动窗口是一种利用双指针来动态调整窗口大小的技巧，用以解决一系列的算法问题。


### 例题：
（1）https://leetcode.cn/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

```shell
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

(2) https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Maintain a sliding window where there is at most one zero on it.
        # 双指针遍历
        p_left = 0
        p_right = 0
        maxlength = 0
        curlength = 1
        zero_num = 0

        while p_right < len(nums):
            if nums[p_right] == 1:
                if curlength > maxlength:
                    maxlength = curlength
                p_right += 1
                curlength += 1
                continue
            else:
                zero_num += 1
                if zero_num == 1 and curlength > maxlength:
                    maxlength = curlength
                while p_left < p_right and zero_num > 1:
                    if nums[p_left] == 1:
                        p_left += 1
                        curlength -= 1
                        continue
                    else:
                        zero_num -= 1
                        p_left += 1
                        curlength -= 1
                        continue
                p_right += 1
                curlength += 1
        return max(maxlength-1, 0)
```

(3) https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

```py
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel_letters = ['a','e','i','o','u']
        length = len(s)
        vowel_num = 0
        max_vowel_num = 0
        for i in range(length-k+1):
            if i == 0:
                for j in range(k):
                    if s[j] in vowel_letters:
                        vowel_num += 1
            else:
                if s[i-1] in vowel_letters:
                    vowel_num -= 1
                if s[i+k-1] in vowel_letters:
                    vowel_num += 1
            if vowel_num == k:
                return k
            if vowel_num > max_vowel_num:
                max_vowel_num = vowel_num
        return max_vowel_num
```