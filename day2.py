f = open("./day2_input.txt", "r")
ids = f.readline().strip().split(",")
f.close()

running_pt_1 = 0

for id in ids:
    start, finish = id.split("-")
    
    for num in range(int(start), int(finish) + 1):
        num_str = str(num)
        num_len = len(num_str)
        if num_len % 2 == 1:
            continue
        if num_str[:num_len//2] == num_str[(num_len//2):]:
            running_pt_1 += num
            
def has_repeating_sequence(n):
    s = str(n)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            if pattern * (length // pattern_len) == s:
                return True
    
    return False


running_pt_2 = 0
for id in ids:
    start, finish = id.split("-")
    
    for num in range(int(start), int(finish) + 1):
        if has_repeating_sequence(num):
            running_pt_2 += num
    

print(running_pt_2)