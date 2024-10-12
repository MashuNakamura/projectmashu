def take_name(daftar_kontak):
    # Easy to Understand
    for i, kontak in enumerate(daftar_kontak, start=1):
        print(f"{i}. {kontak['nama']}")
    # Hard to Understand
    # for i in enumerate(daftar_kontak, start=1):
    #     print(f"{i[0]}. {i[1]['nama']}")

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("============================")
        for nomor in kontak:
            print(f"Nama : {kontak[nomor]}")