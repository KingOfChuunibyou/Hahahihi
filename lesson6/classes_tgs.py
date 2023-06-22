from typing import List
import random


class Tugas:
    
    def __init__(self, nama_siswa: str, isi_tugas: str):
        self.nama_siswa = nama_siswa
        self.isi_tugas = isi_tugas
        self.nilai = None
    
    def ngasih_nilai(self, nilai_baru) -> int:
        self.nilai = nilai_baru 

    def __str__(self) -> str:
        return f"Siswa: {self.nama_siswa} \nIsinya: {self.isi_tugas} \nNilai: {self.nilai}"
    
    def __repr__(self) -> str:
        return self.__str__()

class Siswa:

    def __init__(self, nama_siswa: str):
        self.nama_siswa = nama_siswa

    def ngasilin_tugas(self, isi_tugas: str) -> Tugas:
        tugas_siswa = Tugas(self.nama_siswa, isi_tugas)
        return tugas_siswa
    
    def __str__(self) -> str:
        return self.nama_siswa

    def __repr__(self) -> str:
        return self.nama_siswa

class GuruSMA2Kediri:
    """
    Guru Guru SMA 2 Kediri malas meriksa tugas
    """
    def __init__(self, nama_guru: str, siswa_yang_diajar: List[str]) -> None:
        self.nama_guru = nama_guru
        self.siswa_yang_diajar = siswa_yang_diajar
    
    def nilai_tugas(self, tugas: Tugas) -> int:
        """
        Nilai tugas, kalau Archel busuk nilainya!
        ASUMSI SEMUA GURU ITU KLO NGASIH NILAI ANGKABYA RANDOM
        GURU YANG NYEBELIN, Klo tugasnya punya Archel nilainya ACAK DIBAWAH 50
        KLO BUKAN ARCHEL NILAI ACAK DIBAWAH 100
        """
        if tugas.nama_siswa.lower() == "archel": # 
            if self.nama_guru == "Sutejo":
                print("Sutejo: WOOO ARCHEL, NYEBELINI IKI ORANG! KU ANCURIN NILAINYA!")
            # nilai tugas
            nilai_hasil_dari_guru = random.randint(0,49)  # 50 GA MASUK YA!
            tugas.ngasih_nilai(nilai_hasil_dari_guru)
            return nilai_hasil_dari_guru
        else:
            nilai_hasil_dari_guru = random.randint(0,100)  # 50 GA MASUK YA!
            tugas.ngasih_nilai(nilai_hasil_dari_guru)
            return nilai_hasil_dari_guru

# dimasukin ke suatu tempat
# TempatRuangan -> rak = banyak tugas siswa, tempat_sampah = banyak tugas siswa | tugas dimasukin ke tempat ruangan, ... tugas < 50: masuk tempat_sampah... else masuk rak.
# attributes: rak: List[Tugas], tempat_sampah: List[Tugas]
# method / behavior: masuk_tugas()

class Ruangan:

    def __init__(self):
        self.rak = []
        self.tempat_sampah = []
    
    def bakar_tugas(self):
        self.tempat_sampah = []

    def masukin_tugas(self, tugas: Tugas):
        # handle nilai belum ada
        if tugas.nilai is None:
            print("Bro, ga ada nilainya, ga bisa kami terima nih")
        else:
            if tugas.nilai < 50:
                self.tempat_sampah.append(tugas)
            else:
                self.rak.append(tugas)


siswa_archel = Siswa(nama_siswa="Archel")
siswa_mbek = Siswa(nama_siswa="Mbekk")
siswa_bejo = Siswa(nama_siswa="Bejo")

tugas_archel = siswa_archel.ngasilin_tugas("aku iki stres berantem mulu dirumah \n\n\niihhhh..") # nilai = None
print(tugas_archel)
tugas_bejo = siswa_bejo.ngasilin_tugas("AKu orang keren!")

guru_killer_sutejo = GuruSMA2Kediri("Sutejo", [siswa_archel, siswa_mbek, siswa_bejo])

print(guru_killer_sutejo.siswa_yang_diajar)

nilai_archel = guru_killer_sutejo.nilai_tugas(tugas_archel)  # tugas_archel.nilai = < 50
nilai_bejo = guru_killer_sutejo.nilai_tugas(tugas_bejo)

print(f"Nilai archel adalah {nilai_archel} | nilai bejo adalah {nilai_bejo}")

ruangan_diskriminasi = Ruangan()
ruangan_diskriminasi.masukin_tugas(tugas_archel)
ruangan_diskriminasi.masukin_tugas(tugas_bejo)

print(f"Yang masuk ke tempat sampah: {ruangan_diskriminasi.tempat_sampah}")
print(f"Yang masuk ke rak: {ruangan_diskriminasi.rak}" )

ruangan_diskriminasi.bakar_tugas()

print(f"Yang masuk ke tempat sampah: {ruangan_diskriminasi.tempat_sampah}")
print(f"Yang masuk ke rak: {ruangan_diskriminasi.rak}" )

# Cohesion vs Coupling



## Inheritance

class Car():  # base class

    def belok(self):
        print("Mulus")

    def lurus(self):
        print("LANCARRR!!")

# Truk is a Car
# Car is not truck
class Truk(Car):
    
    def __init__(self, muatan: str) -> None:
        super().__init__()
        self.muatan = muatan

    def belok(self):
        print("Kasar")

truk_archel = Truk(12)
truk_archel.belok()
truk_archel.lurus()

## Interface | template buat diisi

## ngurusin tugas sekolah, dikasih ke temenmu, trus kamu ngasih poin2 kosong yg temenmu harus isi
## temenmu harus isi poin2 kosongnya

## Animal (breath)

## inherit Animal HARUS NGISI METHOD BREATH!

class Animal:

    def breath(self):
        raise NotImplementedError()  # ngasih error


class Cat(Animal):
    pass

cat = Cat()
cat.breath()
