#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy = float(input("Lütfen boyunuzu giriniz:  "))
agirlik = float(input("Lütfen kilonuzu giriniz:  "))

Vki = agirlik / (boy * boy) 

print("Vücut Kitle Endeksiniz:", Vki)
