from typing import List


class Solution:
    def generateParantheisRecursive(self, output: list, currentString: str, opening: int, closing: int) -> None:
        if opening <= 0 and closing <= 0:
            output.append(currentString)
            return
        else:
            if opening > 0:
                self.generateParantheisRecursive(output, currentString + "(", opening - 1, closing)
            if closing > opening:
                self.generateParantheisRecursive(output, currentString + ")", opening, closing - 1)

    def generateParenthesis(self, n: int) -> List[str]:
       output = []
       self.generateParantheisRecursive(output, "", n,n)
       return output

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))
    print(s.generateParenthesis(3))
