print("Palindromic Substrings")

def function(s):

    if len(s) == 1:
        return 1
    st , end = 0, 0
    def newfunction(left, right):
        cnt = 0
        while(left >= 0 and right < len(s)) and s[left] == s[right]:
            cnt = cnt + 1
            left =  left - 1
            right = right + 1
        return cnt
    odd_total = 0
    even_total = 0
    for i in range(len(s)):
        odd_total = odd_total + newfunction(i,i)
        even_total = even_total + newfunction(i,i+1)
    return odd_total + even_total

s = "abc"

print(function(s))

print(function(s="aaa"))

    