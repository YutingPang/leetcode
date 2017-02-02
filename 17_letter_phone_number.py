class Solution(object):
    def letterCombinations(self, digits):
        """
        : type digits: str
        : type List[str]
        """
        kvmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for i in range(len(digits)):
            for letter in kvmap[]

