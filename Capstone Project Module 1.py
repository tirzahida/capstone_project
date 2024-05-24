from tabulate import tabulate 

data_karyawan = [{'ID':'PTID0001', 'Nama':'Yudi Bahari', 'Usia':'40', 'Jenis Kelamin':'Pria', 'Alamat':'Jakarta Timur', 'Divisi':'Marketing'},
                 {'ID':'PTID0002', 'Nama':'Budi Utama', 'Usia':'28', 'Jenis Kelamin':'Pria', 'Alamat':'Bekasi', 'Divisi':'Sales'},
                 {'ID':'PTID0003', 'Nama':'Tono', 'Usia':'31', 'Jenis Kelamin':'Pria', 'Alamat':'Tangerang Selatan', 'Divisi':'HR'},
                 {'ID':'PTID0004', 'Nama':'Diana Putri', 'Usia':'26', 'Jenis Kelamin':'Wanita', 'Alamat':'Jakarta Selatan', 'Divisi':'Operation'}]

def main_menu():
    print('\n','-'*50)
    menu = int(input('''
Selamat datang di Database Karyawan PT Indonesia Ceria
1. Menampilkan seluruh data karyawan
2. Menambahkan data karyawan   
3. Mengupdate data karyawan
4. Menghapus data karyawan
5. Sorting data karyawan
6. Exit Program                 
Silahkan pilih Main Menu (1-6): '''))
       

    while True:
        try:
            user_input = menu

            if user_input == 1:
                tampilkan_data()
            elif user_input == 2:
                tambah_data()
            elif user_input == 3:
                update_data()
            elif user_input == 4:
                hapus_data()
            elif user_input == 5:
                sorting_data()
            elif user_input == 6:
                print('Terima kasih telah berkunjung')
                exit()
            else:
                print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')
                main_menu()
                
        except ValueError:
            print('Masukkan harus berupa angka')

def tampilkan_data():
    print('\n','-'*50)
    menu = int(input(
'''Menampilkan data karyawan
1. Menampilkan seluruh data karyawan
2. Mencari data karyawan(ID)
3. Kembali ke Menu Awal
Silahkan pilih Sub Menu Menampilkan data karyawan (1-3): '''))

    try:
        if menu == 1:
            full_data()

        elif menu == 2:
            def cari_karyawanID(data, id_cari):
                for karyawan in data:
                    if karyawan ['ID'] == id_cari:
                        return karyawan
                return None
        
            id_cari = input('Masukkan ID karyawan yang anda cari : ').upper()
            karyawan = cari_karyawanID(data_karyawan, id_cari)
            if karyawan:
                print('Data karyawan dengan ID', id_cari, 'ditemukan' )
                for key,value in karyawan.items():
                    print(f'{key}:{value}', end=' | ',)
            else:
                print('karyawan dengan ID', id_cari, 'tidak ditemukan')
        elif menu == 3:
            main_menu()
        else:
            print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')

    except IndexError:
        print('Data karyawan kosong')

def full_data():
    header = data_karyawan[0].keys()
    rows = [karyawan.values() for karyawan in data_karyawan]
    full_data = tabulate(rows, headers=header, tablefmt='grid')
    print(full_data)

def tambah_data():
    print('-'*50)
    menu = int(input(
'''Menambahkan data karyawan
1. Menambah data karyawan
2. Kembali ke Menu Utama
Silahkan pilih Sub Menu Menambahkan data karyawan : '''))
    
    if menu == 1:
        id_slice = int(data_karyawan[-1]['ID'][6:])
        tambah_id = 'PTID' + str(id_slice + 1).zfill(4)

        tambah_nama = input('Masukkan nama : ').title()
        while not tambah_nama:
            tambah_nama = input('Nama harus diisi. Masukkan Nama : ').capitalize()
    
        tambah_usia = input('Masukkan usia : ')
        while not tambah_usia.isdigit():
           tambah_usia = input('Usia harus berupa angka. Masukkan usia : ')
    
        tambah_kelamin = input('Masukkan jenis kelamin (Pria/Wanita) : ').capitalize()
        while tambah_kelamin not in ['Pria', 'Wanita']:
            tambah_kelamin = input('Pilih antara Pria atau Wanita. Masukkan jenis kelamin : ').capitalize()

        tambah_alamat = input('Masukkan alamat : ').capitalize()

        tambah_divisi = input('Masukkan divisi : ').capitalize()

        data_karyawan.append({
            'ID' : tambah_id,
            'Nama' : tambah_nama,
            'Usia' : tambah_usia,
            'Jenis Kelamin' : tambah_kelamin,
            'Alamat' : tambah_alamat,
            'Divisi' : tambah_divisi
        })

        print('Data karyawan berhasil ditambahkan')
        full_data()


    elif menu == 2:
        main_menu()
    else:
        print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')

def update_data():
    print('\n','-'*50)
    menu = int(input(
'''Mengupdate data karyawan
1. Update data karyawan
2. Kembali ke Menu Utama
Silahkan masukkan Sub Menu Mengupdate data karyawan : '''))  

    if menu == 1:
        id_cari = input('Masukkan ID yang ingin diubah : ').upper()
        keys_cari = input('Masukkan data yang ingin diubah : ').capitalize()
        value_cari = input('Masukkan value yang ingin diubah : ').capitalize()

        
        for karyawan in data_karyawan:
            if karyawan['ID'] == id_cari:
                if keys_cari == 'Usia':
                    karyawan[keys_cari] = int(value_cari)
                else:
                    karyawan[keys_cari] = value_cari
                print(f'Data {keys_cari} untuk karyawan dengan ID {id_cari} berhasil diubah')
                break
            
        if karyawan['ID'] != id_cari:
            print('Karyawan dengan ID tersebut tidak ditemukan')
        full_data() 

    elif menu == 2:
        main_menu()

    else:
        print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')

def hapus_data():
    print('\n','-'*50)
    menu = int(input('''
Menghapus data karyawan
1. Hapus data karyawan
2. Hapus semua data 
3. Kembali ke Menu Utama
Silahkan pilih Sub Menu Menghapus data karyawan : '''))
    
    if menu == 1:
        id_cari = input('Masukkan ID karyawan : ').upper()
        karyawan_ditemukan = False

        for karyawan in data_karyawan:
            if karyawan['ID'] == id_cari:
                data_karyawan.remove(karyawan)
                print(f'Data karyawan dengan ID {id_cari} berhasil dihapus')
                karyawan_ditemukan = True
                break    
            
        if not karyawan_ditemukan:
            print('ID karyawan tidak ditemukan')

        full_data()
    
    elif menu == 2:
        data_karyawan.clear()
        print('Data dihapus secara keseluruhan')
        # full_data()

    elif menu == 3:    
        main_menu()
    
    else:
        print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')

def sorting_data():
    print('-'*50)
    menu = int(input(
'''Mengurutkan data karyawan
1. Mengurutkan data karyawan berdasarkan nama (A-Z)
2. Kembali ke Main Menu
Silahkan pilih Sub Menu Mengurutkan data karyawan (1-2) : '''
    ))

    if menu == 1:
        sorting = sorted(data_karyawan, key=lambda x: x['Nama'])
        header = sorting[0].keys()
        rows = [karyawan.values() for karyawan in sorting]
        print(tabulate(rows, headers=header, tablefmt='grid'))

    elif menu == 2:
        main_menu() 
    
    else:
        print('Pilihan tidak valid. Silahkan masukkan angka sesuai pilihan')


main_menu()