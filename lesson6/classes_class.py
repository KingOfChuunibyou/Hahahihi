

# blueprint 
class Dog:

    kingdom = "Animalia" # Class Attributes

    def __init__(self, name, tipe, umur=0):
        # self: object
        print("INI DIJALANKAN LOH")
        self.name = name  # Instance Attributes
        self.tipe = tipe
        self.umur = umur

    def _kerongkongan_bunyi(self):
        # ASUMSINYSA KERONGKONGAN KERJA
        print("kerongkongan kerjaa!")

    def speak(self, command):
        if command == "eat":
            print("aukkkk eattt0")
        elif command == "sleep":
            print("emoh auuuu")
        else:
            print("ORA MUDENG!")
        self._kerongkongan_bunyi()
        
    def run(self):
        print("AKU LARI!")

    # ulang_tahun() -> umurnya nambah 1
    
    # static method
    def blue_print_ini_keren():
        print("iya keren")
        return "kerens"

    def ulang_tahun(self):
        self.umur = self.umur + 1
    
    def __str__(self):
        return f"Nama anjing: {self.name} \nUmur: {self.umur}"

    # properties
    # jenis
    # nama

    # behavior
    # run() # method and function 

# CLASS VS INSTANCE
# BLUEPRINT VS HASIL PRODUKSI PABRIKNYA
# DOG VS ANJING ARCHEL

anjing_peliharaan_archel = Dog("archel ga punya nama", "archel")
anjing_peliharaan_suwanti = Dog("petok_petok", "herder")

print(anjing_peliharaan_archel.umur)

# Anjingnya mau kita modif ada atribut umur

print(anjing_peliharaan_archel.tipe)
# pabrik
# BLue print Dog -> Dog (instance) -> real data

## Class Vs instance attributes
print(Dog.kingdom)
print(anjing_peliharaan_archel.kingdom)

## Akses atribut/properti dalam instance
print(anjing_peliharaan_archel.kingdom)
print(anjing_peliharaan_archel.name)

anjing_peliharaan_archel.name = "semprul"
print(anjing_peliharaan_archel.name)

## Instance Methods
anjing_peliharaan_archel.speak('eat')
# Dog.speak() | ERROR, behavior is embedded into object, not TEMPLATE!

## print object yang create

print(anjing_peliharaan_archel)

anjing_peliharaan_archel.ulang_tahun()

print(anjing_peliharaan_archel)

# PRIVATE = cuma bisa dikases sama objectnya sendiri + PUBLIC = diakses oleh user
## PRIVATE: method yang cuma bisa diakses oleh instancenya sendiri

anjing_peliharaan_archel._kerongkongan_bunyi() # GA BOLEH

# STATIC: milik class (blue print) VS NON-STATIC (milik object)
print(Dog.blue_print_ini_keren())


## Relasi antar objek

## Website buat sistem sekolah, Guru dan Siswa, intinya Gurunya ini bisa nilai TUGAS SISWA, Terus siswanya bisa nyerahin tugasnya.
## Tugasnya itu berisi essay dari siswa

### OOP

## 1. Liat entitas apa aja?
## 2. Penjabarannya gimana?
## 3. Eksekusi (kerjain sekarang 15 menit) Bikin class yang menggambarkan apa yang dijabarin tadi.

class Siswa:
    pass


class Tugas:
    pass


class Guru:
    pass

