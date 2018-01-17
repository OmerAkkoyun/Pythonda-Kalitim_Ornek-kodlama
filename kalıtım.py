class Yaz�l�mc�(): #Yaz�l�mc� Clas� Ba�l��� Olu�turuldu./A�a��da �zellikler verilecek.
    def __init__(self,isim,soyisim,maa�,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maa�=maa�
        self.diller=diller
#Buraya kadar sadece i�inde oalcak �zellikleri girdik.

    def bilgilerigoster(self):#Bilgileri g�ster fonksiyonunu ile yaz�l�mc�n�n �zelliklerini  g�rebiliriz.
        print("""
        ******************* Yaz�l�mc�n�n Bilgileri *****************
        �sim= {}
        Soyisim= {}
        Maa��= {}
        Bildi�i diller= {}  
        ************************************************************      
        """.format(self.isim,self.soyisim,self.maa�,self.diller))#format metodu kulland�k.


    def zam_yap(self,miktar):#Burda zamyap fonksiyonu ile maa�'a zam yap�labilecek.
        print("Zam yap�ld�..")
        self.maa�+=miktar
        print("Yeni Maa� =",self.maa�, "\n")

    def dil_ekle(self,yeni_dil):#Burda kullan�c�n�n yeni dil eklemesini sa�l�yacak kodlar yer al�cak
        print("Yeni dil ba�ar�yla kaydedildi...")
        self.diller.append(yeni_dil)
        print("Yeni dil listeniz : ",self.diller, "\n")

#***********************************************************************************************************
#Buraya kadar CLASS i�lemlerini yapt�k.

yazilimci=Yaz�l�mc�("Ma�allah","Demir",4500,["Python","Php","Java","JavaScript"],)
#�stte yazilimci de�i�kene Yaz�l�mc� clas�n� entegre ettik i�ine �zelliklerinide girdik.isim vsvs.

print(yazilimci.dil_ekle("HTML"))

print(yazilimci.zam_yap(520))
print(yazilimci.bilgilerigoster())


#��mdi Yeni Bir Class Olu�turucaz Ama �zellikleri Yukar�dan �ekicez (Kal�t�m Miras konusu)

class Yoneticiler(Yaz�l�mc�):#burda parantezin i�ine yukar�daki class ismini yazd�k miras ald�k.
    def __init__(self,isim,soyisim,maa�,diller,ki�i_sayisi):

        self.isim = isim
        self.soyisim = soyisim
        self.maa� = maa�
        self.diller = diller
        self.ki�i_sayisi=ki�i_sayisi


    def bilgilerigoster(self):
        print("""
        ******************* Y�neticinin Bilgileri *****************
        �sim= {}
        Soyisim= {}
        Maa��= {}
        Bildi�i diller= {} 
        Sorumlu oldu�u ki�i Say�s� = {} 
        ************************************************************      
        """.format(self.isim,self.soyisim,self.maa�,self.diller,self.ki�i_sayisi))


yoneticiler=Yoneticiler("Omer","Akkoyun",5500,["Python","HTML","Css","Java","JavaScript","C","C++"],14)
yoneticiler.bilgilerigoster()

yoneticiler.zam_yap(500)
