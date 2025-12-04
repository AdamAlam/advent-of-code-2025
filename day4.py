f = open("./day4_input.txt", "r")
lines = f.readlines()
f.close()

dirs = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1), (-1, 0), (0, -1)]

mat = []
for line in lines:
    mat.append(list(line.strip()))
    
rows = len(mat)
cols = len(mat[0])

res = 0

to_remove = []

def check_and_remove():
    loc = 0
    for row_num, row in enumerate(mat):
        for col_num, symbol in enumerate(row):
            if symbol == ".":
                continue
            adj_rolls = 0
            for dr, dc in dirs:
                if adj_rolls > 3: 
                    break
                nr = dr + row_num
                nc = dc + col_num
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == "@":
                    adj_rolls += 1
            if adj_rolls < 4:
                loc += 1
                to_remove.append((row_num, col_num))

    for row, col in to_remove:
        mat[row][col] = "."
        
    return loc

    
cur = check_and_remove()
res += cur

while cur > 0:
    to_remove = []
    cur = check_and_remove()
    res += cur

print(res)
            
