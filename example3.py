def is_palindrome_str(s: str) -> bool:
    # normalize: remove non-alphanum and make lowercase (optional)
    import re
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)
    
    return helper(0, len(s) - 1)

# Examples
print(is_palindrome_str("Racecar"))        # True
print(is_palindrome_str("A man, a plan, a canal: Panama"))  # True
print(is_palindrome_str("hello"))          # False
