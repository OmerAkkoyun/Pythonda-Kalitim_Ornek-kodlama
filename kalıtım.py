class Yazýlýmcý(): #Yazýlýmcý Clasý Baþlýðý Oluþturuldu./Aþaðýda Özellikler verilecek.
    def __init__(self,isim,soyisim,maaþ,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maaþ=maaþ
        self.diller=diller
#Buraya kadar sadece içinde oalcak özellikleri girdik.

    def bilgilerigoster(self):#Bilgileri göster fonksiyonunu ile yazýlýmcýnýn özelliklerini  görebiliriz.
        print("""
        ******************* Yazýlýmcýnýn Bilgileri *****************
        Ýsim= {}
        Soyisim= {}
        Maaþý= {}
        Bildiði diller= {}  
        ************************************************************      
        """.format(self.isim,self.soyisim,self.maaþ,self.diller))#format metodu kullandýk.


    def zam_yap(self,miktar):#Burda zamyap fonksiyonu ile maaþ'a zam yapýlabilecek.
        print("Zam yapýldý..")
        self.maaþ+=miktar
        print("Yeni Maaþ =",self.maaþ, "\n")

    def dil_ekle(self,yeni_dil):#Burda kullanýcýnýn yeni dil eklemesini saðlýyacak kodlar yer alýcak
        print("Yeni dil baþarýyla kaydedildi...")
        self.diller.append(yeni_dil)
        print("Yeni dil listeniz : ",self.diller, "\n")

#***********************************************************************************************************
#Buraya kadar CLASS iþlemlerini yaptýk.

yazilimci=Yazýlýmcý("Maþallah","Demir",4500,["Python","Php","Java","JavaScript"],)
#üstte yazilimci deðiþkene Yazýlýmcý clasýný entegre ettik içine özelliklerinide girdik.isim vsvs.

print(yazilimci.dil_ekle("HTML"))

print(yazilimci.zam_yap(520))
print(yazilimci.bilgilerigoster())


#ÞÝmdi Yeni Bir Class Oluþturucaz Ama Özellikleri Yukarýdan Çekicez (Kalýtým Miras konusu)

class Yoneticiler(Yazýlýmcý):#burda parantezin içine yukarýdaki class ismini yazdýk miras aldýk.
    def __init__(self,isim,soyisim,maaþ,diller,kiþi_sayisi):

        self.isim = isim
        self.soyisim = soyisim
        self.maaþ = maaþ
        self.diller = diller
        self.kiþi_sayisi=kiþi_sayisi


    def bilgilerigoster(self):
        print("""
        ******************* Yöneticinin Bilgileri *****************
        Ýsim= {}
        Soyisim= {}
        Maaþý= {}
        Bildiði diller= {} 
        Sorumlu olduðu kiþi Sayýsý = {} 
        ************************************************************      
        """.format(self.isim,self.soyisim,self.maaþ,self.diller,self.kiþi_sayisi))


yoneticiler=Yoneticiler("Omer","Akkoyun",5500,["Python","HTML","Css","Java","JavaScript","C","C++"],14)
yoneticiler.bilgilerigoster()

yoneticiler.zam_yap(500)
