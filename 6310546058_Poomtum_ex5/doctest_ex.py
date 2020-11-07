def string_interleave(s1, s2):
    """
    Mix two strings(s1,s2) by alternating each character of them starting with the larger string.
    
    Args:
        s1,s2(string): string value

    Returns:
        string : mix by alternating s1 and s2

    Raises:
        ValueError: if s1 or s2 is not a string
    
    Examples:
    >>> string_interleave("abc","mnopq")
    'manbocpq'

    >>> string_interleave("mnopq","abc")
    'manbocpq'

    >>> string_interleave("Hello","Sawasdee Thailand")
    'SHaewlalsodee Thailand'

    >>> string_interleave("Mine","Thai")
    'TMhianie'

    >>> string_interleave("Poomtum","Ratanarat")
    'RPaotoamntaurmat'

    >>> string_interleave(6,5)
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest string_interleave[5]>", line 1, in <module>
        string_interleave(6,5)
      File "C:/Users/acer/Desktop/Programming/Python/6310546058_Poomtum_ex5/doctest_ex.py", line 39, in string_interleave
        raise ValueError(f"s1 is not a string; s1 value is {s1} and s1 type is {type(s1)}")
    ValueError: s1 is not a string; s1 value is 6 and s1 type is <class 'int'>
    """
    if isinstance(s1, str) is False:
        raise ValueError(f"s1 is not a string; s1 value is {s1} and s1 type is {type(s1)}")
    if isinstance(s2, str) is False:
        raise ValueError(f"s2 is not a string; s2 value is {s2} and s1 type is {type(s2)}")
    a = ""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            a += s1[i] + s2[i]
        for i in range(len(s2), len(s1)):
            a += s1[i]
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            a += s2[i] + s1[i]
        for i in range(len(s1), len(s2)):
            a += s2[i]
    else:
        if s1 > s2:
            for i in range(len(s2)):
                a += s1[i] + s2[i]
            for i in range(len(s2), len(s1)):
                a += s1[i]
        else:
            for i in range(len(s1)):
                a += s2[i] + s1[i]
            for i in range(len(s1), len(s2)):
                a += s2[i]

    return a


def selective_sum(n, k):
    """
    return the sum of the k largest digits of n
    
    Args:
    int (n,k) : Integer input n and k

    Returns:
    sum of the k largest digits of n

    Raises:
    ValueError: n and k is not integer
    
    Examples:
    >>> selective_sum(3018,2)
    11

    >>> selective_sum(593796,3)
    25

    >>> selective_sum(12345,10)
    15

    >>> selective_sum(124515,3)
    14

    >>> selective_sum("nono",5)
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest selective_sum[3]>", line 1, in <module>
        selective_sum("nono",5)
      File "C:/Users/acer/Desktop/Programming/Python/6310546058_Poomtum_ex5/doctest_ex.py", line 97, in selective_sum
        raise ValueError(f"n is not a int; n value is {n} and s1 type is {type(n)}")
    ValueError: n is not a int; n value is nono and s1 type is <class 'str'>
    """
    if not isinstance(n, int):
        raise ValueError(f"n is not a int; n value is {n} and s1 type is {type(n)}")
    if not isinstance(k, int):
        raise ValueError(f"k is not a int; k value is {k} and s1 type is {type(k)}")
    l = [int(i) for i in str(n)]
    l.sort(reverse=True)
    return sum(l[0:k])


def list_intersect(l1, l2):
    """
    return intersection of l1,l2 in a list containing no duplicate

    Args:
    2 List containing numbers: l1 and l2

    Returns:
    1 List of intersection numbers between l1 and l2 with no duplicates

    Raise:
    ValueError : l1,l2 is not list

    Examples:
    >>> list_intersect([1, 2, 1, 3, 4], [1, 2, 2, 3, 4])
    [1, 2, 3, 4]

    >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4]

    >>> list_intersect([9, 10, 11, 12], [5, 6, 7, 8])
    []

    >>> list_intersect([9, 10, 11, 12], [5, 6, 9, 10, 7, 8])
    [9, 10]

    >>> list_intersect([1,2,3],[3,4,5])
    [3]

    >>> list_intersect((1,2),(2,1))
    Traceback (most recent call last):
      File "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest list_intersect[5]>", line 1, in <module>
        list_intersect((1,2),(2,1))
      File "C:/Users/acer/Desktop/Programming/Python/6310546058_Poomtum_ex5/doctest_ex.py", line 149, in list_intersect
        raise ValueError
    ValueError

    """
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise ValueError
    l = []
    for i in l1:
        if i not in l:
            if i in l2:
                l.append(i)
    return l
