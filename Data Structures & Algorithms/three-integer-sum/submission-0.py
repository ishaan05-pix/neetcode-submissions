
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]

                if total < target:
                    l += 1

                elif total > target:
                    r -= 1

                else:
                    result.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result
