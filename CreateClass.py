class PersegiPanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def _str_(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main() :
    try:
        panjang = float(input("Masukkan panjang persegi:  "))
        lebar = float(input("Masukkan lebar persegi: "))

        if(panjang <=0 or lebar <=0):
            print("Nilai tidak boleh negatif atau nol")

        else:
            pp = PersegiPanjang(panjang, lebar)
            print(pp)
            print("keliling: ", pp.hitung_keliling())
            print("Luas", pp.hitung_luas())

    except ValueError:
        print("Input harus berupa angka.")

main()
