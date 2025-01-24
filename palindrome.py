def is_palindrome(s):
    return s==s[::-1]

string = input("enter the string:")

if is_palindrome(string):
    print("the string is palindrome ",string)
else:
    print("the string is not a palindrome",string)
