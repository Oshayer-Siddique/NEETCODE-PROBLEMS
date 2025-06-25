print("Longest Palindromic Substring")


def function(s):
    if len(s) == 1:
        return s
    
    st,end = 0,0
    def newfunction(left,right):
        while(left>= 0 and right < len(s)) and s[left] == s[right]:
            left = left  - 1
            right = right + 1
        return left+1, right-1
    
    for i in range(len(s)):
        #odd palindrome
        left1 , right1 = newfunction(i,i)
        #even palindrome
        left2 , right2 = newfunction(i,i+1)

        if(right1 - left1 > end -st):
            st, end = left1, right1
        if(right2 - left2 > end - st):
            st, end = left2 ,right2
    
    return s[st:end+1]


s = "ababd"

print(function(s))




