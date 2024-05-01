class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        num2 = num
        romanValues = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        for i in romanValues:
            while num >= i[0]:
                num = num - i[0]
                result = result + i[1]
        print("first is " + result)

        result = ""
        num = num2
        while num >= 1000:
            result = result + 'M'
            num = num - 1000
        while num >= 900:
            result = result + 'CM'
            num = num - 900
        while num >= 500:
            result = result + 'D'
            num = num - 500
        while num >= 400:
            result = result + 'CD'
            num = num - 400
        while num >= 100:
            result = result + 'C'
            num = num - 100
        while num >= 90:
            result = result + 'XC'
            num = num - 90
        while num >= 50:
            result = result + 'L'
            num = num - 50
        while num >= 40:
            result = result + 'XL'
            num = num - 40
        while num >= 10:
            result = result + 'X'
            num = num - 10
        while num >= 9:
            result = result + 'IX'
            num = num - 9
        while num >= 5:
            result = result + 'V'
            num = num - 5
        while num >= 4:
            result = result + 'IV'
            num = num - 4
        while num >= 1:
            result = result + 'I'
            num = num - 1;

        print("Second is " + result)
        return result

def main():
    s = Solution()
    s.intToRoman(3000)

if __name__ == '__main__':
     main()
