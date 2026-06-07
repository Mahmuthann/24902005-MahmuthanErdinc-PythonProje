# 💰 Kişisel Finans ve Harcama Takip Sistemi

> **BGY210 – Python Programlama II | Bahar Dönemi Final Projesi**

Bu proje; gelir ve gider kayıtlarının tutulmasını, CSV dosyasına kaydedilmesini, Pandas/NumPy ile analiz edilmesini ve Matplotlib/Seaborn kullanılarak grafiklerle görselleştirilmesini sağlayan kişisel finans takip uygulamasıdır.

---

## 👤 Öğrenci Bilgileri

| Alan | Bilgi |
|---|---|
| **Ad Soyad** | Mahmuthan Erdinç |
| **Öğrenci No** | 24902005 |
| **Bölüm** | Yönetim Bilişim Sistemleri |
| **Ders** | BGY210 – Python Programlama II |
| **Öğretim Elemanı** | Dr. Öğr. Üyesi Tohid YOUSEFİ |
| **GitHub Repo** | `24902005-MahmuthanErdinc-PythonProje` |
| **Repo Linki** | `https://github.com/Mahmuthann/24902005-MahmuthanErdinc-PythonProje` |

> Not: GitHub reposu public olarak ayarlanmıştır.jyputer nootebooktan markdownlarla güzel şekilde açıklanmıstır.

---

## 🎯 Projenin Amacı

Bu projede amaç, Python Programlama II dersinde öğrenilen temel ve ileri düzey konuları gerçek bir uygulama üzerinde kullanmaktır.

Kişisel finans takibi, günlük hayatta kullanılabilecek pratik bir konu olduğu için seçilmiştir. Uygulama sayesinde kullanıcı gelir ve gider kayıtlarını tutabilir, bu kayıtları dosyaya kaydedebilir, finansal durumunu analiz edebilir ve sonuçları grafikler üzerinden inceleyebilir. İnsani olarak ihtiyac duyduğumuz sistemdi ve umarım işinize yarar.

Projede özellikle şu konular uygulanmıştır:

- Nesne yönelimli programlama
- Modüler Python dosya yapısı
- CSV dosya okuma ve yazma
- Pandas ile veri analizi
- NumPy ile istatistiksel hesaplama
- Matplotlib ve Seaborn ile grafik oluşturma
- Jupyter Notebook üzerinde açıklamalı çalışma
- ipywidgets ile interaktif notebook arayüzü
- Hata kontrolü ve kullanıcı girişi doğrulama

---

## 🗂️ Proje Dosya Yapısı

```text
Mahmuthan_Erdinc_24902005_YBS/
├── main.py                  # Konsol uygulaması giriş noktası
├── main.ipynb               # Açıklamalı Jupyter Notebook dosyası
├── finans_modeli.py         # Islem sınıfı
├── islem_yonetimi.py        # Gelir/gider ekleme, listeleme ve silme fonksiyonları
├── dosya_islemleri.py       # CSV okuma ve yazma işlemleri
├── analiz.py                # Pandas ve NumPy analiz fonksiyonları
├── gorsellestirme.py        # Grafik oluşturma fonksiyonları
├── utils.py                 # Yardımcı fonksiyonlar
├── requirements.txt         # Gerekli Python kütüphaneleri
├── veriler.csv              # Örnek gelir-gider verileri
├── screenshots/             # Notebook ekran görüntüleri
└── grafikler/               # Oluşturulan grafik dosyaları
```

![Proje dosya yapısı](screenshots/ss01.png)

---

## ⚙️ Kurulum

Projeyi çalıştırmadan önce gerekli kütüphaneler yüklenmelidir.

```bash
pip install -r requirements.txt
```

`requirements.txt` içinde kullanılan temel kütüphaneler:

```text
pandas
numpy
matplotlib
seaborn
ipywidgets
```

Jupyter Notebook bilgisayarda kurulu değilse ayrıca şu komut kullanılabilir:

```bash
pip install notebook
```

---

## ▶️ Çalıştırma

### 1. Konsol Uygulaması Olarak Çalıştırma

```bash
python main.py
```

Konsol uygulaması üzerinden:

- Gelir ekleme
- Gider ekleme
- İşlemleri listeleme
- Finansal analiz yapma
- Grafik oluşturma
- CSV dosyasına kaydetme

işlemleri yapılabilir.

---

### 2. Jupyter Notebook Üzerinden Çalıştırma

```bash
jupyter notebook main.ipynb
```

Notebook dosyası, projenin açıklamalı halidir. Kodlar adım adım çalıştırılabilir ve ekran görüntüleriyle desteklenmiştir.

Notebook içinde ayrıca `ipywidgets` kullanılarak interaktif bir menü arayüzü oluşturulmuştur.

![ipywidgets arayüzü](screenshots/ss15.png)

---

## 🧱 Kullanılan Modüller

| Dosya | Açıklama |
|---|---|
| `finans_modeli.py` | Gelir ve gider kayıtları için kullanılan `Islem` sınıfını içerir. |
| `islem_yonetimi.py` | Gelir ekleme, gider ekleme, işlem listeleme ve işlem silme fonksiyonlarını içerir. |
| `dosya_islemleri.py` | Verilerin CSV dosyasından okunmasını ve CSV dosyasına kaydedilmesini sağlar. |
| `analiz.py` | Gelir-gider verilerini DataFrame’e dönüştürür, toplamları ve istatistikleri hesaplar. |
| `gorsellestirme.py` | Aylık grafik, bar grafik ve pasta grafik oluşturur. |
| `utils.py` | ID üretme, tarih kontrolü, sayı kontrolü ve menü gösterme gibi yardımcı işlemleri içerir. |
| `main.py` | Konsol uygulamasının ana çalışma dosyasıdır. |
| `main.ipynb` | Projenin açıklamalı ve görsel destekli notebook sürümüdür. |

---

## 🧩 Nesne Yönelimli Programlama Yapısı

Projede gelir ve gider kayıtları `Islem` sınıfı ile temsil edilmektedir.

Her işlem nesnesinde şu bilgiler tutulur:

| Özellik | Açıklama |
|---|---|
| `id` | İşlem numarası |
| `tutar` | İşlem tutarı |
| `tarih` | İşlem tarihi |
| `aciklama` | İşlem açıklaması |
| `tip` | Gelir veya gider bilgisi |

Örnek veri yapısı:

```python
gelirler = []
giderler = []
```

Bu listelerin içinde `Islem` sınıfından oluşturulmuş nesneler tutulur.

![Kullanılan veri yapıları](screenshots/ss02.png)

---

## 💾 CSV Dosya İşlemleri

Projedeki veriler `veriler.csv` dosyasında saklanır.

CSV dosyasında şu alanlar bulunur:

```text
id,tutar,tarih,aciklama,tip
```

Program başlatıldığında CSV dosyası otomatik okunur. Yeni gelir veya gider kayıtları eklendikten sonra CSV dosyasına tekrar kaydedilebilir.

![CSV dosyasından veri okuma](screenshots/ss04.png)

CSV kaydetme işlemi:

![CSV kaydetme](screenshots/ss14.png)

---

## 📋 İşlemleri Listeleme

Gelir ve gider kayıtları ayrı başlıklar altında listelenir. Bu sayede kullanıcı mevcut finansal hareketlerini düzenli şekilde görebilir.

![İşlemleri listeleme](screenshots/ss05.png)

---

## ➕ Manuel Kayıt Ekleme

Notebook içinde örnek olarak doğrudan `Islem` nesnesi oluşturularak kayıt ekleme gösterilmiştir. Bu bölüm, OOP yapısının çalıştığını göstermek için eklenmiştir.

![Manuel kayıt ekleme](screenshots/ss06.png)

---

## 📊 Pandas ile Veri Analizi

Gelir ve gider listeleri Pandas DataFrame yapısına dönüştürülür.

Bu aşamada:

- Gelirler ve giderler tek tabloda birleştirilir.
- Tarih sütunu datetime formatına çevrilir.
- Tutar sütunu sayısal veri olarak analiz edilir.
- Finansal analiz için düzenli bir tablo elde edilir.

![Pandas DataFrame](screenshots/ss07.png)

---

## 💵 Toplam Gelir, Gider ve Net Bakiye

`toplam_gelir_gider()` fonksiyonu ile:

- Toplam gelir
- Toplam gider
- Net bakiye

hesaplanır.

Net bakiye şu formülle elde edilir:

```text
Net Bakiye = Toplam Gelir - Toplam Gider
```

![Toplam gelir gider analizi](screenshots/ss08.png)

---

## 📅 Aylık Analiz

Aylık analiz bölümünde Pandas `pivot_table` kullanılmıştır.

Bu analiz sayesinde her ay için:

- Toplam gelir
- Toplam gider
- Aylık bakiye

hesaplanır.

![Aylık analiz](screenshots/ss09.png)

---

## 🔢 NumPy İstatistikleri

`numpy_istatistik()` fonksiyonu tüm işlem tutarları üzerinden temel istatistiksel hesaplamalar yapar.

Hesaplanan değerler:

- Ortalama
- Minimum
- Maksimum
- Standart sapma

![NumPy istatistikleri](screenshots/ss10.png)

---

## 📈 Grafikler

Projede üç farklı grafik oluşturulmuştur. Grafikler hem notebook içinde gösterilir hem de `grafikler/` klasörüne PNG dosyası olarak kaydedilir.

---

### 1. Aylık Gelir-Gider Karşılaştırması

Aylara göre gelir ve gider değişimini çizgi grafik olarak gösterir.

![Aylık gelir gider grafiği](screenshots/ss11.png)

Oluşturulan grafik dosyası:

![Aylık grafik](grafikler/aylik_grafik.png)

---

### 2. Toplam Gelir-Gider Bar Grafiği

Toplam gelir ve toplam gideri karşılaştırmalı olarak gösterir.

![Bar grafik ekran görüntüsü](screenshots/ss12.png)

Oluşturulan grafik dosyası:

![Gelir gider bar grafiği](grafikler/gelir_gider_bar.png)

---

### 3. Gelir-Gider Oranları Pasta Grafiği

Gelir ve giderlerin toplam içindeki oranını donut pasta grafik olarak gösterir.

![Pasta grafik ekran görüntüsü](screenshots/ss13.png)

Oluşturulan grafik dosyası:

![Pasta grafik](grafikler/pasta_grafik.png)

---

## 🖥️ Jupyter Notebook Arayüzü

Notebook içinde `ipywidgets` kullanılarak interaktif bir arayüz oluşturulmuştur.

Bu arayüz üzerinden:

- Gelir ekleme
- Gider ekleme
- İşlemleri listeleme
- Analiz yapma
- Grafik gösterme
- CSV kaydetme
- İşlem silme

işlemleri yapılabilir.

Bu yapı özellikle Jupyter Notebook ortamında `input()` kullanımının pratik olmaması nedeniyle tercih edilmiştir.

![Jupyter widget arayüzü](screenshots/ss15.png)

---

## ✅ Ödev Kriterleriyle Eşleşen Bölümler

| Kriter | Projedeki Karşılığı |
|---|---|
| OOP kullanımı | `Islem` sınıfı |
| Modüler yapı | Kodların farklı `.py` dosyalarına ayrılması |
| Dosya işlemleri | `veriler.csv` okuma ve yazma |
| Veri analizi | Pandas DataFrame ve pivot table |
| NumPy kullanımı | Ortalama, minimum, maksimum, standart sapma |
| Görselleştirme | Matplotlib ve Seaborn grafikleri |
| Notebook kullanımı | `main.ipynb` dosyası |
| Kullanıcı etkileşimi | Konsol menüsü ve ipywidgets arayüzü |
| Hata kontrolü | Tarih, sayı ve dosya okuma/yazma kontrolleri |
| GitHub teslimi | Private repo ve collaborator ayarı |

---

## 🧪 Örnek Veri Seti

Projede başlangıç için örnek gelir ve gider kayıtları bulunmaktadır.

Örnek gelirler:

- Maaş
- Ek gelir
- Freelance iş
- Proje ödemesi
- Danışmanlık ücreti

Örnek giderler:

- Kira
- Market
- Ulaşım
- Fatura
- Alışveriş
- Abonelikler
- Yemek & Kafe
- Giyim

Bu veriler `veriler.csv` dosyası içinde tutulmaktadır.

---

## 🔍 Proje Akışı

Projenin genel çalışma mantığı şu şekildedir:

```text
1. Program başlar.
2. veriler.csv dosyasındaki kayıtlar okunur.
3. Gelir ve gider kayıtları ayrı listelerde tutulur.
4. Kullanıcı menüden işlem seçer.
5. Yeni kayıt eklenebilir veya mevcut kayıtlar listelenebilir.
6. Pandas ve NumPy ile analiz yapılabilir.
7. Grafikler oluşturulabilir.
8. Güncel veriler tekrar CSV dosyasına kaydedilir.
```

---

## 📌 Sonuç

Bu proje ile Python Programlama II dersi kapsamında öğrenilen birçok konu tek bir uygulamada birleştirilmiştir derste gördükleirmi uygyulayıp gelişmeye çalıstım .

Kişisel finans takip sistemi sayesinde kullanıcı gelir ve giderlerini kaydedebilir, verilerini CSV dosyasında saklayabilir, finansal durumunu analiz edebilir ve sonuçları grafiklerle inceleyebilir.

Proje hem konsol uygulaması hem de Jupyter Notebook arayüzü ile çalışabilecek şekilde hazırlanmıştır  öncelik olarak jupyteri öneririm .

---

## 📎 Teslim Notu

- Proje klasörü: `Mahmuthan_Erdinc_24902005_YBS`
- Ana notebook dosyası: `main.ipynb`
- Konsol uygulaması: `main.py`
- Veri dosyası: `veriler.csv`
- Grafik çıktıları: `grafikler/`
- Ekran görüntüleri: `screenshots/`
- GitHub repo: 

```text
Hazırlayan: Mahmuthan Erdinç
Öğrenci No: 24902005
Bölüm: Yönetim Bilişim Sistemleri
Ders: BGY210 – Python Programlama II
```

