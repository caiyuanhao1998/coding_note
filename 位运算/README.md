## 位运算

要注意二进制进位与退位的关系，注意区分奇偶规律

#### 例题
（1）https://leetcode.cn/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75

```shell
# 思路1
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans_list = []
        # python模拟二进制的运算
        for i in range(n+1):
            ans_list.append(bin(i).count('1'))
        return ans_list


# 思路2
# 奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1
# 偶数中 1 的个数一定和除以 2 之后的那个数一样多
# 建一个表来存放已有的结果
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans_list = []
        # python模拟二进制的运算
        for i in range(n+1):
            if i == 0 or i == 1:
                ans_list.append(i)
            elif i % 2 == 1:
                ans_list.append(ans_list[i-1]+1)
            else:
                ans_list.append(ans_list[i//2])
        return ans_list
```


