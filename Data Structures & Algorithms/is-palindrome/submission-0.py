class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ""

        for i in s:
            if i.isalnum():
                sentence += i.lower()

        if sentence == sentence[::-1]:
            return True
        return False


        