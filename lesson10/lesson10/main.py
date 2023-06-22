from lesson10.cool_math import sum_two_numbers
from lesson10.wish import Wish
from lesson10.utils.fetcher import fetch_api
from lesson10.list_manipulator import manipulate_your_list, filter_list, reduce_list


def main():
    print("Ini main function")
    print(manipulate_your_list([2, 4, 6]))
    print(filter_list(['archel kucing', 'kucing', 'archel makan kucing', 'archel makan', 'meongg']))
    print(reduce_list(['archel kucing', 'kucing', 'archel makan kucing', 'archel makan', 'meongg']))
    print(''.join(['archel kucing', 'kucing', 'archel makan kucing', 'archel makan', 'meongg']))
    # fungsi or
    text_archel = ['kunyuk', 'archel kunyuk', 'archelll']
    archel_list_nganu = ['archel' in text for text in text_archel]
    print(any(archel_list_nganu))

    # fungsi and
    print(all(archel_list_nganu))
    
    # fungsi sorted (python defaultnya pake Tim Sort)
    print(sorted(text_archel))

    # Zip
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    print(list(zip(list1, list2)))
    for a,b in zip(list1, list2):
        print(a,b)

    # Enumerate
    print(list(enumerate(text_archel)))

    for index, text_kunyuk in enumerate(text_archel):
        print(index, text_kunyuk)
    
    # for looop dibanding sama map (lebih cepet map)
    

if __name__ == "__main__":
    main()
