class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use floyd's tortoise and hair to identify the intersection point and
        # then use a second slow pointer to find the dupe
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow