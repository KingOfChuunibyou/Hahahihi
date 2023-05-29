
# COMMENT
# This is a comment
# print("aaa")

pi = 3.14
radius = 2.2

# Aku lagi ingin menghitung luas lingkaran

## INI RUMUS LINGKARAN LOH!!!
area = pi * (radius ** 2)
print(area)
# INI AREA LOHHHHH!!!

# MEMORI

# VARIABLE
# integer -> int -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 [4 bytes]
# string

archel = 10 # MEMORI 4 BYTES

print(2**128)

# int = min sama max vals. -> MIN -3.000.000 MAX 3.000.000 | -> 3.000.001 -> -2.999.999
# nyewa space ada di RAM. -> 4 bytes -> 32 bits -> 2^32 -> 

# ---------

archel_nganu = 9
archel_ngeselin = False
batas_remed = 8.5

# KLO ARCHEL KURANG DARI BATAS REMED, DIA REMED + DIA NGESELIN DIMARAAHIN ORANG TUA
# KLO NGGAK NGESELIN, DIA TAPI SCORENYA DIATAS REMED DIKASIH UANG 100000
# KLO NGGAK NGESELIN, DIA REMED, DIMARAHIN GURU

if archel_nganu < batas_remed:
    if archel_ngeselin:
        print("ARCHEL DIMARAHIN ORANG TUA")
    print("ARCHEL DIMARAHIN GURU")
else:
    if archel_ngeselin:
        print("ARCHEL DIMARAHIN ORANG TUA + DAPET UANG 5000")
    else:
        print("ARCHEL DAPET UANG 100000")

