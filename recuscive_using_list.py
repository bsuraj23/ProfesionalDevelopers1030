def find_max(lst):
    if len(lst) == 1:        
        return lst[0]
    m = find_max(lst[1:])    
    return lst[0] if lst[0] > m else m

print(find_max([3, 9, 1, 7]))
