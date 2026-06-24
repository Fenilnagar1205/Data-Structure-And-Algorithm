# Exapmle 1 — Reverse a String Using Stack
# Problem: Given "hello", reverse it to "olleh" using a stack.

# def reverse_string(s):
#     stack = []

#     for char in s:
#         stack.append(char)
    
#     result =" "
#     while len(stack) > 0:
#         result += stack.pop()
    
#     return result

# print(reverse_string("Hello"))

# Example 2 — Valid Parentheses (Classic Interview Problem)
# Problem: Given a string like "({[]})", check if brackets are properly opened and closed.
# Valid: "()" "()[]{}" "({[]})"
# Invalid: "(]" "([)]" "{"

def valid_parentheses(s):
    stack = []
    matching = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in '}])':
            if len(stack)==0:
                return False
            if stack[-1] != matching[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parentheses("({[]})"))

