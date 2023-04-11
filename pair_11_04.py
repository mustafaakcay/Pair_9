# Bir okul kayıt sistemi kodlayalım;

# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde
# en az 2 property 2 method barındırmalıdır.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı 
# öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. Listeye ekleme yapan, listedeki tüm 
# elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

# Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki 
#propertylerden yararlanalım.

from ogrenci  import ogrenci
from ogretmen  import ogretmen

ogretmenListe = []
ogrenciListe = []
for i in range(2):
    ogrenci1= ogrenci()
    ogrenci1.ekle(ogrenciListe)
    ogrenci1.isim()
    ogrenci1.yas()
ogretmen1 = ogretmen()
ogretmen1.ekle(ogretmenListe)
ogretmen1.isim()
ogretmen1.yas()

def sırala1(ogretmenListe):
    print("Öğretmen Listesi")
    for i in ogretmenListe:
        print(i)
def sırala(ogrenciListe):
    print("Sınıf Listesi")
    for i in ogrenciListe:
        print(i)
sırala(ogrenciListe)
sırala1(ogretmenListe)