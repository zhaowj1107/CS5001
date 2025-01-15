def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n >0:
        if n % 10 ==8:
            n = n // 10
            if n % 10 ==8:
                return True
            else:
                n = n // 10
                continue
        else:
            n = n //10
    return False


if __name__ == "__main__":
    import doctest 
    doctest.testmod(verbose=True)