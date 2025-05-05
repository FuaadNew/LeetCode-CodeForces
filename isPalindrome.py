class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r= len(s)-1
        while l<r:
            if not self.isAlphaNum(s[l]):
                l+=1
                continue
            if not self.isAlphaNum(s[r]):
                r-=1
                continue
            if s[l].lower()!= s[r].lower():
                return False
            l+=1
            r-=1
        return True




    def isAlphaNum(self,c):
        if (ord('a') <= ord(c) <= ord('z') or 
            ord('A') <= ord(c) <= ord('Z') or 
            ord('0') <= ord(c) <= ord('9')):
            return True
        return False

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))