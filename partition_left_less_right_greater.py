def find_partition_element(numbers):
    size = len(numbers)
    max_min_tracker = [[0,0] for _ in range(size)]
    max_min_tracker[size-1][1] = numbers[size-1]
    max_min_tracker[0][0] = numbers[0]
    for i,j in zip(range(1,size), range(size-2, 0,-1)):
        max_min_tracker[i][0] = max(numbers[i], max_min_tracker[i-1][0])
        max_min_tracker[j][1] = min(numbers[j], max_min_tracker[j+1][1])
        if i>=j:     
            if numbers[i] >= max_min_tracker[i][0] and numbers[i] <= max_min_tracker[i][1]:
                return numbers[i]
            if numbers[j] >= max_min_tracker[j][0] and numbers[j] <= max_min_tracker[j][1]:
                return numbers[j]
    return None

print(find_partition_element([5,2,6,1,8,12,9,11,10]))
