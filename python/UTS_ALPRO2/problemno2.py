class Nomor_2:
    def __init__(self, min: int, max:int):
        self.min = min
        self.max = max
        self.n = 0

    def InputUser (self):
         while True:
            try:
                self.n = int(input("Masukkan nilai n : "))
                break
            except Exception:
                print("Data harus Integer")
                continue

    def Valid(self) -> bool:
        if self.n < self.min or self.n > self.max or self.n % 2 != 1:
            return False
        return True
    
    def Bilangan (self):
        number = 1
        for y in range (0, self.n):
            for x in range (0, self.n):
                if y == 0 or y == self.n - 1:
                    if number >= 10:
                        number = 1
                    print(number, end = "")
                    number += 1
                else:
                    if x == 0:
                        print("@", end = "")
                    elif x == self.n - 1:
                        print("$", end = "")
                    else:
                        print(" ", end = "")
            print()

if __name__ == "__main__":
    while True:
        start = Nomor_2(5, 89)
        start.InputUser()
        if start.Valid():
            start.Bilangan()
            break
        else:
            print("Nilai ketentuan : 5 <= n <= 89 dan Nilai harus Ganjil")
