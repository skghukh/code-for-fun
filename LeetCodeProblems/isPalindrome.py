class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if not x:
            return True
        if x[0] in {'+','-1'}:
            return False #as number is signed it can't be palindrome
        startPointer = 0
        endPointer = len(x)-1
        while startPointer < endPointer:
            if x[startPointer] != x[endPointer]:
                return False
            startPointer = startPointer + 1
            endPointer = endPointer -1
        return True


def main():
    s = Solution()
    ret = s.isPalindrome(111)
    print("is this a palindrome ", ret)

if __name__ == "__main__":
    main()
