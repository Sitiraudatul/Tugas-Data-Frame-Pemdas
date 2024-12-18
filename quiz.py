def hitung_dt(detak_jantung,detik):
    detik = detak_jantung / 60
    ratarata = sum(detak_jantung)/(jumlah_pasien)
    return hitung_dt

# memasukan jumlah pasien
jumlah_pasien = int(input('masukkan jumlah pasien: '))

# membuat list untuk menyimpan nama pasien
nama_pasien = []

detak_jantung = []

# menggunakan perulangan untuk memasukan nama setiap pasien
for i in range(jumlah_pasien):
    nama = input(f'masukkan nama pasien ke {i+1}: ')
    nama_pasien.append(nama)
    detak_jantung = input(f'masukkan detak jantung pasien ke {i+1}: ')
    detak_jantung.append(detak_jantung)


print(f'nama pasien: ',{nama_pasien},'detak jantungnya adalah',{hitung_dt})



