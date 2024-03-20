#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi = input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")
