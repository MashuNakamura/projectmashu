from shape import Shape

class segitiga:
    def user_input(self):
        self.a = int(input("Masukkan nilai alas : "))
        self.t = int(input("Masukkan nilai tinggi : "))
        
    def hasil_luas(self):
        return self.a * self.t / 2