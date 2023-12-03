## 数组、字符串

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

（3）https://leetcode.cn/problems/product-of-array-except-self/submissions/?envType=study-plan-v2&envId=leetcode-75

```python
# 正反向遍历与累计思想
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 使用正反遍历，然后累乘
        # 每一次都只乘以自己之前的累积的乘积

        # 正向遍历
        mul = 1
        ans = []
        length = len(nums)
        for i in range(length):
            ans.append(mul)
            mul = mul * nums[i]
        
        mul_reverse = 1
        for i in range(length):
            ans[length-1-i] = ans[length-1-i]*mul_reverse
            mul_reverse = mul_reverse * nums[length-1-i]
        
        return ans
```

(4) https://leetcode.cn/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 第一轮遍历，记录元音字符和位置，list
        # 第二次遍历做修改

        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowel_list = []
        posi_list = []

        s_list = list(s)
        length = len(s_list)

        for i in range(length):
            if s_list[i] in vowels:
                vowel_list.append(s_list[i])
                posi_list.append(i)
        
        p_revise = 0
        len_list = len(posi_list)

        if len_list == 0:
            return s

        for i in range(length):
            if p_revise < len_list and i == posi_list[p_revise]:
                s_list[i] = vowel_list[len_list-1-p_revise]
                p_revise += 1
        return ''.join(s_list)
```

(5) https://leetcode.cn/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

```python
# 字符串反转
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = []
        length = len(s)

        i = 0
        while i < length:
            if s[i] != ' ':
                word_cur = []
                while i < length and s[i] != ' ':
                    word_cur.append(s[i])
                    i += 1
                word_list.append(''.join(word_cur))
            else:
                i += 1
        
        word_list.reverse()
        return ' '.join(word_list)
```

(6) https://leetcode.cn/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 检查领域然后尽可能多的插花
        
        length = len(flowerbed)
        plant_flag = False
        zero_num = 0

        if n == 0:
            return True

        if length == 0:
            if n == 0:
                return True
            else:
                return False

        if length == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
                else:
                    return False
            else:
                if n == 0:
                    return True
                else:
                    return False

        if length == 2:
            if flowerbed == [0,0]:
                if n <= 1:
                    return True
                else:
                    return False
            else:
                if n == 0:
                    return True
                else:
                    return False


        # 把 1 左右两边的 0 都给去掉
        for i in range(length):
            if flowerbed[i] == 0:
                if i > 0 and i < length-1:
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        n = n - 1
                        flowerbed[i] = 1
                if i == 0:
                    if flowerbed[i+1] != 1:
                        n = n - 1
                        flowerbed[i] = 1
                if i == length - 1:
                    if flowerbed[i-1] != 1:
                        n = n - 1
                        flowerbed[i] = 1
                if n == 0:
                    return True
        return False
```