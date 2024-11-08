## 双指针技术

双指针技术是一种常用的算法策略，在解决特定类型的编程问题时非常有效。它涉及同时使用两个指针（或索引），通常在一个数组或链表中，来实现某种形式的遍历或搜索。一般做的是原地改变，in-place 操作。

### 双指针技术的类型：

1. **读写指针**：
   - 读指针遍历，写指针记录。

2. **快慢指针**：
   - 两个指针以不同的速度移动，通常用于检测循环、寻找中点或解决有关链表的问题。

3. **左右指针**：
   - 两个指针分别从数组的左端和右端开始，向中间移动，经常用于排序、搜索或处理两端数据的问题。

### 使用场景和例子：

1. **数组和链表问题**：
   - 寻找或删除数组/链表中的特定元素。
   - 示例：移除排序数组中的重复项、链表的循环检测。

2. **双指针碰撞**：
   - 主要用于有序数组或链表，通过左右指针向中间移动来找到目标值。
   - 示例：两数之和问题、三数之和问题。

3. **滑动窗口**：
   - 用于处理连续数据块的问题，比如寻找连续子数组的最大和。
   - 示例：最长无重复字符的子串、连续子数组的最大和。

4. **快慢指针**：
   - 用于解决环形链表、周期性问题。
   - 示例：链表中环的检测、寻找链表的中点。

### 为何使用双指针：

- **空间效率**：双指针通常不需要额外的空间，因此非常节省空间。
- **时间效率**：在很多情况下，双指针能减少不必要的迭代，提高算法的时间效率。

### 总结：

双指针技术是解决数组和链表问题的一种高效方法，尤其是在涉及到排序、搜索和滑动窗口问题时。它的优势在于减少了计算时间和空间复杂度，使算法更加高效。根据具体问题的性质，可以选择不同类型的双指针策略来实现最优解。


### 例题：
#### 快慢指针：
（1）https://leetcode.cn/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p_fast = 0
        p_slow = 0
        
        while p_fast < len(chars):
            # 因为题目中的chars是连续重复的，所以可以按顺序遍历
            # 快指针向前，合并计数
            char_cur = chars[p_fast]
            count_cur = 0
            while p_fast < len(chars) and chars[p_fast] == char_cur:
                p_fast = p_fast + 1
                count_cur = count_cur + 1
            
            # 慢指针向前，慢指针是chars的修改位置
            chars[p_slow] = char_cur
            p_slow = p_slow + 1

            # 把计数并入到chars当中
            if count_cur > 1:
                for k in str(count_cur):
                    chars[p_slow] = k
                    p_slow = p_slow + 1
        
        # 直接删除，切片
        chars = chars[:p_slow]

        return len(chars) 
```

(2) 要小心双重循环和 pop 操作，这些都非常费时间

```shell
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p_slow = 0
        p_fast = 1
        count = 0

        while p_slow < len(nums) - 1:
            p_fast = p_slow + 1
            while p_fast < len(nums):
                if nums[p_slow] + nums[p_fast] == k:
                    count += 1
                    nums.pop(p_fast)
                    nums.pop(p_slow)
                    # p_fast = p_fast - 1
                    # print(nums)
                    # print(p_slow)
                    # print(p_fast)
                    # print('-----')
                    # stx()
                    break
                elif p_fast == (len(nums) - 1):
                    # print('--end--')
                    p_fast += 1
                    p_slow += 1
                    # stx()
                else:
                    p_fast += 1
                    # stx()
        return count
```

(3) https://leetcode.cn/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p_t = 0
        p_s = 0
        if s == '':
            return True

        while p_t < len(t) and p_s < len(s):
            if t[p_t] == s[p_s]:
                    p_s += 1
            p_t += 1
        
        if p_s == len(s):
            return True
        else:
            return False
```


#### 左右指针：
#### 例题
（1）https://leetcode.cn/problems/max-number-of-k-sum-pairs/submissions/?envType=study-plan-v2&envId=leetcode-75

一般左右指针处理数组类问题会先做一个排序处理，可以直接 .sort() 排序，也可以快速排序：
快速排序实际上也是一种递归思路，每次选择第一个元素作为 pivot, 小的放左边，大的放右边

```shell
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 选择第一个元素作为基准
    left = [x for x in arr[1:] if x < pivot]  # 所有小于基准的元素
    right = [x for x in arr[1:] if x >= pivot]  # 所有大于等于基准的元素
    return quick_sort(left) + [pivot] + quick_sort(right)
```

本题的解

```shell
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 先排序再左右指针
        nums.sort()

        p_left = 0
        p_right = len(nums) - 1
        count = 0

        while p_left < p_right:
            sum_cur = nums[p_left] + nums[p_right]
            if sum_cur > k:
                p_right -= 1
            if sum_cur < k:
                p_left += 1
            if sum_cur == k:
                count += 1
                p_right -= 1
                p_left += 1

        return count
```

(2) https://leetcode.cn/problems/container-with-most-water/submissions/?envType=study-plan-v2&envId=leetcode-75

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 真正的左右指针
        length = len(height)
        p_left = 0
        p_right = length - 1
        max_area = 0
        # 向内移动规则是每次短板向内移动一格
        # area = (p_right - p_left) * min(height[p_left], height[p_right])
        while p_left < p_right:
            cur_area = (p_right - p_left) * min(height[p_left], height[p_right])
            if cur_area > max_area:
                max_area = cur_area
            if height[p_left] >= height[p_right]:
                p_right -= 1
            else:
                p_left += 1
        return max_area
```

