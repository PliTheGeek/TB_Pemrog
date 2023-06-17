print ("Selamat datang, Apakah anda ingin....")
print ("1. Parkir")
print ("2. Keluar")
print ("3. Keluar Proggram ?")

pilih = int(input("Masukan Pilihanmu : "))
occupied = [ 23, 42, 1, 50, 4, 2, 6,20 ]
print("===================================||")
if pilih == 1:
    while True:
        print(f"Parkiran ini ada 50 slot")
        print(f"Dan nomor tempat parkir yang terpakai di ")

        for i in occupied:
            print (i, end=" ")

        lokasi = int(input("Dimana kamu akan parkir : "))

        #for i in occupied:
        #    print (i, end=" ") ### sementara
        if lokasi > 50 :
            print("Slot Parkir tidak lebih dari 50!, ")
            print()

        elif lokasi in occupied :
            print("Tolong Masukan Lokasi yang lain...")
            print()
            
        else:
            occupied.append(lokasi)
            break
    print("Baik ini tiketnya......")

elif pilih == 2:
    jamMasuk = int(input("Masukan Jam awal masuk : "))
    jamKeluar = int(input("Jam Keluar : "))
    lamanya = jamMasuk - jamKeluar
    if lamanya <= 0:
        print("gratis")
    elif lamanya > 3:
        print(" Rp. 2000")
    elif lamanya > 6:
        print(" Rp. 3000")
    elif lamanya > 12:
        print(" Rp. 5000")
    else:
        print(" Rp. 10000")

else:
    print("Baik...")