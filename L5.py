# LEETCODE: 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Python solution
def reverse(x):
    # Define the 32-bit integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Handle negative numbers
    sign = -1 if x < 0 else 1
    x = abs(x)

    # Reverse the digits
    reversed_x = 0
    while x != 0:
        # Check for overflow before updating reversed_x
        if reversed_x > (INT_MAX - x % 10) // 10:
            return 0
        reversed_x = reversed_x * 10 + x % 10
        x //= 10

    # Apply the sign and check for overflow
    result = sign * reversed_x
    if result > INT_MAX or result < INT_MIN:
        return 0

    return result

# LETCODE: 125
# Valid Palindrome
def isPalindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Check if the string is equal to its reverse
    return s == s[::-1]