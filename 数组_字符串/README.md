## 字符串

### 笔记

（1） 字符串经常遇到的问题 u'l' 转 'l'


#### 例题
（1）https://leetcode.cn/problems/greatest-common-divisor-of-strings/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
# 穷举法
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        max_str = ''

        # gcd = math.gcd(len1,len2) #笑死，不让调包

        # 最大公因子一定是某个长度的前缀
        # 对约数遍历，拼接枚举即可，调用 math.gcd

        for i in range(min(len1,len2),0,-1):
            if len1 % i == 0 and len2 % i == 0:
                if str1[:i] == str2[:i]:
                    if str1[:i] * (len1 / i) == str1 and str2[:i] * (len2 / i) == str2:
                        max_str = str1[:i]
                        return max_str
        return max_str
```

（2）https://leetcode.cn/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 0 or length == 1 or length == 2:
            return False
        # 双向遍历，维护两个数组，找到递推关系
        # nums[i+1]<left_min[i] -> 
        left_min = []
        # right_max 得反过来构造
        right_max = []
        flag = False

        for i in range(1, length):
            if i == 1:
                left_min.append(nums[0])
                right_max.append(nums[length-1])
            else:
                # 更新 left_min, left_min[0] 记录的是 1 左边的最小的数
                if nums[i-1] < left_min[i-2]:
                    left_min.append(nums[i-1])
                else:
                    left_min.append(left_min[i-2])
                
                # 更新 right_max
                if nums[length-i] > right_max[i-2]:
                    right_max.append(nums[length-i])
                else:
                    right_max.append(right_max[i-2])
        right_max.reverse()

        for i in range(1,length-1):
            if left_min[i] < nums[i] and nums[i] < right_max[i]:
                flag = True
        
        return flag
        
```