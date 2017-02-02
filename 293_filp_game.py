class Solution(object):
    def generatePossibleNextMoves(self, s):
        return [s[:i] + '--' + s[i+2:] for i in range(len(s) - 1) if s[i:i+2] == '++']


test = Solution()
s = '+++++'
print(test.generatePossibleNextMoves(s))