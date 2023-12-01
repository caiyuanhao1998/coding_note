## 栈

栈的最大特点就是“先进先出”，牢记。用栈的题目通常都会带有“消消乐”的特点

一般是用list来实现这个功能

```shell
my_list.append()
my_list.pop()
```

list和字符串之间的互相转换：

```shell
# list 转字符串
my_str = ''.join(my_list)

# 字符串转list
my_list = list(my_str)
```


#### 例题
（1）https://leetcode.cn/problems/removing-stars-from-a-string/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_no_star = []

        # 遇到 * 就弹出，没遇到就压入
        for i in range(len(s)):
            if s[i] != '*':
                s_no_star.append(s[i])
            else:
                s_no_star.pop()
        return ''.join(s_no_star)
```

(2) https://leetcode.cn/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        asteroid_state = []
        for i in range(len(asteroids)):
            if len(asteroid_state) == 0:
                asteroid_state.append(asteroids[i])
            else:
                # 异号就会发生碰撞
                if asteroids[i] * asteroid_state[-1] > 0 or (asteroid_state[-1] < 0 and asteroids[i]>0):
                    asteroid_state.append(asteroids[i])
                else:
                    # stx()
                    out_explode = False
                    while len(asteroid_state) > 0 and (asteroid_state[-1] > 0 and asteroids[i] < 0):
                        # stx()
                        if abs(asteroids[i]) > abs(asteroid_state[-1]):
                            # stx()
                            asteroid_state.pop()
                        elif abs(asteroids[i]) == abs(asteroid_state[-1]):
                            # stx()
                            asteroid_state.pop()
                            out_explode = True
                            break
                        else:
                            # stx()
                            out_explode = True
                            break
                    if not out_explode:
                        asteroid_state.append(asteroids[i])
        return asteroid_state
```