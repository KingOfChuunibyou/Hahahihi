

# inp_user = input("Masukkan harga: ")

# pengguna aplikasi
# kita ngeliat ginian di websitenya

# try:
#     print("hahaha")
#     inp_user = int(inp_user)
#     print("MEONGG")
#     # baca_file = open("file.txt", "r")
# except ValueError as e:  
#     # print errornya opo
#     print(e)
#     print("Kamu buta yah, INPUT ANGKA DONG!!!")
#     print("ANGKA KAMU GW UBAH JADI 0")
#     inp_user = 0
# except FileNotFoundError:
#     # Print ngegas
#     print("WOI FILENYA MANA COBA!!!")
# finally:  # pasti dijalanin walau error atau engga
#     print("INI AKHIR DARI SEMUANYA")

# print(f"Kamu inputnya segini {inp_user}")


# Bikin class sendiri untuk exception

class ArchelError(Exception):
    """
    In adalah error archel
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    

def function_apa_kek():
    raise NotImplementedError("Belum dibikin")


ini_input = input("Masukkan nilai Biologi Archel: ")
ini_input = int(ini_input)

if ini_input > 6:
    raise ArchelError("Yakin ini ga salah input? Archel < 6 kok")
else:
    print("Nilai Archel sudah benar")

