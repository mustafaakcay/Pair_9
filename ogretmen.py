class ogretmen:
    def __init__(self) -> None:
        self.name = input (" Öğretmenin ismini giriniz:")
        self.age = input (" Öğretmenin yaşını giriniz:")
        # liste.append(name)
    def ekle(self,ogretmenListe):
        ogretmenListe.append(self.name)
    
    def yas(self):
        print(f"Öğretmenin yaşı {self.age} 'dir")
    def isim(self):
        print(f"Öğretmenin ismi {self.name} 'dir")