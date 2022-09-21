def toFindPalindrome(inputs):
    string = inputs.lower()
    createPalindrome = string[::-1]
    return createPalindrome==string



inputs = input()
output = toFindPalindrome(inputs)
print(output)