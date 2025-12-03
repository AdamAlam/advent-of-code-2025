f = open("./day2_input.txt", "r")
ids = f.readline().strip().split(",")
f.close()

running = 0

for id in ids:
    start, finish = id.split("-")
    
    for num in range(int(start), int(finish) + 1):
        num_str = str(num)
        num_len = len(num_str)
        if num_len % 2 == 1:
            continue
        if num_str[:num_len//2] == num_str[(num_len//2):]:
            running += num

print(running)