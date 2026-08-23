# def isPalindrome(x):
#         if x < 0:
#             return False

#         original = x
#         reverse = 0

#         while x > 0:
#             last_digit = x % 10
#             reverse = reverse * 10 + last_digit
#             x = x // 10

#         return reverse == original  
# print(isPalindrome(121))
# print(isPalindrome(-121))
# print(isPalindrome(1221))
# print(isPalindrome(1321))

def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverse_half = 0

    while x > reverse_half:
        digit = x % 10
        reverse_half = reverse_half * 10 + digit
        x //= 10

    return x == reverse_half or x == reverse_half // 10
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(1221))
print(isPalindrome(1321))