def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """ 
    s=" " 
    for i in range(0,n):
        s=s+str(i)
    x=",".join(s)
    return x
print(main(3))