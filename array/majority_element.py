"""
Problem: Majority Element (LeetCode 169)

Find the element that appears more than n // 2 times.

Approaches:
1. Brute Force: O(n²) time, O(1) extra space
2. Hashing: O(n) average time, O(n) extra space

Assumption: A majority element always exists.
"""

arr = [2, 2, 1, 1, 1, 2, 2]

# Approach 1: Brute Force
# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > len(arr) // 2:
#         print(arr[i])
#         break

# Approach 2: Hashing
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num, count in freq.items():
    if count > len(arr) // 2:
        print(num)
        break