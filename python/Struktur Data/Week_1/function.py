## Function add Barang
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang : ")
    harga_barang = input("Masukkan Harga Barang : ")
    tmp_barang = {
        "Nama" : nama_barang,
        "Harga" : harga_barang,
    }
    print(f"Barang '{nama_barang}' berhasil ditambah")
    return tmp_barang

## Function view Barang
def display_barang(daftar_barang):
    for barang in daftar_barang:
        print("===========================")
        print(f"Nama    : {barang["Nama"]}")
        print(f"Harga : {barang["Harga"]}")

## Function delete barang
def hapus_barang(daftar_barang):
    nama = input("Nama barang yang ingin dihapus : ").lower()
    for i in range(0, len(daftar_barang)):
        if nama == daftar_barang[i]["Nama"].lower():
            del daftar_barang[i]
            print(f"Barang '{nama}' berhasil dihapus.")
            return
    print(f"Barang '{nama}' tidak ditemukan.")
