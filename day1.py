cur_num = 50
zero_count = 0

f = open("./day1_input.txt", "r")
for line in f:
    ins = line.strip()
    mag = int(ins[1:])
    dir = ins[0]
    
    while mag > 0:
        if dir == "L":
            cur_num -= 1
            mag -= 1
            if cur_num == 0:
                zero_count += 1
            if cur_num == -1:
                cur_num = 99
        else:
            cur_num += 1
            mag -= 1
            if cur_num == 100:
                cur_num = 0
                zero_count += 1

    # print(ins, cur_num)
        

print(zero_count)
f.close()