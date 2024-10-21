import filew
import json

class Nomor_2:

    def __init__(self, min: int, max:int):
        self.min = min
        self.max = max
        self.n = 0

    def Valid(self) -> bool:
        if self.n < self.min or self.n > self.max or self.n % 2 != 1:
            return False
        return True

    def UserInput (self):
        while True:
            try:
                self.n = int(input("Masukkan nilai n : "))
                break
            except Exception:
                print("Nilai harus bertipe Integer !")
                continue

    def Generate(self):
        value = 1
        array = []

        for y in range(0, self.n):
            tmp = ""
            if y % 2 == 0:
                valueGenap = 1
                value = 1
                for i in range(0, self.n):
                    if i != self.n - 1:
                        print(f"{value} x ", end ="")
                        tmp += f"{value} x "
                    else:
                        print(f"{value} = ", end ="")
                        tmp += f"{value} = "
                    valueGenap *= value
                    value += 2
                print(f"{valueGenap}")
                tmp += f"{valueGenap}"
            else :
                valueGenap = 0
                value = 2
                for i in range(0, self.n):
                    if i != self.n - 1:
                        print(f"{value} + ", end ="")
                        tmp += f"{value} + "
                    else:
                        print(f"{value} = ", end ="")
                        tmp += f"{value} = "
                    valueGenap += value
                    value += 2
                print(f"{valueGenap}")
                tmp += f"{valueGenap}"
            array.append(tmp)
        self.data = array

    def inijson(self):
        raw_json = filew.read_from_file("output2.json")
        if raw_json != None:
            pass
            reader = json.JSONDecoder()
            parsed = reader.decode(raw_json)
            valuejson = []
            valuejson.extend(parsed["Output"])
            current = valuejson[len(valuejson)-1]["gen_num"]

            valuejson.append({"gen_num": current + 1, "n": self.n, "data": self.data})
            write_this = {"Output": valuejson}
            filew.write_to_file(json.dumps(write_this, indent=4), "output2.json")
        else:
            valuejson = {"Output": [{"gen_num": 1, "n": self.n, "data": self.data}]}
            filew.write_to_file(json.dumps(valuejson, indent=4), "output2.json")

if __name__ == "__main__":
    start = Nomor_2(9, 99)
    while True:
        print("=================================================")
        print("Nilai harus 9 <= n <= 99 dan harus Ganjil !")
        print("=================================================")
        start.UserInput()
        if start.Valid():
            start.Generate()
            start.inijson()
            break
        print("Nilai harus 9 <= n <= 99 dan harus Ganjil !")
