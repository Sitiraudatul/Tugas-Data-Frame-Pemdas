# program rekomendasi asupan air

nama = input('masukan nama anda: ')
usia = int(input('masukan usia anda: '))
gender = input('pilih jenis kelamin anda L/P: ')

if usia <=2:
    hasil = ('masih diberi ASI')
else :
    if usia >= 3 and usia <= 18:
        hasil = '1.6 liter' if gender else '1.4 liter'
    elif usia > 18 and usia < 64:
        hasil = '1.6 liter' if gender else '1.4 liter'
    elif usia >= 64:
        hasil = '2.0 liter' if gender else '1.8 liter'
print(nama, 'usia',usia,'dengan jenis kelamin',gender,'rekomendasi asupan air adalah: ',hasil)                 