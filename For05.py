def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    x=[]
    for i in range(A,B+1):
        x.append(i)
    return x[::-1]
print(main(2,7))