from functools import reduce


def manipulate_your_list(list_to_be_manipulated: list[int]) -> list[int]:
    """
    Manipulate your list in any way you like
    """

    # kali2an


    # bisa map juga
    # f(y) = y*2
    # for i in range(len(list_to_be_manipulated)):
    #     list_to_be_manipulated[i] *= 2 [2,4,6]
    manipulated_list = list(map(lambda y: y * 2, list_to_be_manipulated))
    manipulated_list = [y * 2 for y in list_to_be_manipulated]

    return manipulated_list

def filter_list(list_str: list[str]) -> list[str]:
    """
    Just filter element in your list
    """
    # filter()

    # take only string contains archel
    # if returnnya true, dia bakal masuk ke list
    # f(x): 'archel' in x? True/False
    filtered_archel = filter(lambda x: "archel" in x, list_str)
    return list(filtered_archel)

def reduce_list(list_str: list[str]) -> str:
    """
    do concate string in your list
    """
    # reduce()
    # f(x,y): x+y
    reduced_list = reduce(lambda x,y: x+y, list_str)
    return reduced_list
