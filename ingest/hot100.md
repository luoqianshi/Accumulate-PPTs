# 📘 LeetCode Hot 100 渐进式扫盲手册（Python版）

> **适用对象**：准备互联网研发岗笔试的计算机专业研究生
> **使用方式**：按顺序学习，利用碎片时间反复背诵模板代码
> **核心原则**：先掌握套路，再理解原理，最后追求优雅

---

## 目录导航

| 阶段 | 知识模块 | 难度 | 核心能力 |
|------|---------|------|---------|
| 🟢 第一阶段 | 哈希、技巧、链表基础 | ⭐ | 基础数据结构 |
| 🟡 第二阶段 | 双指针、滑动窗口、栈 | ⭐⭐ | 线性结构操作 |
| 🟠 第三阶段 | 二叉树、二分查找、堆 | ⭐⭐⭐ | 树形结构+搜索 |
| 🔴 第四阶段 | 回溯、贪心、图论 | ⭐⭐⭐⭐ | 搜索策略 |
| 🟣 第五阶段 | 动态规划（一维→多维） | ⭐⭐⭐⭐⭐ | 状态设计能力 |

---

# 🟢 第一阶段：基础入门（⭐ 简单）

> **目标**：掌握哈希表、位运算技巧、链表基本操作
> **预计用时**：3-5天

---

## 一、哈希表（Hash Table）

### 核心知识

```python
# Python哈希表就是dict，O(1)查找
hash_map = {}
hash_map.get(k, None)   # 查找，不存在返回None
hash_map[k] = v          # 存入
k in hash_map            # 判断key是否存在
```

**哈希表的三大应用场景：**
1. **快速查找**：用空间换时间，将O(n²)降为O(n)
2. **频率统计**：Counter统计字符/数字出现次数
3. **分组归类**：将具有相同特征的元素归到一组

### 1.1 两数之和（#1 简单）

**思路**：遍历数组，用哈希表记录 `{值: 下标}`，查找 `target - 当前值` 是否已出现

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
```

> 💡 **一句话总结**：边遍历边查找，用哈希表把"查找另一半"变成O(1)

### 1.2 字母异位词分组（#49 中等）

**思路**：排序后的字符串作为哈希键，相同字符组成的单词归为一组

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        return list(groups.values())
```

> 💡 **一句话总结**：排序后相同的字符串 → 同一组，`defaultdict` 省去判空

### 1.3 最长连续序列（#128 中等）

**思路**：用集合存所有数，只从"序列起点"（前一个数不存在）开始向右扩展

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:          # num是序列起点
                cur = num
                while cur + 1 in s:       # 向右扩展
                    cur += 1
                longest = max(longest, cur - num + 1)
        return longest
```

> 💡 **一句话总结**：只从起点开始数，避免重复遍历，O(n)时间

---

## 二、位运算技巧

### 核心知识

```python
a ^ a = 0          # 相同异或为0
a ^ 0 = a          # 任何数与0异或为自身
a & (-a)           # 取最低位的1（lowbit）
a >> 1             # 右移一位（除以2）
```

### 2.1 只出现一次的数字（#136 简单）

**思路**：全部异或，成对的数异或为0，剩下的就是只出现一次的数

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
```

> 💡 **一句话总结**：异或消去成对元素，一行 `return reduce(xor, nums)` 也可

### 2.2 多数元素（#169 简单）

**思路**：Boyer-Moore投票法，候选人计数，不同则抵消

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            count += 1 if num == candidate else -1
            if count == 0:
                candidate, count = num, 1
        return candidate
```

> 💡 **一句话总结**：票数抵消，最后站着的就是多数

### 2.3 颜色分类（#75 中等）

**思路**：三指针法（荷兰国旗），0放左边，2放右边，1自然在中间

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1; mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1
```

> 💡 **一句话总结**：三指针一次遍历完成三色排序，O(n)时间O(1)空间

---

## 三、链表基础

### 核心知识

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 哑节点技巧：避免头节点特殊处理
dummy = ListNode(0, head)
```

**链表题万能思路**：
- 反转 → 三指针迭代
- 快慢指针 → 找中点/判环
- 哑节点 → 统一头节点处理

### 3.1 反转链表（#206 简单）

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
```

> 💡 **一句话总结**：三指针 `pre → cur → nxt`，逐个翻转指向

### 3.2 环形链表（#141 简单）

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
```

> 💡 **一句话总结**：快慢指针，有环必相遇

### 3.3 合并两个有序链表（#21 简单）

```python
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
```

> 💡 **一句话总结**：哑节点 + 逐个比较接入，剩余直接拼接

### 3.4 两数相加（#2 中等）

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, s = divmod(s, 10)
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

> 💡 **一句话总结**：逐位相加，`divmod` 同时处理进位和当前位

### 3.5 环形链表 II（#142 中等）

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                p = head
                while p != slow:
                    p, slow = p.next, slow.next
                return p
        return None
```

> 💡 **一句话总结**：快慢相遇后，一指针回头部，同步走，再遇即入环点

### 3.6 相交链表（#160 简单）

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```

> 💡 **一句话总结**：走完自己的路再走对方的路，相遇即交点（浪漫解法）

### 3.7 回文链表（#234 简单）

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # 反转后半部分
        pre, cur = None, slow.next
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        # 比较前后半部分
        p, q = head, pre
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True
```

> 💡 **一句话总结**：快慢找中点 → 反转后半 → 前后比较

### 3.8 删除链表的倒数第N个节点（#19 中等）

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
```

> 💡 **一句话总结**：fast先走n+1步，然后同步走，slow.next就是要删的节点

### 3.9 两两交换链表中的节点（#24 中等）

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next
```

> 💡 **一句话总结**：三步交换 `pre→a→b` 变为 `pre→b→a`，注意赋值顺序

---

# 🟡 第二阶段：线性结构进阶（⭐⭐ 中等）

> **目标**：掌握双指针、滑动窗口、栈的高级应用
> **预计用时**：5-7天

---

## 四、双指针

### 核心模板

```
同向双指针（slow/fast）：链表去重、数组分区
相向双指针（left/right）：两数之和、接水
```

### 4.1 移动零（#283 简单）

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i, n in enumerate(nums):
            if n:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
```

### 4.2 盛最多水的容器（#11 中等）

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
```

> 💡 **一句话总结**：相向逼近，移动短板，面积 = 宽 × 短板高

### 4.3 三数之和（#15 中等）

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans
```

> 💡 **一句话总结**：排序 + 固定一个数 + 相向双指针找两数之和，注意去重

### 4.4 接雨水（#42 困难）⭐重点

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
```

> 💡 **一句话总结**：双指针维护左右最大值，哪边矮就算哪边的接水量

---

## 五、滑动窗口

### 核心模板

```python
# 不定长滑动窗口模板
left = 0
for right in range(len(s)):
    # 扩展右边界，更新窗口状态
    ...
    while 窗口不满足条件:
        # 收缩左边界
        ...
    # 更新答案
```

### 5.1 无重复字符的最长子串（#3 中等）

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}       # 字符 → 最近出现位置
        left = ans = 0
        for right, ch in enumerate(s):
            if ch in last_idx:
                left = max(left, last_idx[ch] + 1)
            last_idx[ch] = right
            ans = max(ans, right - left + 1)
        return ans
```

> 💡 **一句话总结**：哈希记录字符最新位置，直接跳步更新left

### 5.2 找到字符串中所有字母异位词（#438 中等）

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        cnt_p, cnt_s = Counter(p), Counter()
        ans = []
        for right, ch in enumerate(s):
            cnt_s[ch] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            cnt_s[s[left]] -= 1
        return ans
```

> 💡 **一句话总结**：定长滑动窗口 + Counter比较，O(n)时间

### 5.3 和为K的子数组（#560 中等）

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}    # 前缀和 → 出现次数
        cur = ans = 0
        for num in nums:
            cur += num
            ans += prefix.get(cur - k, 0)
            prefix[cur] = prefix.get(cur, 0) + 1
        return ans
```

> 💡 **一句话总结**：前缀和 + 哈希表，`cur - k` 在表中出现过几次就有几个子数组

### 5.4 最小覆盖子串（#76 困难）⭐重点

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need, window = Counter(t), Counter()
        have, need_cnt = 0, len(need)
        left = 0
        ans = (float('inf'), '')
        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have += 1
            while have == need_cnt:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, s[left:right + 1])
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return ans[1]
```

> 💡 **一句话总结**：滑动窗口 + Counter，扩展找可行解，收缩找最优解

### 5.5 滑动窗口最大值（#239 困难）⭐重点

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()       # 单调递减队列，存下标
        ans = []
        for right, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(right)
            if q[0] <= right - k:
                q.popleft()
            if right >= k - 1:
                ans.append(nums[q[0]])
        return ans
```

> 💡 **一句话总结**：单调递减队列维护窗口最大值，队首永远是当前最大

---

## 六、栈（Stack）

### 核心知识

```python
stack = []
stack.append(x)    # 入栈
stack.pop()        # 出栈
stack[-1]          # 查看栈顶
```

### 6.1 有效的括号（#20 简单）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
```

> 💡 **一句话总结**：左括号入栈，右括号匹配栈顶，最后栈空则有效

### 6.2 最小栈（#155 中等）

```python
class MinStack:
    def __init__(self):
        self.stack = []       # (val, cur_min)

    def push(self, val: int):
        cur_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

> 💡 **一句话总结**：栈中存 `(值, 当前最小值)` 元组，O(1)获取最小值

### 6.3 每日温度（#739 中等）

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []       # 单调递减栈，存下标
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
```

> 💡 **一句话总结**：单调递减栈，当前温度高于栈顶 → 弹出并计算间隔天数

### 6.4 柱状图中最大的矩形（#84 困难）⭐重点

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]   # 哨兵
        stack = []       # 单调递增栈
        ans = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans
```

> 💡 **一句话总结**：单调递增栈 + 哨兵，出栈时计算以该柱为高的最大矩形面积

### 6.5 字符串解码（#394 中等）

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ''
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur_str, cur_num))
                cur_str, cur_num = '', 0
            elif ch == ']':
                prev_str, num = stack.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += ch
        return cur_str
```

> 💡 **一句话总结**：遇 `[` 压栈保存当前状态，遇 `]` 弹栈拼接重复字符串

---

# 🟠 第三阶段：树形结构与搜索（⭐⭐⭐ 中等偏难）

> **目标**：掌握二叉树遍历、二分查找、堆的应用
> **预计用时**：5-7天

---

## 七、二叉树

### 核心遍历模板

```python
# 前序遍历（根→左→右）
def preorder(root):
    if not root: return
    res.append(root.val)
    preorder(root.left)
    preorder(root.right)

# 中序遍历（左→根→右）—— BST有序
def inorder(root):
    if not root: return
    inorder(root.left)
    res.append(root.val)
    inorder(root.right)

# 后序遍历（左→右→根）
def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    res.append(root.val)

# 层序遍历（BFS）
from collections import deque
def levelOrder(root):
    if not root: return []
    q = deque([root])
    ans = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
    return ans
```

### 7.1 二叉树的最大深度（#104 简单）

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### 7.2 翻转二叉树（#226 简单）

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

> 💡 **一句话总结**：递归交换左右子树，Python一行交换

### 7.3 对称二叉树（#101 简单）

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l, r):
            if not l and not r: return True
            if not l or not r: return False
            return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)
        return check(root.left, root.right)
```

> 💡 **一句话总结**：递归比较左子树的左 vs 右子树的右（镜像对称）

### 7.4 二叉树的直径（#543 简单）

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if not node: return 0
            l, r = depth(node.left), depth(node.right)
            self.ans = max(self.ans, l + r)   # 直径 = 左深 + 右深
            return 1 + max(l, r)
        depth(root)
        return self.ans
```

> 💡 **一句话总结**：后序遍历，用全局变量记录最大直径

### 7.5 二叉树的层序遍历（#102 中等）

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []
        q, ans = deque([root]), []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans
```

### 7.6 验证二叉搜索树（#98 中等）

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low, high):
            if not node: return True
            return low < node.val < high and check(node.left, low, node.val) and check(node.right, node.val, high)
        return check(root, float('-inf'), float('inf'))
```

> 💡 **一句话总结**：递归验证每个节点值在 `(下界, 上界)` 范围内

### 7.7 二叉搜索树中第K小的元素（#230 中等）

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历BST得到有序序列，第k个即为答案
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
```

> 💡 **一句话总结**：中序遍历迭代写法，第k个弹出的就是第k小

### 7.8 二叉树的右视图（#199 中等）

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root: return []
        q, ans = deque([root]), []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == len(q):     # 每层最后一个（此时q已弹出当前）
                    ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans
```

### 7.9 二叉树展开为链表（#114 中等）

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right, root.left = root.left, None
        # 把原来的右子树接到当前右子树的末尾
        while root.right:
            root = root.right
        root.right = self.saved_right  # 需要额外保存
```

**更优雅的Morris遍历解法：**

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
```

> 💡 **一句话总结**：Morris遍历，把左子树整体移到右边，O(1)空间

### 7.10 从前序与中序遍历序列构造二叉树（#105 中等）

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {v: i for i, v in enumerate(inorder)}
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root = idx_map[root_val]
            left_size = in_root - in_left
            root.left = build(pre_left + 1, pre_left + left_size, in_left, in_root - 1)
            root.right = build(pre_left + left_size + 1, pre_right, in_root + 1, in_right)
            return root
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

> 💡 **一句话总结**：前序第一个是根 → 中序定位根 → 递归构建左右子树

### 7.11 二叉树的最近公共祖先（#236 中等）

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
```

> 💡 **一句话总结**：左右分别找，两边都找到则当前为最近公共祖先

### 7.12 二叉树中的最大路径和（#124 困难）⭐重点

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def gain(node):
            if not node: return 0
            l = max(gain(node.left), 0)
            r = max(gain(node.right), 0)
            self.ans = max(self.ans, l + r + node.val)
            return node.val + max(l, r)
        gain(root)
        return self.ans
```

> 💡 **一句话总结**：后序遍历，`gain`返回单边最大贡献，`ans`记录经过节点的最大路径和

### 7.13 路径总和 III（#437 中等）

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.ans = 0
        def dfs(node, cur_sum):
            if not node: return
            cur_sum += node.val
            self.ans += prefix[cur_sum - targetSum]
            prefix[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            prefix[cur_sum] -= 1      # 回溯
        dfs(root, 0)
        return self.ans
```

> 💡 **一句话总结**：前缀和 + DFS + 回溯，和"和为K的子数组"是树形版本

---

## 八、二分查找

### 核心模板

```python
# 标准二分查找
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 8.1 搜索插入位置（#35 简单）

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
```

### 8.2 在排序数组中查找元素的第一个和最后一个位置（#34 中等）

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left):
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound
        return [find_bound(True), find_bound(False)]
```

> 💡 **一句话总结**：两次二分，找左边界时收缩右端，找右边界时收缩左端

### 8.3 搜索旋转排序数组（#33 中等）

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:       # 左半有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                              # 右半有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

> 💡 **一句话总结**：先判断哪半有序，再判断target是否在有序区间内

### 8.4 寻找旋转排序数组中的最小值（#153 中等）

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

> 💡 **一句话总结**：比较mid和right，mid大则在右半找最小值

### 8.5 搜索二维矩阵（#74 中等）

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

> 💡 **一句话总结**：把二维矩阵展平为一维做二分，`mid // n` 是行，`mid % n` 是列

---

## 九、堆（优先队列）

### 核心知识

```python
import heapq
heapq.heappush(heap, x)     # 最小堆入堆
heapq.heappop(heap)          # 弹出最小值
heapq.heappushpop(heap, x)   # 先入再弹（高效）
heapq.nlargest(k, nums)      # 取前k大
# 最大堆：存负数即可
```

### 9.1 数组中的第K个最大元素（#215 中等）

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]
```

**手写最小堆版本（更面试友好）：**

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```

### 9.2 前K个高频元素（#347 中等）

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        count = Counter(nums)
        return heapq.nsmallest(k, count.keys(), key=count.get)
```

### 9.3 数据流的中位数（#295 困难）⭐重点

```python
class MedianFinder:
    def __init__(self):
        import heapq
        self.small = []    # 最大堆（存负数），存较小一半
        self.large = []    # 最小堆，存较大一半

    def addNum(self, num: int):
        import heapq
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -self.small[0])
        heapq.heappop(self.small)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

> 💡 **一句话总结**：对顶堆，大顶堆存小数，小顶堆存大数，保持平衡

---

## 十、普通数组

### 10.1 最大子数组和（#53 中等）

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans
```

> 💡 **一句话总结**：Kadane算法，`cur`记录当前子数组和，负了就重新开始

### 10.2 合并区间（#56 中等）

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
```

### 10.3 轮转数组（#189 中等）

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
```

> 💡 **一句话总结**：整体反转 + 前k个反转 + 后n-k个反转

### 10.4 除自身以外数组的乘积（#238 中等）

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # 前缀积
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # 后缀积
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans
```

> 💡 **一句话总结**：ans先存前缀积，再乘后缀积，O(n)时间O(1)空间

### 10.5 缺失的第一个正数（#41 困难）⭐重点

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

> 💡 **一句话总结**：把每个数放到正确位置（值i放在索引i-1），第一个不在位的即答案

---

## 十一、矩阵

### 11.1 螺旋矩阵（#54 中等）

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []
        while top <= bottom and left <= right:
            ans.extend(matrix[top][left:right + 1])
            top += 1
            ans.extend(matrix[i][right] for i in range(top, bottom + 1))
            right -= 1
            if top <= bottom:
                ans.extend(matrix[bottom][left:right + 1][::-1])
                bottom -= 1
            if left <= right:
                ans.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
                left += 1
        return ans
```

### 11.2 旋转图像（#48 中等）

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 每行翻转
        for row in matrix:
            row.reverse()
```

> 💡 **一句话总结**：转置 + 水平翻转 = 顺时针旋转90°

### 11.3 搜索二维矩阵 II（#240 中等）

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
```

> 💡 **一句话总结**：从右上角出发，大则左移，小则下移

### 11.4 矩阵置零（#73 中等）

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
```

---

# 🔴 第四阶段：搜索策略（⭐⭐⭐⭐ 较难）

> **目标**：掌握回溯、贪心、图论/BFS/DFS
> **预计用时**：5-7天

---

## 十二、回溯算法

### 核心模板

```python
def backtrack(路径, 选择列表):
    if 满足结束条件:
        结果.append(路径[:])
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择（回溯）
```

### 12.1 全排列（#46 中等）

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                dfs(path, used)
                path.pop()
                used[i] = False
        dfs([], [False] * len(nums))
        return ans
```

### 12.2 子集（#78 中等）

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(start, path):
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return ans
```

> 💡 **一句话总结**：每个元素选或不选，用 `start` 避免重复

### 12.3 组合总和（#39 中等）

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(start, path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                path.append(candidates[i])
                dfs(i, path, remaining - candidates[i])  # i可重复选
                path.pop()
        dfs(0, [], target)
        return ans
```

> 💡 **一句话总结**：每个数可重复选，传 `i`（不传 `i+1`）即可

### 12.4 括号生成（#22 中等）

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left, right, path):
            if len(path) == 2 * n:
                ans.append(path)
                return
            if left < n:
                dfs(left + 1, right, path + '(')
            if right < left:
                dfs(left, right + 1, path + ')')
        dfs(0, 0, '')
        return ans
```

> 💡 **一句话总结**：左括号随时加，右括号数量不能超过左括号

### 12.5 电话号码的字母组合（#17 中等）

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        def dfs(i, path):
            if i == len(digits):
                ans.append(path)
                return
            for ch in phone[digits[i]]:
                dfs(i + 1, path + ch)
        dfs(0, '')
        return ans
```

### 12.6 单词搜索（#79 中等）

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            board[i][j] = '#'
            found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or \
                    dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return found
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
```

> 💡 **一句话总结**：DFS四方向搜索，临时标记已访问，回溯恢复

### 12.7 分割回文串（#131 中等）

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(start, path):
            if start == len(s):
                ans.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:       # 判断回文
                    path.append(sub)
                    dfs(end, path)
                    path.pop()
        dfs(0, [])
        return ans
```

### 12.8 N皇后（#51 困难）⭐重点

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        diag1 = set()    # 主对角线：row - col
        diag2 = set()    # 副对角线：row + col
        def dfs(row, queens):
            if row == n:
                ans.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in queens])
                return
            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                dfs(row + 1, queens + [col])
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
        dfs(0, [])
        return ans
```

> 💡 **一句话总结**：用集合记录列和两条对角线的占用，递归放皇后+回溯

---

## 十三、贪心算法

### 核心思想：局部最优 → 全局最优

### 13.1 买卖股票的最佳时机（#121 简单）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        ans = 0
        for p in prices:
            min_price = min(min_price, p)
            ans = max(ans, p - min_price)
        return ans
```

> 💡 **一句话总结**：维护历史最低价，每天计算最大利润

### 13.2 跳跃游戏（#55 中等）

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
        return True
```

### 13.3 跳跃游戏 II（#45 中等）

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = end = max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == end:
                ans += 1
                end = max_reach
        return ans
```

> 💡 **一句话总结**：到达当前边界时必须跳一次，更新到下一边界

### 13.4 划分字母区间（#763 中等）

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans
```

> 💡 **一句话总结**：记录每个字母最后出现位置，到达最远边界时划分

---

## 十四、图论 / BFS / DFS

### 14.1 岛屿数量（#200 中等）

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
```

### 14.2 腐烂的橘子（#994 中等）

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        return minutes if fresh == 0 else -1
```

> 💡 **一句话总结**：BFS层序遍历，每层代表一分钟，腐烂所有可达的新鲜橘子

### 14.3 课程表（#207 中等）

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        state = [0] * numCourses    # 0=未访问, 1=访问中, 2=已完成
        def dfs(node):
            if state[node] == 1: return False   # 有环
            if state[node] == 2: return True
            state[node] = 1
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            state[node] = 2
            return True
        return all(dfs(i) for i in range(numCourses))
```

> 💡 **一句话总结**：DFS + 三色标记法检测有向图是否有环

### 14.4 实现 Trie（前缀树）（#208 中等）⭐重点

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

> 💡 **一句话总结**：字典树嵌套实现，`children`存子节点，`is_end`标记单词结尾

---

# 🟣 第五阶段：动态规划（⭐⭐⭐⭐⭐ 困难）

> **目标**：掌握DP状态设计和状态转移方程
> **预计用时**：7-10天
> **核心心法**：定义状态 → 推导转移 → 确定初始值 → 确定遍历顺序

---

## 十五、一维动态规划

### 15.1 爬楼梯（#70 简单）

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
```

> 💡 **一句话总结**：斐波那契数列，`dp[i] = dp[i-1] + dp[i-2]`

### 15.2 杨辉三角（#118 简单）

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            row = [1] + [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)] + [1]
            res.append(row)
        return res
```

### 15.3 打家劫舍（#198 中等）

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
```

> 💡 **一句话总结**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，空间优化为两个变量

### 15.4 完全平方数（#279 中等）

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] + 1 for j in range(1, int(i ** 0.5) + 1))
        return dp[n]
```

> 💡 **一句话总结**：完全背包，`dp[i] = min(dp[i - j²] + 1)`

### 15.5 零钱兑换（#322 中等）

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```

> 💡 **一句话总结**：完全背包求最小硬币数，`dp[i] = min(dp[i], dp[i-coin] + 1)`

### 15.6 单词拆分（#139 中等）

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
        return dp[-1]
```

> 💡 **一句话总结**：`dp[i]` 表示前i个字符能否被拆分，枚举分割点j

### 15.7 最长递增子序列（#300 中等）

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
```

> 💡 **一句话总结**：贪心+二分，维护tails数组，O(n log n)

### 15.8 乘积最大子数组（#152 中等）

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            ans = max(ans, max_prod)
        return ans
```

> 💡 **一句话总结**：同时维护最大和最小乘积，负数会翻转大小关系

### 15.9 分割等和子集（#416 中等）

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
```

> 💡 **一句话总结**：0-1背包，能否凑出总和的一半

### 15.10 最长有效括号（#32 困难）⭐重点

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]      # 哨兵
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
```

> 💡 **一句话总结**：栈存索引，`')'`弹出匹配的`'('`，长度=当前索引-栈顶索引

---

## 十六、多维动态规划

### 16.1 不同路径（#62 中等）

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
```

> 💡 **一句话总结**：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`，一维空间优化

### 16.2 最小路径和（#64 中等）

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
```

### 16.3 最长回文子串（#5 中等）

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l + 1:r]
        ans = ''
        for i in range(len(s)):
            ans = max(ans, expand(i, i), expand(i, i + 1), key=len)
        return ans
```

> 💡 **一句话总结**：中心扩展法，奇数和偶数长度分别处理

### 16.4 最长公共子序列（#1143 中等）

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

> 💡 **一句话总结**：相等则对角线+1，不等则取上方或左方较大值

### 16.5 编辑距离（#72 中等）⭐重点

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i
        for j in range(n + 1): dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
```

> 💡 **一句话总结**：`dp[i][j]` = 删除/插入/替换 三种操作取最小值+1

---

## 十七、高级链表

### 17.1 K个一组翻转链表（#25 困难）⭐重点

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            pre, cur = tail.next, head
            while cur != tail:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            return tail, head
        dummy = ListNode(0, head)
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            head, tail = reverse(head, tail)
            pre.next, pre, head = head, tail, nxt
        return dummy.next
```

### 17.2 随机链表的复制（#138 中等）

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        # 在每个节点后插入拷贝
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next, cur = copy, copy.next
        # 设置random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        new_head = head.next
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next if copy.next else None
            cur = cur.next
        return new_head
```

> 💡 **一句话总结**：三步走：插入拷贝 → 连random → 拆分

### 17.3 排序链表（#148 中等）

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 快慢指针找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        # 归并排序
        left, right = self.sortList(head), self.sortList(mid)
        dummy = cur = ListNode()
        while left and right:
            if left.val <= right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next
```

### 17.4 合并K个升序链表（#23 困难）⭐重点

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = cur = ListNode()
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
```

> 💡 **一句话总结**：最小堆每次弹出最小节点，O(n log k)

### 17.5 LRU缓存（#146 中等）⭐重点

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}       # key → node
        # 哑节点简化边界处理
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_to_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = ListNode(key, value)
        self._add_to_front(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

class ListNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None
```

> 💡 **一句话总结**：哈希表 + 双向链表，get/put都O(1)，哑节点简化操作

---

## 十八、其他技巧

### 18.1 下一个排列（#31 中等）

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 1. 从右找首个下降位
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # 2. 从右找刚好大于nums[i]的数
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 3. 反转i右侧
        nums[i + 1:] = reversed(nums[i + 1:])
```

> 💡 **一句话总结**：找下降位 → 交换 → 反转右侧，字典序下一个排列

### 18.2 寻找重复数（#287 中等）

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
```

> 💡 **一句话总结**：数组模拟链表（下标→值→下标），Floyd判圈找重复

---

# 📋 附录：知识点速查表

## 按题型分类的解题套路

| 题型 | 核心思路 | 时间复杂度 | 代表题目 |
|------|---------|-----------|---------|
| 哈希表 | 空间换时间，O(1)查找 | O(n) | 两数之和、字母异位词 |
| 双指针 | 同向/相向逼近 | O(n) | 三数之和、接雨水 |
| 滑动窗口 | 扩展右边界+收缩左边界 | O(n) | 最小覆盖子串、无重复子串 |
| 单调栈 | 维护递增/递减序列 | O(n) | 每日温度、柱状图最大矩形 |
| 二分查找 | 有序区间折半缩小 | O(log n) | 搜索旋转数组 |
| BFS | 层序遍历，队列 | O(n) | 腐烂橘子、岛屿数量 |
| DFS/回溯 | 递归+撤销选择 | O(2ⁿ) | 全排列、N皇后 |
| 贪心 | 局部最优→全局最优 | O(n) | 跳跃游戏、买卖股票 |
| 动态规划 | 状态定义+转移方程 | O(n²) | 编辑距离、最长公共子序列 |
| 并查集 | 路径压缩+按秩合并 | O(α(n)) | 岛屿数量（变体） |

## Python常用技巧速查

```python
# 1. 交换两个变量
a, b = b, a

# 2. 反转列表/字符串
nums[::-1]

# 3. 哈希表默认值
from collections import defaultdict, Counter
d = defaultdict(list)
c = Counter("hello")    # {'l': 2, 'h': 1, 'e': 1, 'o': 1}

# 4. 堆操作
import heapq
heapq.nlargest(k, nums)      # 前k大
heapq.nsmallest(k, nums)     # 前k小

# 5. 二分查找
import bisect
bisect.bisect_left(a, x)     # 第一个>=x的位置
bisect.bisect_right(a, x)    # 第一个>x的位置

# 6. 双端队列
from collections import deque
q = deque([1, 2, 3])
q.append(4)       # 右端入队
q.appendleft(0)   # 左端入队
q.popleft()       # 左端出队

# 7. 排序
nums.sort()                    # 原地排序
sorted(nums, key=abs)          # 返回新列表
intervals.sort(key=lambda x: x[0])  # 按第一个元素排序

# 8. 进制/位运算
bin(n)           # 二进制字符串
n >> 1           # 右移
n & (-n)         # 取最低位1
```

---

> 📖 **参考来源**：
> - [LeetCode 热题 100 官方学习计划](https://leetcode.cn/studyplan/top-100-liked/)
> - [力扣Hot100算法解题思路总结 - CSDN](https://blog.csdn.net/qq_69490950/article/details/156769621)
> - [LeetCode Hot100总结(Python手撕代码) - CSDN](https://blog.csdn.net/weixin_54338498/article/details/146763788)
> - [Python LeetCode热题100专题 - CSDN](https://blog.csdn.net/xiaoyuting999/article/details/149404323)
> - [力扣hot100分类整理及解题方法 - CSDN](https://blog.csdn.net/lmh_qwq/article/details/149530065)
