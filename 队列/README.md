## 队列

### 队列数据结构的特点就是先进先出

#### 例题
（1）https://leetcode.cn/problems/number-of-recent-calls/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class RecentCounter(object):

    def __init__(self):
        self.request = []


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # 维护一个长度为3000的队列
        self.request.append(t)
        while t - self.request[0] > 3000:
            self.request.pop(0)
        return len(self.request)
```

