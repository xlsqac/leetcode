"""
前缀和
https://leetcode.cn/problems/range-sum-query-immutable/
给一个列表[]，和一个范围[left, right]，返回该列表在该范围中的值的和
给出的范围包含 left 和 right 所在索引的值

在初始化时把和保存起来，sumRange 时直接根据范围取结果
这样就相当于一个 O(n) + n*O(1)
每次 sumRange 都去求和的话就相当与 n * O(n)，在查询次数多的情况下，时间大幅增加

self.nums = [0] 预先存一个值，可以省去求和和取值时的判断，取值 right 和 left 都加 1即可
求和：
if not _nums:
    _nums.append(num)
    continue
_nums.append(_nums[-1] + num)
取值：
if left == 0:
    return _nums[right]
else:
    return _nums[right] - _nums[left - 1]
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = [0]
        _nums = self.nums

        for num in nums:
            _nums.append(_nums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        _nums = self.nums
        return _nums[right + 1] - _nums[left]


nums = [-8261, 2300, -1429, 6274, 9650, -3267, 1414, -8102, 6251, -5979, -5291, -4616, -4703]
obj = NumArray(nums)
left = 4
right = 5
_sum = obj.sumRange(left, right)
print(_sum)

