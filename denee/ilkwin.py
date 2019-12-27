import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from oyunpen import Ui_MainWindow
import random
import time
import sqlite3


class window1(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        QWidget.setWindowTitle(self,"PALABRAS- Kurallar ve Ayarlar")
        QWidget.setStyleSheet(self,"font: 75 12pt \"Century Gothic\";")
        self.setWindowIcon(QIcon("icons/PapirusCheese.ico"))
        dosya = open("oyuncu1.txt", "w")
        dosya.close()
        self.i=0
        self.setGeometry(350,210,550,400)
        self.etiket= QLabel()
        self.kolay=QRadioButton()
        self.orta=QRadioButton()
        self.zor=QRadioButton()
        self.kolay = QRadioButton("Kolay")
        self.orta = QRadioButton("Orta")
        self.zor = QRadioButton("Zor")
        self.nickal= QLineEdit()
        self.nicklabel=QLabel()
        self.nicklabel.setText("1.oyuncu nickname:")
        self.kurallar = QLabel()
        self.kurallar.setText("                                 -> Karışık verilmiş harflerden doğru kelimeyi bulun. \n                     "
                              "-> Ne kadar hızlı cevap verirseniz o kadar yüksek puan alırsınız.\n                    "
                              "-> Doğru cevabı 30 saniye içinde vermezseniz puan alamazsınız.\n   "
                              "->Yanlış cevaplar 30 saniye içinde verilirse 5, Verilmezse 10 puan kaybedersiniz!          \n"
                              "               -> Zorluk seçimi ve nickname girişlerinden sonra oyuna geçebilirsiniz \n"
                              "                                      -> Oyunumuz 4 kişi ile oynanmaktadır")
        self.oyunagec = QPushButton("OYUNA GEÇ")
        self.oyunagec.setStyleSheet("font: 75 Bold 14pt \"Century Gothic\";")
        self.kolay.setStyleSheet("font: 75 Bold 13pt \"Century Gothic\";")
        self.orta.setStyleSheet("font: 75 Bold 13pt \"Century Gothic\";")
        self.zor.setStyleSheet("font: 75 Bold 13pt \"Century Gothic\";")
        self.oyunagec.setIcon(QIcon("icons/PapirusCheese.ico"))
        self.etiket.setPixmap(QtGui.QPixmap("icons/icon150.png"))
        h2box=QHBoxLayout()
        h2box.addWidget(self.nicklabel)
        h2box.addWidget(self.nickal)

        h3box=QHBoxLayout()
        h3box.addStretch()
        h3box.addWidget(self.etiket)
        h3box.addStretch()

        h_box= QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.kolay)
        h_box.addWidget(self.orta)
        h_box.addWidget(self.zor)
        h_box.addStretch()

        v_box = QVBoxLayout()  # dikey layout
        v_box.addLayout(h3box)
        v_box.addStretch()
        v_box.addWidget(self.kurallar)  # yazı alanını layouta ekle
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        v_box.addLayout(h2box)
        v_box.addWidget(self.oyunagec)
        self.setLayout(v_box)  # pencereye ekle layoutu

        self.kolay.clicked.connect(self.kolay1)
        self.orta.clicked.connect(self.orta1)
        self.zor.clicked.connect(self.zor1)
        self.nickal.returnPressed.connect(self.tik)

        self.oyunagec.clicked.connect(self.window2)

    def kolay1(self):
        print("kolay")
        dosya=open("zorluk.txt","w")
        dosya.write("kolay")

    def orta1 (self):
        print("orta")
        dosya = open("zorluk.txt", "w")
        dosya.write("orta")

    def zor1 (self):
        print("zor")
        dosya = open("zorluk.txt", "w")
        dosya.write("zor")

    def tik(self):
        self.i = self.i + 1
        file = open("oyuncu1.txt", "a")
        if self.i == 1:
            self.nicklabel.setText("2.oyuncu nickname:")
            self.oyuncu1 = self.nickal.text()
            self.nickal.clear()
            file.write(self.oyuncu1 + " ")
        elif self.i == 2:
            self.nicklabel.setText("3.oyuncu nickname:")
            self.oyuncu2 = self.nickal.text()
            self.nickal.clear()
            file.write(self.oyuncu2 + " ")
        elif self.i == 3:
            self.nicklabel.setText("4.oyuncu nickname:")
            self.oyuncu3 = self.nickal.text()
            self.nickal.clear()
            file.write(self.oyuncu3 + " ")
        elif self.i == 4:
            self.nicklabel.clear()
            self.oyuncu4 = self.nickal.text()
            # self.nickal.setText("Şimdi Oyuna geçebilirsiniz")
            self.nicklabel.setText("Nickname girişi tamamlandı")
            self.nickal.setText("Zorluk seçimini yapıp oyuna başlayablirsiniz")
            file.write(self.oyuncu4+" ")
        else:
            self.nickal.setText("Oyuna başlayın")

    def window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PALABRAS")

        self.ui.label.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_2.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_3.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_3.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_4.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_5.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_6.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_7.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.label_8.setStyleSheet("font: Normal 14pt \"Impact\";")
        self.ui.basla.setIcon(QIcon("icons/PapirusCheese.ico"))
        self.ui.bitir.setIcon(QIcon("icons/PapirusCheese.ico"))
        self.setWindowIcon(QIcon("icons/PapirusCheese.ico"))

        self.say=0
        self.kolay="kolay"
        self.orta="orta"
        self.zor="zor"
        self.kelimelerial()
        self.nick=[]
        self.nicklerial()
        self.t=0
        self.oyuncusay=0
        self.sure = 0
        self.score = 0
        self.ui.basla.clicked.connect(self.click)

        self.ui.kelime.returnPressed.connect(self.process)

        self.ui.bitir.clicked.connect(self.skor)
    def labelclear(self):
        self.ui.label.clear()
        self.ui.label_2.clear()
        self.ui.label_3.clear()
        self.ui.label_4.clear()
        self.ui.label_5.clear()
        self.ui.label_6.clear()
        self.ui.label_7.clear()
        self.ui.label_8.clear()
        self.ui.label_9.clear()
        self.ui.label_10.clear()

    def click (self):
        self.labelclear()
        self.start_time=time.time()
        self.ui.kelime.clear()
        self.kelime = random.choice(self.kelimeler)  # kelimeler kümesinden rastgele eleman seçildi
        kelime_harf = list(''.join(self.kelime))  # seçilen elemanı oluşturan karakterler ayrı bir listeye atandı
        self.kelimeler.remove(self.kelime)  # oyun içinde aynı elemanın birden fazla seçilmemesi için seçilen eleman silinir
        print(random.sample(kelime_harf, len(kelime_harf)))  # burayı kelime labeline koycak
        harfler = random.sample(kelime_harf, len(kelime_harf))
        lent=len(harfler)
        print(lent)

        self.ui.label.setText(harfler[0])
        self.ui.label_2.setText(harfler[1])
        self.ui.label_3.setText(harfler[2])
        self.ui.label_4.setText(harfler[3])
        if lent>4:
            self.ui.label_5.setText(harfler[4])
        if lent>5:
            self.ui.label_6.setText(harfler[5])
        if lent>6:
            self.ui.label_7.setText(harfler[6])
        if lent>7:
            self.ui.label_8.setText(harfler[7])
        if lent>8:
            self.ui.label_9.setText(harfler[8])
        if lent>9:
            self.ui.label_10.setText(harfler[9])

    def kelimelerial(self):
        dosya=open("zorluk.txt","r")
        secim=""
        secim=dosya.read()
        if secim=="kolay":
            print("seçimli")
            print("kolayyy")
            dos=open("kolay.txt","r",encoding="utf-8")
            kolayy=dos.read()
            self.kelimeler = kolayy.split(" ")
        if secim=="orta":
            print("seçimli")
            print("orta")
            dos=open("orta.txt","r",encoding="utf-8")
            orta=dos.read()
            self.kelimeler = orta.split(" ")
        if secim=="zor":
            print("seçimli")
            print("zor")
            dos=open("zor.txt","r",encoding="utf-8")
            zor=dos.read()
            self.kelimeler = zor.split(" ")

    def nicklerial(self):
        with open("oyuncu1.txt", "r") as file:
            self.oyuncular=file.read()
            self.nick=self.oyuncular.split(" ")
            print("nick")
            print(self.nick[0])

    def process(self):
        self.labelclear()
        self.finish_time=time.time()
        self.say=self.say+1
        tahmin = self.ui.kelime.text()
        self.ui.kelime.clear()
        print(tahmin)
        sayac=self.finish_time - self.start_time
        if (tahmin == self.kelime or tahmin == self.turkce_upper(self.kelime)):  # caps lock açıkken yazılırsa hata vermemesi için
            if (sayac > 30):
                print("Süre aşımı!")
                self.ui.durumtext.setText("Süre Aşımı!")
            else:
                self.score += int(30 - (sayac))  # şu anki zamandan start_time çıkarılıp tahminin kaç
                # saniyede yapıldığı bulundu, 20'den çıkarılıp alınacak skor belirlendi
                self.ui.durumtext.setText("Doğru!")
        else:
            if (sayac > 30):
                print("Yanlış tahmin ve süre aşımı!")
                self.ui.durumtext.setText("Yanlış tahmin ve süre aşımı!")
                self.score -= 10
            else:
                print("Yanlış tahmin!")
                self.ui.durumtext.setText("Yanlış!! ")
                self.score -= 5
            print("Doğru cevap:", self.kelime)
            durum=self.ui.durumtext.text()
            self.ui.durumtext.setText(durum+" Cevap : "+self.kelime)
        self.sure += (sayac)
        print("skore",self.score)
        print("sure",self.sure)

        if self.say < 6:
            self.click()
        else:
            self.oyuncusay = self.oyuncusay + 1
            self.sure=round(self.sure,3)
            con = sqlite3.connect("SkorTablosu.db")
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS tablo (isim TEXT, skor INT, zaman INT)")
            con.commit()
            gamer=str((self.oyuncusay))

            cursor.execute("Insert into tablo Values(?,?,?)",(self.nick[self.t],self.score,self.sure))
            con.commit()
            self.t = self.t + 1
            self.sure=0
            self.score=0

            #skoru tabloya kaydet, toplam skoru yeni oyuncu için sıfırla
            self.say=0
            if self.oyuncusay==4:
                self.ui.kelime.setText("Skor tablosunu görmek için Bitire tıklayın")
            else:
                self.ui.kelime.setText((self.nick[self.t])+" oyuna başlamak için başlaya bassın ")


    def skor(self):
        self.t = Skor()
        self.t.show()
        self.hide()


    def turkce_upper(self,str):  # caps lock acıkken i-I sorunu oluşturmayan upper fonksiyonu
        list2 = []
        str1 = ""
        list1 = list(str)
        for i in range(len(list1)):
            if ord(list1[i]) == 105:  # i=105
                list2.append("İ")
            else:
                list2.append(list1[i].upper())
            str1 += list2[i]
        return (str1)

class Skor(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.satir=QLabel()
        self.skor=QLineEdit()
        self.setGeometry(350, 210, 550, 400)

class Skor(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.satir=QLabel()
        self.satir.setStyleSheet("font: Normal 12pt \"Impact\";")
        self.setWindowIcon(QIcon("icons/PapirusCheese.ico"))
        self.setWindowTitle("Skor Tablosu")
        self.satir.setText("Oyuncu Numarası - Skoru - Süresi")
        self.skor1=QLabel()
        self.skor2=QLabel()
        self.skor3=QLabel()
        self.skor4=QLabel()
        self.kapat=QPushButton("Kapat")
        self.kapat.setIcon(QIcon("icons/PapirusCheese.ico"))

        self.kapat.setStyleSheet("font: Normal 11pt \"Impact\";")
        self.skor1.setStyleSheet("font: 75 Bold 11pt \"Century Gothic\";")
        self.skor2.setStyleSheet("font: 75 Bold 11pt \"Century Gothic\";")
        self.skor3.setStyleSheet("font: 75 Bold 11pt \"Century Gothic\";")
        self.skor4.setStyleSheet("font: 75 Bold 11pt \"Century Gothic\";")
        v=QVBoxLayout()
        v.addWidget(self.skor1)
        v.addWidget(self.skor2)
        v.addWidget(self.skor3)
        v.addWidget(self.skor4)
        h=QHBoxLayout()
        h.addStretch()
        h.addLayout(v)
        h.addStretch()

        self.setGeometry(550, 280, 200, 200)
        con = sqlite3.connect("SkorTablosu.db")
        cursor = con.cursor()
        cursor.execute("Select * From tablo")
        liste = cursor.fetchall()

        a= liste[0]
        a=str(a)
        b=liste[1]
        b=str(b)
        c = liste[2]
        c = str(c)
        d = liste[3]
        d = str(d)
        self.kapat.clicked.connect(self.close)

        self.skor1.setText(a)
        self.skor2.setText(b)
        self.skor3.setText(c)
        self.skor4.setText(d)

        v2=QVBoxLayout()
        v2.addWidget(self.satir)
        v2.addLayout(h)
        v2.addWidget(self.kapat)
        self.setLayout(v2)



app = QApplication(sys.argv)
winn = window1()
winn.show()
sys.exit(app.exec_())