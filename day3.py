f = open("./day3_input.txt", "r")
lines = f.readlines()
f.close()
running = 0

for line in lines:
    nums = list(line.strip())
    
    if len(nums) < 12:
        continue
    
    # Using a greedy approach: at each position, pick the largest digit
    # which still leaves enough digits remaining
    selected_indices = []
    start_pos = 0
    
    for digit_position in range(12):
        remaining_needed = 12 - digit_position - 1
        latest_pos = len(nums) - remaining_needed - 1
        
        max_digit = nums[start_pos]
        max_idx = start_pos
        
        for i in range(start_pos, latest_pos + 1):
            if nums[i] > max_digit:
                max_digit = nums[i]
                max_idx = i
        
        selected_indices.append(max_idx)
        start_pos = max_idx + 1
    
    result = ''.join(nums[i] for i in selected_indices)
    running += int(result)

print(running)