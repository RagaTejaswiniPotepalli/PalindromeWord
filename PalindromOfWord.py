a = input("Enter a word: ")
def ispal(a):
    a = a.lower()
    b= a[::-1]
    if a==b:
        print("Entered word is a palindrome")
    else:
        print("Entered word is not a palindrome")
ispal(a)
