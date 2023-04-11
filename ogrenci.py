class ogrenci:
    def __init__(self) -> None:
        self.name = input (" Öğrenci ismini giriniz:")
        self.age = input (" Öğrenci yaşını giriniz:")
        # liste.append(name)
    def ekle(self,ogrenciListe):
        ogrenciListe.append(self.name)
    
    def yas(self):
        print(f"Öğrencinin yaşı {self.age} 'dir")
    def isim(self):
        print(f"Öğrencinin ismi {self.name} 'dir")

