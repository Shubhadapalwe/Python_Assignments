# take an input from user and print wheather it is vowel or Consonant
def CheckVowelOrConsonant(ch):
    ch = ch.lower()
    if ch in ['a','e','i','o','u']:
        print("Its a vowel")
    else:
        print("Not an vowel ie cosonant")
ch = input("Enter the character: ")
CheckVowelOrConsonant(ch)

