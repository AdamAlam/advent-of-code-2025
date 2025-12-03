f = open("./day3_input.txt", "r")
lines = f.readlines()
f.close()
running = 0
for line in lines:
    nums = list(line.strip())
    cur_max_idx = 0
    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            break
        if int(num) > int(nums[cur_max_idx]):
            cur_max_idx = i
    
    sec_max_idx = cur_max_idx + 1
    for j in range(cur_max_idx + 1, len(nums)):
        if int(nums[j]) > int(nums[sec_max_idx]):
            sec_max_idx = j
    
    running += int(nums[cur_max_idx] + nums[sec_max_idx])

print(running)
        
    
    
