def toplama(sayı1,sayı2):

    return sayı1 + sayı2

def çıkarma(sayı1,sayı2):
    return sayı1 - sayı2

def carpma(sayı1,sayı2):
    return  sayı1*sayı2 

def bölme (sayı1,sayı2):
    return sayı1 / sayı2

print("yapacağınız işlemi seçin n/,"
      "1.toplama n/"
      "2. çıkarma n/"
      "3. çarpma n/"
      "4. bölme n/")

seçim = int(input("seçtiğiniz işlemi 1,2,3,4 " 
                     "olacak şekilde giriniz: "))

sayı1 = int(input("ilk sayıyı giriniz:"))
sayı2 = int(input("ikinci sayıyı giriniz:"))

if seçim ==1:
    print(sayı1,"+", sayı2, "=", toplama(sayı1,sayı2))

if seçim ==2:
    print(sayı1, "-", sayı2, "=", çıkarma(sayı1, sayı2)) 

if seçim ==3:
    print(sayı1, "*", sayı2, "=", carpma(sayı1,sayı2))  

if seçim ==4: 
    print(sayı1, "\"", sayı2, "=", bölme(sayı1,sayı2))
