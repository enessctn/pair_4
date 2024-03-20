#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float(input("Lütfen maasinizi giriniz:  "))
zam_orani = float(input("Lütfen zam oranini giriniz:  "))

yeni_maas = maas + (maas * zam_orani / 100)

print("Güncel Maasiniz:", yeni_maas)
