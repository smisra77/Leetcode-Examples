s = 'babad'

#class Solution:
def longestPalindrome(s):

        if len(s) == 0:
            return ""
        ma = 0
        mu = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == s[j]:
                    print('s[i]::', s[i])
                    print('s[j]::', s[j])
                    #Slicing notation.
                    # j =2
                    #s[i:j] >> ba
                    #s[i:j+1] >> bab
                    su = s[i:j + 1]
                    print('su::', su)
                    #su[::-1]: Reverse the string
                    if su == su[::-1]:
                        print('su[::-1]', su[::-1])
                        print('------------')
                        if ma < len(su):
                            mu = su
                            ma = len(su)
        return mu

ans = longestPalindrome(s)
lans = len(ans)
print('Longest Palindromic Substring: %s and Length: %d' %(ans,lans))