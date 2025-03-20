import filew
import json
import random
import time
import platform
import subprocess
import psutil

def get_cpu_name() -> str | None :
    system = platform.system()
    
    if system == "Windows":
        command = "wmic cpu get name"
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
        return result.stdout.split('\n')[1].strip()
    elif system == "Linux":
        with open('/proc/cpuinfo') as f:
            for line in f:
                if 'model name' in line:
                    return line.split(':')[1].strip()
    elif system == "Darwin":
        command = "sysctl -n machdep.cpu.brand_string"
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
        return result.stdout.strip()
    else:
        return "Unknown CPU"

def mem() -> int:
    memory_info = psutil.virtual_memory()
    return memory_info.total // 1000000

class Masalah1:
    def __init__(self):
        self.os = platform.system()
        self.cpu = get_cpu_name()
        self.ram = mem()

    def compare(self):
        print("SPECS:")
        print(f"  OS : {self.os}")
        print(f"  CPU: {self.cpu}")
        print(f"  RAM: {self.ram} MB")
        print()
        max_size = 100
        data_arr: list[int] = []
        for i in range(0, max_size):
            data_arr.append(random.randint(0, max_size))

        print("Bubble sort (START)")
        arr = data_arr

        # bubble sort start here
        f_start = time.time()
        arr_len = len(arr)
        for i in range(arr_len-1):
            for j in range(0, arr_len -1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        f_stop = time.time()
        print("Bubble sort (END)")
        self.bs = f_stop - f_start
        print(f"Using {max_size} data with : {self.bs}")

        print()

        print("Heap sort (START)")
        arr2 = data_arr

        # heap sort start here
        s_start = time.time()
        def heapify(arr, n, i):
            largest = i # Initialize largest as root
            l = 2 * i + 1 # left = 2*i + 1
            r = 2 * i + 2 # right = 2*i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                (arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
                heapify(arr, n, largest)
        n = len(arr2)
        for i in range(n // 2, -1, -1):
            heapify(arr2, n, i)
        for i in range(n - 1, 0, -1):
            (arr2[i], arr2[0]) = (arr2[0], arr2[i]) # swap
            heapify(arr2, i, 0)
        s_stop = time.time()
        print("Heap sort (END)")
        self.hs = s_stop - s_start
        print(f"Using {max_size} data with : {self.hs}")

    def builds(self):
        raw_str = filew.read_from_file("Output1.json")
        if raw_str != None:
            pass
            reader = json.JSONDecoder()
            parsed = reader.decode(raw_str)
            something = []
            something.extend(parsed["runs"])
            current = something[len(something)-1]["gen_num"]

            something.append({"gen_num": current + 1, "os": self.os, "cpu": self.cpu, "ram": self.ram, "sort": [
                {"name": "bubble", "time": self.bs},
                {"name": "heap", "time": self.hs}
            ]})
            write_this = {"runs": something}
            filew.write_to_file(json.dumps(write_this, indent=4), "Output1.json")
        else:
            something = {"runs": [{"gen_num": 1, "os": self.os, "cpu": self.cpu, "ram": self.ram, "sort": [
                {"name": "bubble", "time": self.bs},
                {"name": "heap", "time": self.hs}
            ]}]}
            filew.write_to_file(json.dumps(something, indent=4), "Output1.json")


if __name__ == "__main__":
    test = Masalah1()
    test.compare()
    test.builds()
