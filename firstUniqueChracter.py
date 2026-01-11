#Write a function that takes a string (e.g., "swiss") and returns the index of the first character that does not repeat. If every character repeats, return -1
def uniqueindexfinder(s):
    for j in range(len(s)):
        is_unique=True
        for i in range(len(s)):
            if i!=j and s[j]==s[i]:
                is_unique=False
                break
        if is_unique:
            return j
    return -1


ss= input("Enter string to find index of first unqiue character:")
res=uniqueindexfinder(ss)
print("Index of first unique chracter is :", res)

