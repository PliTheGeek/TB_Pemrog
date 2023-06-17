print ("Selamat datang, Apakah anda ingin")
print ("1. Parkir")
print ("2. Keluar")
print ("3. Keluar Proggram ?")

pilih = int(input("Masukan Pilihanmu : "))
occupied = [ 23, 42, 1, 50, 4, 2, 6,20 ]

if pilih == 1:
    print(f"Parkiran ini ada 50 slot")
    print(f"Dan nomor tempat parkir yang terpakai ada di {occupied}")