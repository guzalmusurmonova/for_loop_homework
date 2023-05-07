def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    x=[]
    for i in range(len(list1)):
        
        x.append(list1[i].capitalize())
    return x
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))