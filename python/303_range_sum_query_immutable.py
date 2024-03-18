class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        _nums = self.nums

        for num in nums:
            if not _nums:
                _nums.append(num)
                continue
            _nums.append(_nums[-1] + num)


    def sumRange(self, left: int, right: int) -> int:
        _nums = self.nums
        return _nums[right] - _nums[left]


