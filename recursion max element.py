def max_rec(lst, i=0):
    if i == len(lst)-1:
        return lst[i]
    return max(lst[i], max_rec(lst, i+1))

print(max_rec([3, 9, 2, 7]))
