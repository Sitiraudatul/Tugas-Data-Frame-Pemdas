# Input:
#  Nama, Tekanan darah sistolik (mmHg). Tekanan darah diastolik (mmHg). Denyut nadi (bpm). jangan lupa tambahkan while untuk mengulang nama sebanyak 3 kali.
#  Kondisi dan Rekomendasi:
# 1. Jika tekanan darah sistolik lebih dari 180 atau diastolik lebih dari 120, rekomendasikan  pasien untuk segera mencari bantuan medis karena ini merupakan krisis hipertensi. 
# 2. Jika tidak dalam krisis hipertensi, cek tekanan darah: 
# 3. Jika sistolik lebih dari 140 atau diastolik lebih dari 90, sarankan untuk konsultasi  dengan dokter mengenai hipertensi. 
# 4. Jika sistolik antara 120 dan 139 atau diastolik antara 80 dan 89, beri tahu pasien  bahwa mereka berada dalam kategori prehipertensi. 
# 5. Jika sistolik di bawah 120 dan diastolik di bawah 80, beri tahu  pasien bahwa tekanan darahnya normal. Setelah mengecek tekanan darah, cek denyut nadi: 
# 6. Jika denyut nadi lebih dari 100 bpm, sarankan untuk memeriksa kondisi kesehatan jantung. 
# 7. Jika denyut nadi di bawah 60 bpm, sarankan untuk memeriksa apakah ada gejala lain yang mengiringi bradikardia. 
# 8. Jika denyut nadi antara 60 dan 100 bpm, beri tahu pasien bahwa denyut nadi mereka normal.
# 9. Masukan kedalam case 2 di pada fungsi switch yang sudah dibuat
# Screenshoot code dan Output berupa Nama masing masing
angka = int(input('masukan pilihan angka (1/2/3):'))
match angka:
    case 1:
        i = 1
        while (i<=3):
                nama = input('Masukkan nama anda : ')
                sistolik = int(input('Berapa tekanan darah sistolik anda? (mmHg) '))
                diastolik = int(input('Berapa tekanan darah diastolik anda? (mmHg) '))
                denyut = int(input('Berapa denyut nadi anda? (bpm) '))
                if (sistolik > 180) or (diastolik > 120) :
                    kondisi1 = 'Krisis Hipertensi dan perlu bantuan medis'
                else:
                    if (sistolik > 140) or (diastolik > 90) :
                        kondisi1 = 'Perlu konsultasi dengan dokter mengenai Hipertensi'
                    elif (139 > sistolik > 120) or (80 < diastolik < 89):
                        kondisi1 = 'Prehipertensi'
                    elif (sistolik < 120) and (diastolik < 80):
                        kondisi1 = 'Tekanan darah Normal'
                    if (denyut > 100) :
                        kondisi2 = 'Kesehatan jantung perlu di periksa'
                    elif (denyut < 60) :
                        kondisi2 = 'Kesehatan jantung perlu diperiksa apakah ada gejala lain yang mengiringi Bradikardia'
                    elif (60 < denyut <= 100):
                        kondisi2 = 'Denyut nadi Normal'
                    print('Nama : ',nama)
                    print('Tekanan Darah Sistolik : ',sistolik, ' mmHg')
                    print('tekanan Darah Diastolik : ',diastolik, ' mmHg')
                    print('Denyut Nadi : ',denyut, ' Bpm')
                    print('Kondisi pasien ',kondisi1, ', selain itu ',kondisi2)
                    i += 1
    case 3:
        print("")
    case _:
        print("input tidak valid")                