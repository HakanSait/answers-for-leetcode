class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        combination_lengths = []

        while len(s) != 0:
            new_combination = ''

            i = 0
            while not s[i] in new_combination:
                new_combination += s[i]
                i += 1

                if i == len(s):
                    i -= 1
                    break

            combination_lengths.append(len(new_combination))
            s = s[s.find(s[i]) + 1:]

        return max(combination_lengths, default=0)

