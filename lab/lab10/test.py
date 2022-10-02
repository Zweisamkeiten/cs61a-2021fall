def remove(item, lst):
    print(lst)
    if lst == []:
        return []
    if lst[0] == item:
        lst = lst[1:]
        return remove(item, lst)
    return [lst[0]] + remove(item, lst[1:])
