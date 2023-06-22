

def looping_yield():
    i = 0
    while True:
        i += 1
        if i == 10:
            break
        yield i


# differences between yield and loop
# yield: generator
# loop: infinite loop

# Loop: for i in [12,3,4,5,6,6]  # KITA NGASIH LIST DAPET LANGSUNG OUTPUT
# yield: for i in looping_yield() # KITA NGASIH GENERATOR (PABRIKNYA) KELEMAHNA EKSEKUSI DULU BUAT DAPET OUTPUT
# kita dikasih list list video itu terus2an

if __name__ == "__main__":
    hasilnya = looping_yield()
    for i, angka in enumerate(hasilnya):
        if i == 20:
            break
        print("Angka yield:" , angka)
