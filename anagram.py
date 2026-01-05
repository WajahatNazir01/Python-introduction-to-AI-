def checkAnagram(s1, s2):
    # Check if lengths are equal
    if len(s1) != len(s2):
        print("Not anagrams")
        return False
    
    # Create frequency array
    count = [0] * 26
    
    # Process first string
    for char in s1:
        if 'a' <= char <= 'z':
            count[ord(char) - ord('a')] += 1
        else:
            print("Only lowercase letters supported")
            return False
    
    # Process second string
    for char in s2:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            count[index] -= 1
            # Early exit if count goes negative
            if count[index] < 0:
                print("Not anagrams")
                return False
        else:
            print("Only lowercase letters supported")
            return False
    
    # Final check (all zeros)
    for c in count:
        if c != 0:
            print("Not anagrams")
            return False
    
    print("Strings are anagrams")
    return True


# Get input from user
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Call the function
result = checkAnagram(s1, s2)
print("Result:", result)