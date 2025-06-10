# Program Toko Obat (Terminal)

obat = [
    {"nama": "Amlodipine", "register": 1289, "stok": 200, "harga": 3420},
    {"nama": "Candesartan", "register": 3490, "stok": 600, "harga": 3230},
    {"nama": "Captopril", "register": 1266, "stok": 240, "harga": 1200},
    {"nama": "Fenofibrate", "register": 3308, "stok": 320, "harga": 2890},
    {"nama": "Atorvastatin", "register": 4366, "stok": 540, "harga": 5600},
]

log_harga = []  # Menyimpan log perubahan harga obat
def tampilkan_daftar():
    print("\n=== Tampilkan Data Obat ===")
    print("1. Tampilkan semua data")
    print("2. Tampilkan berdasarkan nomor register")
    pilihan = input("Pilih opsi (1/2): ").strip()

    if pilihan == "1":
        print("\nDaftar Obat")
        print("Index | Nama Obat       | Register  | Stok | Harga")
        print("----------------------------------------------------")
        for i, item in enumerate(obat):
            print(f"{i+1:<5} | {item['nama']:<15} | {item['register']:<9} | {item['stok']:<4} | {item['harga']}")
    elif pilihan == "2":
        try:
            register_input = int(input("Masukkan nomor register: "))
            data = cari_obat_by_register(register_input)
            if data:
                print("\nData Obat:")
                print(f"Nama     : {data['nama']}")
                print(f"Register : {data['register']}")
                print(f"Stok     : {data['stok']}")
                print(f"Harga    : Rp{data['harga']}")
            else:
                print("x Obat dengan register tersebut tidak ditemukan.")
        except ValueError:
            print("Register harus berupa angka!")
    else:
        print("Pilihan tidak valid.")

def tampilkan_log_perubahan_harga():
    print("\n Riwayat Perubahan Harga Obat:")
    if not log_harga:
        print("Belum ada perubahan harga yang dicatat.")
        return

    print("No | Waktu               | Nama Obat       | Register | Harga Lama | Harga Baru")
    print("-------------------------------------------------------------------------------")
    for i, log in enumerate(log_harga):
        print(f"{i+1:<2} | {log['waktu']} | {log['nama']:<15} | {log['register']:<8} | Rp{log['harga_lama']:<9} | Rp{log['harga_baru']}")

def tambah_obat():
    print("\n=== Tambah Obat Baru ===")

    while True:
        nama = input("Masukkan nama obat: ").strip()
        if nama:
            break
        else:
            print("Nama obat tidak boleh kosong!")

    while True:
        try:
            register = int(input("Masukkan register obat (angka unik): "))
            if any(item["register"] == register for item in obat):
                print("Register ini sudah terdaftar. Masukkan register yang lain.")
            else:
                break
        except ValueError:
            print("Register harus berupa angka!")

    while True:
        try:
            stok = int(input("Masukkan stok obat: "))
            if stok >= 0:
                break
            else:
                print("Stok harus bernilai nol atau lebih.")
        except ValueError:
            print("Stok harus berupa angka!")

    while True:
        try:
            harga = int(input("Masukkan harga obat: "))
            if harga >= 0:
                break
            else:
                print("Harga harus bernilai nol atau lebih.")
        except ValueError:
            print("Harga harus berupa angka!")

    print("\nSilakan periksa kembali data obat yang Anda masukkan:")
    print(f"Nama     : {nama}")
    print(f"Register : {register}")
    print(f"Stok     : {stok}")
    print(f"Harga    : Rp{harga}")

    konfirmasi = input("Apakah data ini sudah benar? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        obat.append({"nama": nama, "register": register, "stok": stok, "harga": harga})
        print("V Obat berhasil ditambahkan!")
    else:
        print("x Penambahan dibatalkan.")

def hapus_obat():
    print("\n=== Menu Hapus Obat ===")
    print("1. Hapus berdasarkan register")
    print("2. Hapus berdasarkan index")
    pilihan = input("Pilih metode hapus (1/2): ").strip()

    if pilihan == "1":
        hapus_obat_berdasarkan_register()
    elif pilihan == "2":
        hapus_obat_berdasarkan_index()
    else:
        print("Pilihan tidak valid.")

def hapus_obat_berdasarkan_register():
    print("\n=== Hapus Obat Berdasarkan Register ===")

    if not obat:
        print("Tidak ada data obat yang tersedia.")
        return

    print("\nDaftar Obat Saat Ini:")
    print("Index | Nama Obat       | Register  | Stok | Harga")
    print("----------------------------------------------------")
    for i, item in enumerate(obat):
        print(f"{i+1:<5} | {item['nama']:<15} | {item['register']:<9} | {item['stok']:<4} | {item['harga']}")

    try:
        register_input = int(input("\nMasukkan nomor register obat yang ingin dihapus: "))
    except ValueError:
        print("Register harus berupa angka!")
        return

    for i, item in enumerate(obat):
        if item["register"] == register_input:
            print("\nData obat ditemukan:")
            print(f"Nama    : {item['nama']}")
            print(f"Stok    : {item['stok']}")
            print(f"Harga   : Rp{item['harga']}")

            konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").strip().lower()
            if konfirmasi == 'y':
                obat.pop(i)
                print("v Obat berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            return

    print("x Register tidak ditemukan. Data tidak tersedia.")

def hapus_obat_berdasarkan_index():
    print("\n=== Hapus Obat Berdasarkan Index ===")

    if not obat:
        print("Tidak ada data obat yang tersedia.")
        return

    print("\nDaftar Obat Saat Ini:")
    print("Index | Nama Obat       | Register  | Stok | Harga")
    print("----------------------------------------------------")
    for i, item in enumerate(obat):
        print(f"{i+1:<5} | {item['nama']:<15} | {item['register']:<9} | {item['stok']:<4} | {item['harga']}")

    try:
        index_input = int(input("\nMasukkan index obat yang ingin dihapus: ")) - 1
    except ValueError:
        print("Index harus berupa angka!")
        return

    if 0 <= index_input < len(obat):
        item = obat[index_input]
        print("\nData obat yang dipilih:")
        print(f"Nama    : {item['nama']}")
        print(f"Register: {item['register']}")
        print(f"Stok    : {item['stok']}")
        print(f"Harga   : Rp{item['harga']}")

        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").strip().lower()
        if konfirmasi == 'y':
            obat.pop(index_input)
            print("v Obat berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("x Index tidak valid.")

def beli_obat():
    keranjang = []
    total_belanja = 0

    while True:
        tampilkan_daftar()
        try:
            index = int(input("Masukkan index obat yang ingin dibeli (0 untuk selesai): ")) - 1
            if index == -1:
                break
            if 0 <= index < len(obat):
                jumlah = int(input(f"Masukkan jumlah {obat[index]['nama']} yang ingin dibeli: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari nol.")
                    continue
                if obat[index]['stok'] >= jumlah:
                    subtotal = jumlah * obat[index]['harga']
                    keranjang.append({
                        "nama": obat[index]['nama'],
                        "jumlah": jumlah,
                        "harga": obat[index]['harga'],
                        "subtotal": subtotal,
                        "index": index
                    })
                    total_belanja += subtotal
                    print(f"v Ditambahkan {jumlah} x {obat[index]['nama']} ke keranjang.")
                else:
                    print("x Stok tidak mencukupi.")
            else:
                print("x Index tidak valid!")
        except ValueError:
            print("x Input harus berupa angka!")

    if not keranjang:
        print("x Tidak ada barang yang dibeli.")
        return

    # Tampilkan ringkasan belanja
    print("\n Ringkasan Belanja:")
    for item in keranjang:
        print(f"{item['jumlah']} x {item['nama']} @ Rp{item['harga']} = Rp{item['subtotal']}")
    print(f"Total Belanja: Rp{total_belanja}")

    # Pembayaran
    while True:
        try:
            uang = int(input("Masukkan jumlah uang yang dibayarkan: "))
            if uang < total_belanja:
                print(f"x Uang tidak cukup. Kurang Rp{total_belanja - uang}")
            else:
                kembalian = uang - total_belanja
                print(f"v Pembayaran berhasil. Kembalian Anda: Rp{kembalian}")
                # Kurangi stok
                for item in keranjang:
                    obat[item["index"]]['stok'] -= item["jumlah"]
                break
        except ValueError:
            print("Input harus berupa angka!")

def cari_obat_by_register(register_input):
    for item in obat:
        if item["register"] == register_input:
            return item
    return None

from datetime import datetime

def update_harga_obat():
    print("\n=== Update Harga Obat ===")

    if not obat:
        print("Data obat kosong, tidak ada yang bisa diupdate.")
        return

    try:
        register_input = int(input("Masukkan nomor register obat yang ingin diupdate harganya: "))
    except ValueError:
        print("Register harus berupa angka!")
        return

    data = cari_obat_by_register(register_input)
    if data:
        harga_lama = data['harga']
        print(f"\nData obat ditemukan:")
        print(f"Nama     : {data['nama']}")
        print(f"Harga lama: Rp{harga_lama}")

        try:
            harga_baru = int(input("Masukkan harga baru: "))
            if harga_baru < 0:
                print("Harga harus bernilai nol atau lebih.")
                return
        except ValueError:
            print("Harga harus berupa angka!")
            return

        if harga_baru == harga_lama:
            print("Harga tidak berubah.")
            return

        data['harga'] = harga_baru
        log_harga.append({
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nama": data["nama"],
            "register": data["register"],
            "harga_lama": harga_lama,
            "harga_baru": harga_baru
        })

        print(f"v Harga berhasil diperbarui dari Rp{harga_lama} menjadi Rp{harga_baru}")
    else:
        print("x Obat dengan nomor register tersebut tidak ditemukan.")

while True:
    print("\nSelamat Datang di Toko Obat")
    print("Menu:")
    print("1. Menampilkan Daftar Obat")
    print("2. Menambah Obat")
    print("3. Menghapus Obat")
    print("4. Membeli Obat")
    print("5. Cari Obat Berdasarkan Register")
    print("6. Update Harga Obat")
    print("7. Tampilkan Log Perubahan Harga")
    print("8. Keluar")

    pilihan = input("Masukkan nomor menu yang ingin dijalankan: ").strip()

    if pilihan == "1":
        tampilkan_daftar()
    elif pilihan == "2":
        tambah_obat()
    elif pilihan == "3":
        hapus_obat()
    elif pilihan == "4":
        beli_obat()
    elif pilihan == "5":
        try:
            register_input = int(input("Masukkan nomor register: ").strip())
            hasil = cari_obat_by_register(register_input)
            if hasil:
                print("\nData Obat Ditemukan:")
                print(f"Nama Obat : {hasil['nama']}")
                print(f"Stok      : {hasil['stok']}")
                print(f"Harga     : Rp{hasil['harga']}")
            else:
                print("Register tidak terdaftar.")
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")
    elif pilihan == "6":
        update_harga_obat()
    elif pilihan == "7":
        tampilkan_log_perubahan_harga()
    elif pilihan == "8":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")