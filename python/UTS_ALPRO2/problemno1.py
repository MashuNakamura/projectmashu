class Nomor_1:
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

    def Bilangan(self):
        number = 1
        number_2 = self.n + 1
        setengah = (self.n // 2)

        for y in range(0, self.n):
            print(number, end = "")
            number += 1
            for x in range(1, setengah + 1):
                if x == setengah:
                    print("$", end = "")
                else:
                    if y == 0:
                        print("*", end = "")
                    else:
                        print(" ", end="")
            for x in range(1, setengah):
                if y == 0:
                    print("*", end = "")
                else:
                    print(" ", end="")
            print(number_2, end = "")
            number_2 += 1
            print();


if __name__ == "__main__":
    while True:
        start = Nomor_1(5, 89)
        start.InputUser()
        if start.Valid():
            start.Bilangan()
            break
        else:
            print("Nilai ketentuan : 5 <= n <= 89 dan Nilai harus Ganjil")
