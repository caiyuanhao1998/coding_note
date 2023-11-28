# 力扣刷题笔记

## 1. leecode-75

https://leetcode.cn/studyplan/leetcode-75/

&nbsp;

### 1.1 字符串（str）
（1）len( ) 返回字符串长度

&nbsp;

### 1.2 列表（list）
（1）list转换为set会自动删去重复的元素，如果还需要进一步保留原来的顺序的话：

```shell
my_list = [1, 2, 2, 3, 4, 4, 4, 5]

# or 前为True的话就不执行 or 后边的部分，set 类型 add 后返回 None，bool 语句中就是 False
seen = set()
unique_elements = [x for x in my_list if not (x in seen or seen.add(x))]

print(unique_elements)
```

把 list 转成 set 是一个非常重要的处理技巧，常常用于处理掉重复元素


（2）采用collections中的counter包，可以把一个字符串转换为字典，里面是不重复元素与其出现的次数

（3）用list.count(a)函数可以统计a在list中出现的次数

（4）列表合并，直接用 `+`

```shell
list_1 + list_2
```

（5）List 删除元素的两个函数：

```shell
# 按照值来删除
my_list.remove('apple') 会从列表 my_list 中删除第一个出现的 apple

# 按照索引来删除
my_list.pop(1) 会删除列表 my_list 中索引为 1 的元素
```

(6) 判断一个元素是否在一个列表中用 `in`

(7) 将字典转成元组, tuple(list), 但如果是双重 list 转成 tuple 的话：

```shell
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 将字典转成元组作为key，构造哈希表，因为list本身是可变的，无法作为key
        # 行字典
        n = len(grid[0])
        rows = [tuple(grid[r][:]) for r in range(n)]
        cols = [tuple(grid[r][c] for r in range(n)) for c in range(n)]

        count = 0

        for i in range(n):
            for j in range(n): 
                if rows[i] == cols[j]:
                    count += 1

        return count
```

&nbsp;

### 1.3 数组（array）
（1）十进制拆分的基本思路是将其先转换成字符串（str），然后拆成单个字母后再转成int：

```shell
number = 123
digits = [int(digit) for digit in str(number)]
```

（2）python本身没有库函数可以求平均数，只有sum()和len()函数。numpy包有。注意在用 sum() / len() 时要强行 float() 变成浮点数。

&nbsp;

### 1.4 类（class）
（1）采用 hasstr() 函数，判定某个属性是否属于这个类

```shell

class MyClass:
    def __init__(self):
        self.my_attr = 42

obj = MyClass()
print(hasattr(obj, 'my_attr'))  # 输出：True
print(hasattr(obj, 'another_attr'))  # 输出：False

```

（2）采用 getstr() 函数，获取类里面某个属性的值

```shell
class MyClass:
    def __init__(self):
        self.my_attr = 42

obj = MyClass()
try:
    value = getattr(obj, 'my_attr')
    print('Attribute exists')
except AttributeError:
    print('Attribute does not exist')
```

&nbsp;

### 1.5 字典（dictionary）
字典的值，用 .values() 方法返回，可以用这种方式检车某个值是否在字典中。

```shell
my_dict = {'a': 1, 'b': 2, 'c': 3}
value_to_check = 2

# 检查值是否存在
if value_to_check in my_dict.values():
    print("值存在于字典中")
else:
    print("值不在字典中")

```

字典的特性在于，能够快速地根据 Key 找到 Value。反过来不行，除非将字典反转：

```shell
def reverse_dict(original_dict):
    return {value: key for key, value in original_dict.items()}

# 示例
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dict(my_dict)

value_to_check = 2
if value_to_check in reversed_dict:
    print(f"值 {value_to_check} 对应的键是 {reversed_dict[value_to_check]}")
else:
    print(f"字典中不存在值为 {value_to_check} 的键")

```

在 Python 中，字典的键（key）可以是任何不可变（immutable）类型。这主要包括以下几种类型：

1. **字符串（String）**：这是使用最广泛的键类型。
   
   示例：`my_dict = {"name": "Alice", "age": 25}`

2. **数字（Number）**：整数和浮点数都可以作为键。
   
   示例：`my_dict = {1: "apple", 2: "banana"}`

3. **元组（Tuple）**：元组是不可变的，因此它们可以作为键。但元组中的元素也必须是不可变的。
   
   示例：`my_dict = {(1, 2): "coordinates", (3, 4): "points"}`

4. **布尔值（Boolean）**：`True` 和 `False` 也可以作为键。
   
   示例：`my_dict = {True: "yes", False: "no"}`

5. **冻结集合（Frozen Set）**：冻结集合是不可变的，因此可以作为键，尽管这种用法不太常见。
   
   示例：`my_dict = {frozenset([1, 2, 3]): "numbers"}`

### 不能作为键的类型：

- **列表（List）**：列表是可变的，因此不能作为字典的键。
- **集合（Set）**：集合也是可变的，不能作为键。
- **字典（Dictionary）**：字典本身是可变的，所以不能作为键。


### 字典的遍历
（1）遍历所有的键:

```shell
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key)
```

（2）遍历所有的值:

```shell
for value in my_dict.values():
    print(value)
```

（3）遍历所有的键值对:

```shell
for key, value in my_dict.items():
    print(key, value)
```