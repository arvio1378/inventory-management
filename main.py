import inventory as ven

while True:
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Lihat Semua Barang")
    print("2. Tambah Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Cari Barang")
    print("6. Keluar")

    pilihan = int(input("Masukkan pilihan (1-5) : "))

    if pilihan == 1:
        ven.lihat_barang()
        
    elif pilihan == 2:
        ven.tambah_barang()

    elif pilihan == 3:
        ven.update_barang()

    elif pilihan == 4:
        ven.hapus_barang()

    elif pilihan == 5:
        ven.cari_barang()

    elif pilihan == 6:
        exit = input("Keluar (y/n) ? ")
        if exit == "y":
            break
        elif exit == "n":
            continue
        else:
            print("Pilihan salah !!")
    
    else:
        print("Pilihan salah !!")
    