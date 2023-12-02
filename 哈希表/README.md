## 哈希表（Hash Table）

哈希表（Hash Table），又称散列表，是一种常用的数据结构，它提供了快速的数据插入和查找操作。哈希表的核心是哈希函数和数组，它通过哈希函数将键（Key）映射到数组的一个位置（一个索引），并在这个位置存储对应的值（Value）。

### 哈希表的工作原理：

1. **哈希函数**：哈希表使用哈希函数将键转换为数组的索引。好的哈希函数能够均匀地分布键，减少冲突（两个不同的键映射到同一位置）。

2. **键-值对存储**：在哈希表中，数据以键-值对的形式存储。每个键都是独一无二的，哈希函数根据键计算出数组的索引，并在该位置存储值。

3. **处理冲突**：当两个不同的键通过哈希函数映射到相同的索引时，会发生冲突。常见的解决冲突的方法有链地址法（在冲突的位置存储一个链表）和开放地址法（找到一个空的位置进行存储）。

### 哈希表的特点：

- **高效的查找、插入和删除**：在理想情况下，哈希表的这些操作的时间复杂度可以达到 O(1)。

- **无序**：哈希表中的数据是无序的，不能保证数据的顺序。

- **动态扩容**：当哈希表中的数据增多，为了保持操作的高效性，哈希表可能需要进行扩容，这涉及到重新计算现有所有键的哈希值，并将它们放入新的更大的表中。

### 应用：

哈希表在计算机科学中应用广泛，比如实现关联数组（如 Python 中的字典和 JavaScript 中的对象）、数据库索引、缓存等。

在不同的编程语言中，哈希表可能有不同的实现，例如 Python 的字典（dict）、Java 的 HashMap 和 JavaScript 的对象。

&nbsp;

---

## Python 的 `dict` 与哈希表的区别

在 Python 中，字典（`dict`）实际上是使用哈希表实现的。所以，从实现的角度来看，Python 的 `dict` 类型是一种哈希表。但是，有一些细节和特性使得 Python 的 `dict` 在使用上和一般的哈希表有所不同：

1. **内置实现**：
   - Python 的 `dict` 是语言核心的一部分，提供了内置的支持和优化。而一般的哈希表可能是以库的形式提供，或者需要程序员手动实现。

2. **功能丰富**：
   - Python 的 `dict` 提供了许多便利的特性，如动态扩展、能够直接使用对象作为键（只要它们是可哈希的）等。

3. **保序性**：
   - 从 Python 3.7 开始，`dict` 保持了插入顺序，即遍历字典时可以按照元素添加的顺序进行。这是哈希表通常不具备的特性（哈希表通常是无序的）。

4. **优化的冲突解决机制**：
   - Python 的 `dict` 在实现上做了很多优化来处理哈希冲突，从而保持了高效的查找、插入和删除操作。

因此，尽管从概念上讲 Python 的 `dict` 是一种哈希表，但它通过语言层面的

&nbsp;

---

## 例题

（1）https://leetcode.cn/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

计算速度很慢
```shell
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        ans_1 = []
        ans_2 = []
        
        if len_1 > len_2:
            for i in range(len_2):
                if nums1[i] not in ans_1 and nums1[i] not in nums2:
                    ans_1.append(nums1[i])
                if nums2[i] not in ans_2 and nums2[i] not in nums1:
                    ans_2.append(nums2[i])
            for j in range(len_2,len_1):
                if nums1[j] not in ans_1 and nums1[j] not in nums2:
                    ans_1.append(nums1[j])
        else:
            for i in range(len_1):
                if nums1[i] not in ans_1 and nums1[i] not in nums2:
                    ans_1.append(nums1[i])
                if nums2[i] not in ans_2 and nums2[i] not in nums1:
                    ans_2.append(nums2[i])
            for j in range(len_1,len_2):
                if nums2[j] not in ans_2 and nums2[j] not in nums1:
                    ans_2.append(nums2[j])
        return [ans_1,ans_2]
```

（2）https://leetcode.cn/problems/max-number-of-k-sum-pairs/submissions/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        num_dic = {}
        # 用哈希表来解 - 字典
        # 键值对 数值，它出现的次数
        
        # 第一次遍历，构造哈希表，基本操作
        for num in nums:
            num_dic[num] = num_dic.get(num,0) + 1
        
        # 第二次遍历，配对
        for num in nums:
            if k - num in num_dic:
                if k-num == num and num_dic[num] > 1:
                    count += 1
                    num_dic[num] -= 2
                if k-num != num and num_dic[num]>0 and num_dic[k-num]>0:
                    count += 1
                    num_dic[num] -= 1
                    num_dic[k-num] -= 1

        return count
```

（3）https://leetcode.cn/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

```shell
# 双重字典嵌套
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_dic = {}
        flag = True

        for num in arr:
            arr_dic[num] = arr_dic.get(num,0) + 1
        
        # 对出现次数做一个dict计数
        value_dic = {}
        for value in arr_dic.values():
            value_dic[value] = value_dic.get(value,0) + 1
        
        for key in value_dic:
            if value_dic[key] > 1:
                flag = False
        return flag
```

（4）https://leetcode.cn/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

```shell
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # 规则：总的类别一样，出现的次数得一样
        # 对每个字符出现的次数建字典
        dic_word1 = {}
        dic_word2 = {}
        close_flag = False

        for i in range(len(word1)):
            dic_word1[word1[i]] = dic_word1.get(word1[i],0) + 1

        for i in range(len(word2)):
            dic_word2[word2[i]] = dic_word2.get(word2[i],0) + 1
        
        # 比较两个dic的keys是否完全相等
        if set(dic_word1.keys()) == set(dic_word2.keys()):
            dic_word1_num = {}
            dic_word2_num = {}

            for key in dic_word1:
                dic_word1_num[dic_word1[key]] = dic_word1_num.get(dic_word1[key],0) + 1
            for key in dic_word2:
                dic_word2_num[dic_word2[key]] = dic_word2_num.get(dic_word2[key],0) + 1
            
            if dic_word1_num == dic_word2_num:
                close_flag =True
        return close_flag
```