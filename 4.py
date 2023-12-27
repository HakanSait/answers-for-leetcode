class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        numbers = sorted(nums1)

        answer = None

        if len(numbers) % 2 == 0:
            return (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1]) / 2

        else:
            return numbers[len(numbers) // 2]

