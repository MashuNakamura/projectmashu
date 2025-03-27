from shape import Shape

class persegi_panjang:
    def user_input(self):
       self.panjang = int(input("Masukkan nilai Panjang : "))
       self.lebar = int(input("Masukkan nilai Lebar : "))
        
    def hasil_luas(self):
        return self.panjang * self.lebar