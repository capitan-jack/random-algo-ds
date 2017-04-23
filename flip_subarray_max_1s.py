def find_fippable_subarray(numbers):
    best_start_end = (0,0)
    curr_max = 0
    overall_max = 0
    for i in range(len(numbers)):
        num = numbers[i]
        if num == 0:
            curr_max += 1
        if num == 1:
            curr_max -= 1
        if curr_max < 0:
            curr_max = 0
            curr_start = i + 1
        if curr_max > overall_max:
            overall_max = curr_max
            best_start_end = (curr_start, i)
    return best_start_end

print(find_fippable_subarray([1,1,1,0,1,0,0,1,1]))
