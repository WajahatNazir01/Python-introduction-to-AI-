
def stringReverseR(s):
    result=[]
    word=""
    for i in range(len(s)-1,-1,-1):
        if s[i]==' ':
            if word:
                # to reverse the found word
                result.append(word[::-1])
                word=""
        else:
            word+=s[i]
    if word:
            result.append(word[::-1])
    return " ".join(result)
    
print("---------------------------------------")
print("--WELCOME TO STRING REVERSING PROGRAM--")
print("---------------------------------------")
ss= input("Enter a string to revrsre words:")
res=stringReverseR(ss)
print(res)
