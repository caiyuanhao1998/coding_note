## 链表

单链表的数据结构

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

（1）链表翻转 —— 画图，记得头结点要指向 None，不然会死锁

```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p_cur = head
        p_pre = None
        while p_cur:
            p_temp = p_cur.next
            p_cur.next = p_pre
            p_pre = p_cur
            p_cur = p_temp
                
        return p_pre
```