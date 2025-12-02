# palindrome_recursive.py
# Recursive palindrome checker (ignores non-alphanumeric and case)

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (recursive), False otherwise."""
    def helper(left: int, right: int) -> bool:
        # move left forward past non-alnum
        while left < right and not s[left].isalnum():
            left += 1
        # move right backward past non-alnum
        while left < right and not s[right].isalnum():
            right -= 1
        if left >= right:
            return True
        if s[left].lower() != s[right].lower():
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)

if __name__ == "__main__":
    tests = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "No 'x' in Nixon",
        ""
    ]
    for t in tests:
        print(f"'{t}' -> {is_palindrome(t)}")