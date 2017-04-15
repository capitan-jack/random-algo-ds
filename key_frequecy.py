''' Q: given a sorted array, finde frequency of a key.
    ex:- array = 1 2 2 3 4 5 5 6 7, 
          key = 2
          ans = 2
          key = 3
          ans = 1
    Soln:- use binary search for O(log(n)). Simple counting for O(n)
'''
numbers = list(map(int,input().strip().split(' ')))
key = int(input().strip())

def find_frequency(numbers, key):
    left_start = 0
    left_end = len(numbers) - 1
    right_start = 0
    right_end = len(numbers) - 1
    left_found_index = -1
    right_found_index = -1
    while left_end - left_start > 0 and right_end - right_start > 0 and\
    (left_found_index==-1 or right_found_index==-1):
        left_mid = left_start + int((left_end - left_start)/2)
        right_mid = right_start + int((right_end - right_start)/2)
        if numbers[left_mid] < key:
            left_start = left_mid + 1
        elif numbers[left_mid] > key:
            left_end = left_mid -1
        elif numbers[left_mid - 1] == key:
            left_end = left_mid
        else:
            left_found_index = left_mid
        if numbers[right_mid] < key:
            right_start = right_mid + 1
        elif numbers[right_mid] > key:
            right_end = right_mid -1
        elif numbers[right_mid + 1] == key:
            right_start = right_mid
        else:
            right_found_index = right_mid
    print(right_found_index - left_found_index + 1)


find_frequency(numbers, key)
