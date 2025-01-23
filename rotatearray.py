class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while(k!=0):
            lst=nums.pop()
            nums.insert(0,lst)
            k-=1
        return nums
