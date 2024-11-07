## Meta Tag Leetcode

字符串的分类处理

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

（2）https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

```py
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 先遍历链表获得长度，得到待删除节点的序号
        length = 0
        p = head

        while p:
            length += 1
            p = p.next
        
        if length == 1 or length == 0:
            # print('0 or 1')
            return

        p_cur = head
        p_pre = head

        # print(head)

        index = 0
        while p_cur:
            if index == length // 2:
                # print(head)
                p_pre.next = p_cur.next
                return head
            else:
                # 得形成 p_pre 和 p_cur
                p_pre = p_cur
                p_cur = p_cur.next
                index += 1
```

(3) https://leetcode.cn/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75

```py
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head_odd = ListNode()
        # head_even = ListNode()

        index = 1
        p_cur = head

        # p_pre 要奇数偶数分开存

        # 循环操作完之后让奇链表的尾巴指向偶链表的表头
        while p_cur:
            if index == 1:
                head_odd = p_cur
                p_pre_odd = p_cur
                p_cur = p_cur.next
                index += 1
            elif index == 2:
                head_even = p_cur
                p_pre_even = p_cur
                p_cur = p_cur.next
                index += 1
            elif index % 2 == 1:
                p_pre_odd.next = p_cur
                p_pre_odd = p_cur
                p_cur = p_cur.next
                index += 1
            elif index % 2 == 0:
                p_pre_even.next = p_cur
                p_pre_even = p_cur
                p_cur = p_cur.next
                index += 1
        
        if index <= 2:
            return head
        else:
            p_pre_odd.next = head_even
            p_pre_even.next = None
            return head_odd
```