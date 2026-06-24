# Example 1— Rotate a List
# Problem: Given [1,2,3,4,5], rotate it by 2 positions to the right.
# Expected output: [4,5,1,2,3]

def rotate_right(numbers, k):
    for i in range(k):
        last = numbers.pop()         # remove last element
        numbers.insert(0, last)      # insert at front
    return numbers

print(rotate_right([1,2,3,4,5], 2))  # [4,5,1,2,3]

# Example 2- Remove duplicates
# Problem 2:
# Given [3,1,4,1,5,9,2,6,5], remove all duplicates and return only unique elements.
# Expected output: [3,1,4,5,9,2,6] (order preserved)