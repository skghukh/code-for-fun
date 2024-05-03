class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print("Matching  with  ",s,p)
        if s == "" and p == "":
            return True
        # if s == "" or p == "":
        #     return False
        # if len(s) == 1:
        #     if len(p) == 1 and  (s[0] == p[0] or p[0] == '.')   :
        #         return True
        #     else:
        #         return False

        p_len = len(p)
        s_len = len(s)

        if p[p_len-1] ==  '.':
            return self.isMatch(s[:-1], p[:-1])
        elif p[p_len-1] == '*':
            if  s_len > 0 and self.is_matching(p, p_len, s, s_len):  #case when last character is matching
                return self.isMatch(s[:-1],p)
            return self.isMatch(s,p[:-1])
        elif p[p_len-1] ==  s[s_len-1]:
            return self.isMatch(s[:-1],p[:-1])
        return False

    def is_matching(self, p, p_len, s, s_len):
        return p[p_len - 2] == s[s_len - 1] or p[p_len-2] == '.'


def main():
    s = Solution()
    print(s.isMatch("aab","c*a*b"))

if __name__ == "__main__":
    main()




