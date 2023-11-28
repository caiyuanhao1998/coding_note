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