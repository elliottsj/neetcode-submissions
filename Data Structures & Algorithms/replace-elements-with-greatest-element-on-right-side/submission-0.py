class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        arr[-1] = -1
        for i, el in reversed(list(enumerate(arr[:-1]))):
            arr[i] = greatest
            greatest = max(greatest, el)
        return arr