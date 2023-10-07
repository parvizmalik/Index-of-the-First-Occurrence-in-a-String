# Solution 1:


def strStr(boyuk, kichik):
    for i in range(len(boyuk)-len(kichik)+1):
        if boyuk[i:i+len(kichik)]== kichik:
            return i
    return -1

print(strStr('abcxxxy','xxx'))


#Solution 2 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indexes = []
        start = 0
        while start < len(needle):
            pos= haystack.find(needle, start)

            if pos >= 0:
                return pos
            else:
                return -1

solution = Solution()
result = solution.strStr('xxyooxxy','xxy')
print(result)