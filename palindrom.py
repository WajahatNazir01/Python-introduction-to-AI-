def checkPalindrom(s):
    left = 0
    right= len(s)-1
    while left< right :
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

S = input("Enter a string to check weather it is palindrom or not:")
print(checkPalindrom(S))