

class ElemenSekolah:

    def __init__(self, nama):
        self.nama = nama

    def masuk_kelas(self):
        print(f"{self.nama} masuk kelas")

class Guru(ElemenSekolah):

    def __init__(self, nama):
        super().__init__(nama)
        _udah_ngasih_makan_kucing = False

    def _minum(self):
        print("gluk3")

    # Override
    def masuk_kelas(self, haha=None):
        super().masuk_kelas() # superclass
        if haha is None:
            print("ga ketawa kamu")
        else:
            print("ketawa ih")
        print("Sekalian ngajar") 

class GuruMatematika(Guru):

    def ngajarirn_mtk_sambil_minum(self):
        self._minum()

class Siswa(ElemenSekolah):

    def masuk_kelas(self):
        print("Aku masuk kelas terus bengong")

class OfficeBoy(ElemenSekolah):
    pass


pak_semprul = Guru("semprul")
pak_semprul.masuk_kelas()

pak_julkilpli = OfficeBoy("julkipli")
pak_julkilpli.masuk_kelas()

pak_semprul._minum()  # INI PROTECTED GA BISA


# Polymorphism

