"""Given a string s, find the length of the longest substring without repeating characters.

Ex: 1
Input s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Ex: 2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    left = 0
    right = 0
    temp = ''
    maxLen = 0

    while right < len(s):
        # Check if the character exists in temp
        if s[right] in temp:
            # update temp to remove the first element
            temp = temp[1:]
            left = left + 1
        else:
            # Add the character to temp if it does not exist
            temp = temp + s[right]
            # get the max length
            maxLen = max(maxLen, right - left + 1)
            right = right + 1
    return maxLen


solution = lengthOfLongestSubstring("pwwkew")
print(solution)
