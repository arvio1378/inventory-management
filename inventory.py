import pandas as pd

# baca csv
df = pd.read_csv("inventory.csv", sep=";", encoding="utf-8-sig")
# jadikan id sebagai index
df.set_index("id", inplace=True)

# lihat barang
def lihat_barang():
    if df.empty:
        print("Data Kosong")
    else:
        print(df)

# tambah barang
def tambah_barang():
    global df
    # input data
    nama = input("Nama : ")
    kategori = input("Kategori : ")
    jumlah = int(input("Jumlah : "))
    harga = int(input("Harga : Rp. "))

    # tambah id
    if df.empty:
        id_baru = 1
    else:
        id_baru = df.index.max() + 1

    # simpan data
    data_baru = {
        "id" : id_baru,
        "nama" : nama,
        "kategori" : kategori,
        "jumlah" : jumlah,
        "harga" : harga
    }

    # jadikan dataframe dari input tadi
    df = pd.DataFrame([data_baru])
    # masukkan data ke csv
    df.to_csv("inventory.csv", mode='a', index=False, header=False, sep=";")

# update barang
def update_barang():
    global df

    # lihat tabel
    print(df)

    # pilih kolom update
    print("\n=== Kolom Update Barang ===\n")
    pilih_id = int(input("Id berapa ? "))

    # cek id lebih dari id yang ada di tabel
    if pilih_id > df.index.max():
        print("Pilih id yang sesuai !!")
        return

    # bagian kolom apa yang akan diupdate
    pilih_kolom = input("Kolom update ? ")

    if pilih_kolom == "nama":
        ubah_nama = input("nama jadi apa ? ")
        df.loc[pilih_id, "nama"] = ubah_nama
    elif pilih_kolom == "kategori":
        ubah_kategori = input("kategori jadi apa ? ")
        df.loc[pilih_id, "kategori"] = ubah_kategori
    elif pilih_kolom == "jumlah":
        ubah_jumlah = input("jumlah jadi berapa ? ")
        df.loc[pilih_id, "jumlah"] = ubah_jumlah
    elif pilih_kolom == "harga":
        ubah_harga = input("harga jadi berapa ? Rp. ")
        df.loc[pilih_id, "harga"] = ubah_harga
    else:
        print("pilih yang sesuai !!")
        return
    
    df.to_csv("inventory.csv", index=True, sep=";")

# hapus barang
def hapus_barang():
    global df
    # lihat tabel
    print(df)

    print("\n=== Hapus Barang ===\n")
    pilih_hapus = int(input("Baris berapa yang ingin dihapus (id)? "))

    # cek id lebih dari id yang ada di tabel
    if pilih_hapus > df.index.max():
        print("Pilih id yang sesuai !!")
        return
    
    df.drop([pilih_hapus], axis=0, inplace=True)
    df.to_csv("inventory.csv", index=True, sep=";")

# cari barang
def cari_barang():
    global df

    print(list(df.columns))

    print("\n=== Hapus Barang ===\n")

    cari_kolom = input("Kolom mana ? ")
    cari_barang = input("Barang apa ? ")

    cari_data = df[df[cari_kolom] == cari_barang]
    print(cari_data)
