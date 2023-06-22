"""
1. buat variabel word untuk input user
2. buat fungsi (word sbg parameter) yg isinya:
loop untuk iterasi karakter word dari depan & belakang
# jika tdk sama -> return False
# jika sama -> return True
3. print apakah word adalah palindrome atau bukan berdasarkan return value


PALINDROM?
radar -> radar
amma -> amma
< 2 (a)
"""
word = input()

# ganjil
# genap
def is_palindrome(word):
    lower_word = word.lower()
    for i in lower_word:
        if len(lower_word) < 2:
            return True
        else:
            # r a d a r
            if lower_word[0] == lower_word[-1]:
                if len(lower_word[1:-1]) % 2 != 0: # Klo ganjil
                    # tengahnya ganjil (ini palindrome)
                    return True
                else:  # genap
                    # a d a
                    is_palindrome(lower_word[1:-1]) # TRUE / FALSE
            elif lower_word[0] != lower_word[-1]:
                return False

# r a d a r
# a d a 
# d # TRUE

# Loop aja

# r a d e r

# r[0] == r[len(word) - 1]??? 'r' == 'r'?
# r[1] == r[len(word) - 2]??? 'a' == 'e'??? False (Return False)
# Otherwise sampe tengah ga nemu conflicting chars, return True

def is_palindrome(word):
    for i in range(1/2 * len(word)):
        if word[i] != r[len(word) - (i+1)]:
            return False

    return True

if is_palindrome(word):
    print("The word " + word + " is a palindrome.")
else:
    print("The word " + word + " is not a palindrome.")

# 40


