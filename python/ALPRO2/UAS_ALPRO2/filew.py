def write_to_file(item:str, output:str) -> bool:
    file = open(output, "w+")
    try:
        file.write(item)
        file.close()
        return True
    except Exception:
        file.close()
        return False

def read_from_file(file_path:str):
    try:
        file = open(file_path, "r+")
        s = file.read()
        if s == "":
            return None
        return s
    except Exception:
        return None
