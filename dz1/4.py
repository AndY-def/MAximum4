def palindrome(s):
    return s[::-1] == s
def polindrol():
    jpj=input('Ведите полиндрол ')
    if palindrome(jpj):
        print(True)
    else:
        print(False)
polindrol()