def merge_ranges(ranges):
    if not ranges:
        return []
    
    ranges.sort()
    merged = [ranges[0]]
    
    for start, end in ranges[1:]:
        if start <= merged[-1][1] + 1:  # Overlapping or adjacent
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return merged

def is_in_ranges(value, merged_ranges):
    # Binary search to check if value is in any merged range
    left, right = 0, len(merged_ranges) - 1
    
    while left <= right:
        mid = (left + right) // 2
        start, end = merged_ranges[mid]
        
        if start <= value <= end:
            return True
        elif value < start:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

with open('./day5_input.txt') as f:
    lines = [line.strip() for line in f]
    blank_idx = lines.index('')
    
    ranges = []
    for line in lines[:blank_idx]:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    values = [int(line) for line in lines[blank_idx + 1:]]

merged = merge_ranges(ranges)
print(f"Reduced {len(ranges)} ranges to {len(merged)} merged ranges")
total = sum(end - start + 1 for start, end in merged)
print(total)


res = 0
for value in values:
    if is_in_ranges(value, merged):
        res += 1

print(res)