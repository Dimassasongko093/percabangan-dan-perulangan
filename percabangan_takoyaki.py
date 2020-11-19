# percabangan Tokoyaki
print("============================================")
print("selamat datang di Guri-GuritaYum :D")
print("takoyaki apa yang anda ingin pesan di hari yang ceria ini :)")
print("============================================")
print("Menu Takoyaki GGY")
print("1. Takoyaki cheese ink = Rp.2000/pcs")
print("2. Takoyaki deep sea = Rp.2500/pcs")

takoyaki = int(input("anda ingin Takoyaki yang mana = "))
if takoyaki == 1:
    harga = 2000
    banyak = int(input("Anda mau berapakah Takoyakinya = "))
    if banyak <= 10:
        print("============================================")
        print("anda memesan Takoyaki cheese ink")
        print("sebanyak : %s"% banyak)
        print("")
        bayar = harga * banyak
        print("Total semua pesanan anda adalah : Rp.%s"% bayar)
    
    if banyak >= 45:
        print("============================================")
        print("mohon maaf kita cuma menyediakan 45 Takoyaki cheese ink")
        print("anda bisa datang besok jika ingin memesan lagi :}")
    
    elif banyak >= 10:
        print("============================================")
        print("anda memesan Takoyaki cheese ink 10pcs lebih")
        print("selamat anda dapat diskon 10%")
        print("")
        harga_asli = harga * banyak
        total_harga = harga * banyak
        diskon = total_harga * 10/100
        bayar = total_harga - diskon
        print("Total Harga asli anda Rp.%s"% harga_asli)
        print("dan ini Total Harga Discon anda Rp.%s"% bayar)
        print("")
        print("Total yang harus anda bayar adalah : Rp.%s"% bayar)

elif takoyaki == 2:
    harga = 2500
    banyak = int(input("Anda mau berapakah Takoyakinya = "))
    if banyak <= 8:
        print("============================================")
        print("anda memesan Takoyaki deep sea")
        print("sebanyak %s"% banyak)
        print(" ")
        bayar = harga * banyak
        print("Total semua pesanan anda adalah : Rp.%s"% bayar)
    
    if banyak >=40:
        print("============================================")
        print("mohon maaf kita cuma menyediakan 40 Takoyaki deep sea")
        print("anda bisa datang besok jika ingin memesan lagi :}")
    
    elif banyak >=8:
        print("============================================")
        print("anda memesan Takoyaki deep sea 8pcs lebih")
        print("selamat anda dapat diskon 8%")
        print("")
        harga_asli = harga * banyak
        total_harga = harga * banyak
        diskon = total_harga * 8/100
        bayar = total_harga - diskon
        print("Total Harga asli anda Rp.%s"% harga_asli)
        print("dan ini Total Harga Discon anda Rp.%s"% bayar)
        print("")
        print("Total yang harus anda bayar adalah : Rp.%s" % bayar)
else:
    ("============================================")
    print("mohon maaf kita cuma punya dua variasi tokoyaki mohon dipilih lagi :O")

print("============================================")
print("terima kasih sudah memesan di Guri-GuritaYum :D")
