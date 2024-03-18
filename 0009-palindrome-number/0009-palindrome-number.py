class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        reverse_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reverse_num = reverse_num * 10 + digit
            temp //= 10

        return reverse_num == x
        """
        :type x: int
        :rtype: bool
        """
        