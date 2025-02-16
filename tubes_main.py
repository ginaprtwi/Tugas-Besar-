import csv

file_name = "tubes.csv"


def load_data():
    try:
        with open(file_name, mode='r', newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader if len(row) == 2]
    except FileNotFoundError:
        return []


def save_data(data):
    with open(file_name, mode='w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def show_data(data):
    print("-" * 40)
    print("\nDaftar entry Kamus Gen Alpha: \n")
    for i, row in enumerate(data, 1):
        if len(row) == 2:
            kata, arti = row
            print(f"{i}.{kata} : {arti}")
    print("\n", "-" * 40, sep="")


def add_data(data):
    kata = input("Masukkan Kata: ")
    arti = input(f"Masukkan Makna ({kata}): ")
    data.append([kata, arti])
    save_data(data)
    print(f"Entry,\n"
          f"{kata} - {arti}\n"
          f"Berhasil ditambahkan!")


def edit_data(data):
    show_data(data)
    index = int(input("Masukkan nomor entry yang ingin diubah: ")) - 1
    if 0 <= index < len(data):
        kata = input(f"Masukkan kata baru ({data[index][0]}): ") or data[index][0]
        arti = input(f"Masukkan makna baru dari ({kata}) ({data[index][1]}): ") or data[index][1]
        data[index] = [kata, arti]
        save_data(data)
        print("Entry berhasil diubah!")
    else:
        print("Entry tidak ada")


def delete_data(data):
    show_data(data)
    index = int(input("Masukan nomor entry yang ingin dihapus: ")) - 1
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        print("Entry berhasil dihapus!")
    else:
        print("Entry tidak ada")


def search_data(data):
    keyword = input("Masukkan kata kunci pencarian: ").lower()
    found = False
    for row in data:
        if any(keyword == element.lower() for element in row):
            found = True
            break
    if found:
        hasil = [e for e in data if keyword in e[0].lower() or keyword in e[1].lower()]
        print(f"{keyword} ditemukan! \n")
        for i, row in enumerate(hasil, 1):
            if len(row) == 2:
                kata, arti = row
                print(f"{i}.{kata} - {arti}")
        print("\n", "-" * 40, sep="")
        lanjut = input("Tekan enter untuk kembali ke menu utama.......")
    else:
        print("Entry tidak ditemukan!\nCoba lagi!")
        search_data(data)



def SelectionSort(data, posisi=0):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][posisi].lower() < data[min_index][posisi].lower():
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def sort_data(data):
    pilihan = input("Urutkan entry berdasarkan (1: Kata 2: Makna): ").lower()
    valid = True
    if pilihan == "1":
        data = SelectionSort(data, 0)
    elif pilihan == "2":
        data = SelectionSort(data, 1)
    else:
        print("Input tidak valid!")
        valid = False

    if valid:
        save_data(data)
        print("-" * 40)
        print("\nDaftar entry berhasil diurutkan!")
        print("\nDaftar entry: ")
        for i, row in enumerate(data, 1):
            if len(row) == 2:
                kata, arti = row
                print(f"{i}. {kata} : {arti}")
        print("\n")
    else:
        return 0


def main():
    data = load_data()
    while True:
        print("-" * 40)
        print("""
Selamat Datang di SiMaK Gen Alpha!
(Sistem Manajemen Kamus Gen Alpha)

Silahkan Memilih Opsi Berikut:

1. Tambah Entry
2. Ubah Entry
3. Hapus Entry
4. Cari Entry
5. Urutkan Entry
6. Tampilkan Entry
0. Keluar
        """)
        print("-" * 40)
        pilihan = input("Pilih Menu : ")
        if pilihan == "1":
            add_data(data)
        elif pilihan == "2":
            edit_data(data)
        elif pilihan == "3":
            delete_data(data)
        elif pilihan == "4":
            search_data(data)
        elif pilihan == "5":
            sort_data(data)
        elif pilihan == "6":
            show_data(data)
        elif pilihan == "0":
            print("Keluar dari program............")
            break
        else:
            print("Pilihan tidak valid! Coba lagi. \n")


if __name__ == "__main__":
    main()