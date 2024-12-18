def hitung_imt(weight, height):
    height = height/100
    imt = weight/height**2
    
    return  imt

def kategori(imt):
    
        if  imt < 18.5:
             kondisi = 'Underweight'
        elif  18.5 <= imt < 25:
            kondisi = 'Normal weight'
        elif  25 <= imt < 30:
            kondisi = 'Overweight'
        else:
            kondisi = 'Obesitas'
        return  kondisi

i = int(input('Berapa kali anda mau menginput data?'))

while i > 0:  
    nama =  input('Masukkan nama Anda: ')
    weight = int(input('Masukkan berat badan  (kg) : '))
    height = int(input('Masukkan tinggi badan (cm) :'))

    imt = hitung_imt(weight, height)
    kondisi = kategori(imt)
    print (nama,'dengan berat badan',weight,'dan tinggi badan',height,'kondisinya adalah',kondisi)
    i-=1




