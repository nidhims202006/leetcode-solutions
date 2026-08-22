class Solution:

  def longestPalindrome(self, s: str) -> str:
    if not s:
      return ""

    start, max_len = 0, 0

    def expandAroundCenter(left: int, right: int) -> int:
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      # Length of palindrome found
      return right - left - 1

    for i in range(len(s)):
      # Odd length palindromes (single character center)
      len1 = expandAroundCenter(i, i)
      # Even length palindromes (two character center)
      len2 = expandAroundCenter(i, i + 1)

      length = max(len1, len2)
      if length > max_len:
        max_len = length
        # Calculate start index based on max length found
        start = i - (length - 1) // 2

    return s[start : start + max_len]
