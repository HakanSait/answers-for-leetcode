class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sortedList = sorted(nums)

        firstIndex = 0
        secondIndex = len(sortedList) - 1

        while firstIndex < secondIndex:
            if sortedList[firstIndex] + sortedList[secondIndex] == target:
                answer = [nums.index(sortedList[firstIndex])]

                nums[answer[0]] = None

                answer.append(nums.index(sortedList[secondIndex]))

                return answer


            elif sortedList[firstIndex] + sortedList[secondIndex] > target:
                secondIndex -= 1

            elif sortedList[firstIndex] + sortedList[secondIndex] < target:
                firstIndex += 1

