class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mset = set(nums)
        count = 0

        for i in mset:
            if i-1 not in mset:
                curr_num = i
                curr_streak = 1
                while curr_num + 1 in mset:
                    curr_num += 1
                    curr_streak += 1

                count = max(count, curr_streak) 
        
        return count

        
