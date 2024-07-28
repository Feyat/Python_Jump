# 1.Problemin Çözümünü Buraya Yazınız

import requests
from lxml import html
# from bs4 import BeautifulSoup as bs

'''
adres = 'https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27de_yay%C4%B1n_yapan_televizyon_kanallar%C4%B1_listesi'
baslik = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
sayfa = requests.get(adres, headers = baslik)
soup = bs(sayfa.content, features='lxml')
'''
url = 'https://www.dsmart.com.tr/kanallar'
response = requests.get(url)
tree = html.fromstring(response.content)
xpath_expression = '//*[@id="__BVID__103"]/div/div[2]/div[4]/div[2]'
kanallar = tree.xpath(xpath_expression)
for kanal in kanallar:
    print(kanal)
'''
import random
import time
kanallar = [
    'atv',
    'fox',
    'show'
]
ses_ayarları = 20
class Tv():
    def __init__(self, tv_durumu = 'kapalı', kanallar = ['atv', 'fox', 'show'], tv_bilgileri = ['OLED', 'HDMI', 'USB', 'ETHERNAT']):
        self.tv_durumu = tv_durumu
        self.ses_ayarları = ses_ayarları
        self.tv_bilgileri = tv_bilgileri
    def tvAcma(self):
        if self.tv_durumu == 'kapalı':
            print('Tv açılıyor...')
            self.tv_durumu = 'açık'
            print('Tv açıldı...')
        else:
            print('Tv açık zaten.')
    
    def tvKapatma(self):
        if self.tv_durumu=='kapalı':
            print('Tv zaten kapalı...')
        else:
            print('Tv kapatılıyor...')
            self.tv_durumu = 'kapalı'
            print('Tv kapatıldı...')
    def sesAçma(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:
            self.ses_ayarları += int(1)
            print('Ses oranı: ', self.ses_ayarları)
    def sesKapatma(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:    
            self.ses_ayarları -= 1
            print('Ses oranı: ', self.ses_ayarları)

    def kanal_ekleme(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:
            kanal_ismi = input('Kanalın ismini giriniz: ')
            kanallar.append(kanal_ismi)
            print(kanallar)

    def kanal_sayısı(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:
            print('Kanal sayısı: ',len[kanallar])

    def kanal_değiştirme(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:
            a = random.randint(0, len(kanallar)-1)
            print('Rastgele açılan kanal: ', kanallar[a])
    
    def tv_bilgisi(self):
        if self.tv_durumu == 'kapalı':
            print('Lütfen önce tv açınız.')
        else:
            print(self.tv_bilgileri)
a = Tv()
3
while 1:
    islem = input('Komutu giriniz: ')
    if islem == 'q':
        time.sleep(1)
        a.tvKapatma()
        break
    elif islem == '1':
        time.sleep(1)
        a.tvAcma()
    elif islem == '2':
        time.sleep(1)
        a.sesAçma()
    elif islem == '3':
        time.sleep(1)
        a.sesKapatma()
    elif islem == '4':
        time.sleep(1)
        a.kanal_ekleme()
    elif islem == '5':
        time.sleep(1)
        a.kanal_sayısı()
    elif islem == '6':
        time.sleep(1)
        a.kanal_değiştirme()
    elif islem == '7':
        a.tv_bilgisi()
    else:
        break
        
'''