/* 前缀和
https://leetcode.cn/problems/range-sum-query-immutable/
给一个列表[]，和一个范围[left, right]，返回该列表在该范围中的值的和
给出的范围包含 left 和 right 所在索引的值
*/
package main

import "fmt"

type NumArray struct {
    sums []int
}

func Constructor(nums []int) NumArray {
    sums := make([]int, len(nums)+1)
    for index, value := range nums {
        sums[index+1] = sums[index] + value
    }
    return NumArray{sums}
}

func (numArray *NumArray) SumRange(left int, right int) int {
    return numArray.sums[right+1] - numArray.sums[left]
}

func main() {
    nums := []int{-2, 0, 3, -5, 2, -1}
    left := 2
    right := 5
    obj := Constructor(nums)
    param_1 := obj.SumRange(left, right)
    fmt.Printf("[sumRange left: %d right %d]: sum: %d", left, right, param_1)
}
