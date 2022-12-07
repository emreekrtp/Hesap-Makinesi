print("""
Hesap Makinesi

TOPLAMA İŞLEMİ YAPMAK İÇİN 1' e BASIN
ÇIKARMA İŞLEMİ YAPMAK İÇİN 2' e BASIN
ÇARPMA İŞLEMİ YAPMAK İÇİN 3' e  BASIN
BÖLME İŞLEMİ YAPMAK İÇİN 4' e BASIN
ÜSSÜ İŞLEMİ YAPMAK İÇİN 5' e BASIN

""")

islem = str(input("işlem Seçiniz:"))

if islem == "1":
    sayi1 = int(input("sayi1 girin :"))
    sayi2 = int(input("sayi2 girin :"))
    print("Sonuç: ", sayi1 + sayi2)



elif islem == "2":
    sayi1 = int(input("sayi1 girin :"))
    sayi2 = int(input("sayi2 girin :"))
    print("Sonuç:", sayi1-sayi2)



elif islem == "3":
    sayi1 = int(input("sayi1 girin :"))
    sayi2 = int(input("sayi2 girin :"))
    print("Sonuç:", sayi1 * sayi2)


elif islem == "4":
    sayi1 = int(input("sayi1 girin :"))
    sayi2 = int(input("sayi2  girin:"))
    print("Sonuç:", sayi1/sayi2)


elif islem == "5":
    sayi1 = int(input("sayi1 girin:"))
    sayi2 = int(input("sayi2 giriniz:"))
    print("Sonuç:", sayi1 ** sayi2)


else:
    print("GEÇERSİZ TUŞLAMA YAPTINIZ..")

