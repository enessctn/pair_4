#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("İkinci sayiyi giriniz: "))
sayi3 = float(input("Üçüncü sayiyi giriniz: "))

en_büyük_sayi = max(sayi1, sayi2, sayi3)

print("En Büyük Sayi:", en_büyük_sayi)