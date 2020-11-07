def group_elements(l):
    """
    >>> group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]

    >>> group_elements([3, 3, 3, 3])
    [[3, 3, 3, 3]]

    >>> group_elements([3, 3, 1, 3, 3, 1])
    [[3, 3, 3, 3], [1, 1]]

    >>> group_elements([5, 3, 1, 2, 4, 10])
    [[5], [3], [1], [2], [4], [10]]
    """
    lis = []
    nodup = []
    for i in range(len(l)):
        if l[i] not in nodup:
            nodup.append(l[i])
    for uniquevalue in nodup: #Loop every unique value
        lis2 = []
        for value in l: #Check value 
            if uniquevalue == value:
                lis2.append(value)
        lis.append(lis2)
    return lis
# print(group_elements([3, 3, 1, 3, 3, 1]))

def dup_elements(l):
    """
    >>> dup_elements([1,3,3,4,2,5,8,5,6,7])
    [3,5]

    >>> dup_elements([3,3,3,3])
    [3]

    >>> dup_elements([3,3,1,3,3,1])
    [3,1]

    >>> dup_elements([5,3,1,2,4,10])

    """
    l = group_elements(l)
    print(l)
    lis = []
    for i in l:
        if len(i) > 1:
            lis.append(i[0])
    return lis
