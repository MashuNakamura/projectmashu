import json

# ALGORITMA
# 1. BUAT PATTERN DAN SIMPAN KE DALAM ARRAY TEMPORARY / SEMENTARA 

# 2. LOAD FILE -> UNTUK MENGAMBIL DATA JSON DAN PANJANG DATA JSON

# 3. SIMPAN DATA JSON KE SUATU VARIABEL DAN TAMBAHKAN DATA BARU KE JSON YANG TELAH DISIMPAN

# 4. KIRIMKAN DATA KE FILE JSON
class Square:

    def __init__(self) -> None:
        pass

# membuat pattern
    def exercise(self, n):
        pattern = []

        for y in range(0, n + 1):
            temp = ""
            for _ in range(0, (n - y) + 1):
                temp += " "
            temp += "*"
            for _ in range(1, (y * 2 - 1) + 1):
                temp += " "
            if(y != 0):
               temp += "*"
            pattern.append(temp)

        return pattern

# load json jika ada return file json, jika tidak ada return {} -> dictionary
    def load_json(self):
        try:
            with open('output1.json', 'r') as f:
                return json.load(f)
        except Exception:
            return {}

# kirim data ke file json
    def write_json(self, pattern, n):

        # menyimpan file json yang telah di load ke dalam variabel
        key = self.load_json()

        # melihat panjang jsonnya
        iter = len(key) + 1

        # menambahkan value baru ke data yang telah disimpan -> key
        key[f"output-{iter}"] = {
            'nilai': n,
            'pattern': pattern
        }

        with open('output1.json', 'w') as f:
            json.dump(key, f, indent=4)

if __name__ == '__main__':
    square = Square()

    # membuat nilai n sesuai dengan input dari user
    start = int(input("Masukkan nilai n : "))
    y = start
    x = start - 1

    data = square.exercise(x)
    square.write_json(data, y)

    print(data)
