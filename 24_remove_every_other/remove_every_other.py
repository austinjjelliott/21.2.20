def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    new_list = []
    for index, item in enumerate(lst):
        if index % 2 == 0:
           new_list.append(item)
    return new_list

# or the way they did it: return lst[::2] ((this uses the slicing method!))
    
    
