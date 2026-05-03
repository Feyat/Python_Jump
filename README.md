# Python Jump — Yetgen 12 Haftalık Python Eğitimi Notlarım

> **Yetgen** bünyesinde düzenlenen 12 haftalık Python eğitim programı boyunca tuttuğum notlar ve yazdığım uygulama kodları. 
> Haftalık canlı derslerle ilerledik — bu repo o sürecin bir yansıması.

---

## Program Hakkında

| | |
|---|---|
| **Program** | Yetgen — Python Eğitimi |
| **Süre** | 12 Hafta |
| **Format** | Haftalık Canlı Dersler |
| **Sonuç** | Sertifika alındı |
| **Dil / Araç** | Python 3, VS Code |

---

## Repo Yapısı

```
Python_Jump/

Hafta_01/ → Veri Tipleri & Değişkenler
Hafta_02/ → Veri Tipleri & Değişkenler (devam)
Hafta_03/ → Döngüler & Koşullar
Hafta_04/ → Döngüler & Koşullar (devam)
Hafta_05/ → Fonksiyonlar
Hafta_06/ → Fonksiyonlar (devam)
Hafta_07/ → Nesne Yönelimli Programlama (OOP)
Hafta_08/ → OOP (devam)
Hafta_09/ → Modüller & Kütüphaneler
Hafta_10/ → Modüller & Kütüphaneler (devam)
Hafta_11/ → Dosya İşlemleri
Hafta_12/ → Dosya İşlemleri & Genel Tekrar

README.md
```

---

## Haftalık Konu Notlarım

### Hafta 1 – 2 | Veri Tipleri & Değişkenler

İlk iki hafta Python'un temel yapı taşlarıyla başladık. Sözdizimi oldukça sade, tip belirtmeden direkt atama yapabiliyorsun.

```python
isim = "Feyat" # str
yas = 21 # int
ortalama = 3.75 # float
aktif = True # bool
```

**Tip dönüşümleri** ilk haftanın en çok kullandığım konusu oldu:

```python
girdi = input("Sayı gir: ") # her zaman str döner!
sayi = int(girdi) # str → int
print(type(sayi)) # <class 'int'>
```

**String metodları** — bunları not almadan geçemedim:

```python
metin = " yetgen python "
print(metin.strip()) # baştaki/sondaki boşlukları sil
print(metin.upper()) # BÜYÜK HARF
print(metin.replace("python", "jump"))
print(metin.split()) # listeye böl → ['yetgen', 'python']
```

> **Notum:** `input()` her zaman string döndürüyor — bunu ilk başta atlayıp sayısal işlemlerde hata yedim. Sayı alacaksan mutlaka `int()` veya `float()` ile sar.

---

### Hafta 3 – 4 | Döngüler & Koşullar

Programın mantık kurduğu yer burası. `if/elif/else` ve döngüleri kavramak kodun akışını anlamak demek.

```python
puan = int(input("Puanınızı girin: "))

if puan >= 90:
print("Mükemmel!")
elif puan >= 70:
print("İyi")
elif puan >= 50:
print("Geçer")
else:
print("Başarısız")
```

**for & while döngüleri:**

```python
# range(başlangıç, bitiş, adım)
for i in range(1, 11, 2):
print(i) # 1, 3, 5, 7, 9

# while — koşul sağlandıkça devam eder
sayac = 0
while sayac < 5:
print(f"{sayac}. tur")
sayac += 1
```

**break / continue — döngü kontrolü:**

```python
for i in range(10):
if i == 7:
break # döngüyü tamamen durdur
if i % 2 == 0:
continue # bu adımı atla
print(i) # 1, 3, 5
```

> **Notum:** `while True` ile sonsuz döngü + `break` kombinasyonu menü uygulamalarında çok işe yarıyor. Canlı derste hoca bu kalıbı gösterince "a, demek böyle yapılıyor" dedim. 

---

### Hafta 5 – 6 | Fonksiyonlar

Tekrar eden kodları fonksiyona almak hem okunabilirliği artırıyor hem de değişiklik yapmayı kolaylaştırıyor. Bu haftadan itibaren kod yazmak daha keyifli hale geldi.

```python
def bmi_hesapla(kilo, boy, birim="metrik"):
if birim == "metrik":
bmi = kilo / (boy ** 2)
else:
bmi = (kilo * 703) / (boy ** 2)
return round(bmi, 2)

print(bmi_hesapla(70, 1.75)) # 22.86
print(bmi_hesapla(154, 69, "ing")) # 22.75
```

**\*args — değişken sayıda parametre:**

```python
def toplam(*sayilar):
return sum(sayilar)

print(toplam(1, 2, 3, 4, 5)) # 15
```

**\*\*kwargs — anahtar kelimeli parametreler:**

```python
def profil(**bilgiler):
for anahtar, deger in bilgiler.items():
print(f"{anahtar}: {deger}")

profil(isim="Feyat", sehir="Ankara", program="Yetgen")
```

**Lambda — tek satır fonksiyon:**

```python
kare = lambda x: x ** 2
carpim = lambda x, y: x * y

print(kare(5)) # 25
print(carpim(3, 4)) # 12
```

> **Notum:** Lambda'yı `sorted()` ve `map()` ile birlikte kullanınca gerçek gücünü görüyorsun:
> ```python
> isimler = ["ali", "zeynep", "bora"]
> print(sorted(isimler, key=lambda x: len(x))) # uzunluğa göre sırala
> ```

---

### Hafta 7 – 8 | Nesne Yönelimli Programlama (OOP)

Bu bölüm programın en yoğun ve en zorlandığım kısmıydı. Ama mantığı oturduktan sonra her şey yerine oturdu.

```python
class Ogrenci:
kurum = "Yetgen" # sınıf değişkeni — herkeste ortak

def __init__(self, isim, brans):
self.isim = isim # nesne değişkeni
self.brans = brans

def tanitim(self):
return f"{self.isim} | {self.brans} | {self.kurum}"

def __str__(self):
return self.tanitim()


ogr1 = Ogrenci("Feyat", "Python")
print(ogr1) # Feyat | Python | Yetgen
```

**Miras (Inheritance) — bir sınıftan türetme:**

```python
class MezunOgrenci(Ogrenci):
def __init__(self, isim, brans, mezuniyet_yili):
super().__init__(isim, brans)
self.mezuniyet_yili = mezuniyet_yili

def tanitim(self):
return f"{super().tanitim()} | Mezun: {self.mezuniyet_yili}"

mezun = MezunOgrenci("Feyat", "Python", 2025)
print(mezun)
```

> **Notum:** `__init__` metodunu ve `self`'i kavramak OOP'un kilidi. `super()` ile üst sınıfın metodunu çağırmak da miras alırken hayat kurtarıyor.

---

### Hafta 9 – 10 | Modüller & Kütüphaneler

Python'un güçlü standart kütüphanesi bu haftanın konusuydu. Sıfırdan yazmak yerine hazır modülleri kullanmak işleri çok kolaylaştırıyor.

```python
import math
import random
import os
from datetime import datetime

# math
print(math.pi) # 3.14159...
print(math.sqrt(144)) # 12.0
print(math.ceil(4.2)) # 5 → yukarı yuvarla
print(math.floor(4.9)) # 4 → aşağı yuvarla

# random
print(random.randint(1, 6)) # zar at
print(random.choice(["elma", "armut", "muz"])) # rastgele seç
liste = [1, 2, 3, 4, 5]
random.shuffle(liste) # karıştır

# datetime
print(datetime.now().strftime("%d/%m/%Y %H:%M")) # 04/05/2025 14:30

# os
print(os.getcwd()) # çalışma dizini
print(os.listdir(".")) # mevcut klasördeki dosyalar
```

> **Notum:** `random.shuffle()` listeyi yerinde karıştırıyor, yeni liste döndürmüyor — bunu bilmeden `print(random.shuffle(liste))` yazdım, `None` çıktı. 

---

### Hafta 11 – 12 | Dosya İşlemleri & Genel Tekrar

Son iki hafta dosya okuma/yazma ve tüm konuların tekrarıyla kapandı. Dosya işlemleri gerçek projelerde çok sık lazım oluyor.

```python
# Dosyaya yazma
with open("notlar.txt", "w", encoding="utf-8") as f:
f.write("Yetgen Python Eğitimi\n")
f.write("12 Hafta | 2025\n")

# Dosyaya ekleme
with open("notlar.txt", "a", encoding="utf-8") as f:
f.write("Sertifika alındı! \n")

# Satır satır okuma
with open("notlar.txt", "r", encoding="utf-8") as f:
for satir in f:
print(satir.strip())
```

**CSV dosyası işleme:**

```python
import csv

# CSV yazma
with open("veriler.csv", "w", newline="", encoding="utf-8") as f:
yazar = csv.writer(f)
yazar.writerow(["İsim", "Puan", "Durum"])
yazar.writerow(["Feyat", 95, "Geçti"])

# CSV okuma
with open("veriler.csv", "r", encoding="utf-8") as f:
okuyucu = csv.reader(f)
for satir in okuyucu:
print(satir)
```

**Dosya modları özeti:**

| Mod | Ne yapar? |
|-----|-----------|
| `"r"` | Okuma — dosya yoksa hata verir |
| `"w"` | Yazma — varsa siler, yoksa oluşturur |
| `"a"` | Ekleme — varsa sonuna yazar |
| `"r+"` | Hem okuma hem yazma |

> **Notum:** `with` bloğu dosyayı otomatik kapatıyor. `f.close()` yazmana gerek kalmıyor, hata olsa bile dosya güvenle kapanıyor. Her zaman `with` kullan.

---

## 12 Hafta Sonunda Neler Öğrendim?

Yetgen Python programını tamamladığımda elimde şunlar vardı:

- Python sözdizimini ve temel yapılarını rahatça okuyup yazabilmek
- Kendi fonksiyonlarımı yazıp, OOP prensiplerine göre sınıf oluşturabilmek
- Standart kütüphaneyi etkin kullanmak
- Dosya okuma/yazma ile basit veri yönetimi yapabilmek
- Canlı derslerde hocayla birlikte anlık problem çözme deneyimi

Bu eğitim benim için ciddi bir sıçrama noktasıydı — reponun adı da oradan geliyor zaten: **Python Jump** 

---

## Kurulum

```bash
# Python sürümünü kontrol et
python --version # Python 3.x.x olmalı

# Repoyu klonla
git clone https://github.com/Feyat/Python_Jump.git
cd Python_Jump

# Herhangi bir dosyayı çalıştır
python hafta_01.py
```

---

## Bağlantılar

- [Yetgen Resmi Sitesi](https://www.yetgen.com)
- [Python Resmi Dokümantasyon](https://docs.python.org/tr/3/)

---

> 12 haftalık yoğun bir program — sertifikayı hak ettik! 
> Kodlarda hata veya önerin varsa PR açabilirsin, memnuniyetle bakarım.
