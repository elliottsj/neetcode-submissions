class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        to_del = []
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                to_del.append(i)
            else:
                k += 1
        for j in reversed(to_del):
            del nums[j]
        return k