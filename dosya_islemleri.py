# ============================================================
# dosya_islemleri.py  –  CSV okuma / yazma
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

import csv
from finans_modeli import Islem

CSV_ALANLARI = ["id", "tutar", "tarih", "aciklama", "tip"]


def csv_kaydet(dosya_adi, gelirler, giderler):
    """
    Tüm gelir ve gider nesnelerini belirtilen CSV dosyasına yazar.
    Mevcut dosyanın üzerine yazar.

    Args:
        dosya_adi (str): Kaydedilecek CSV dosyasının adı/yolu
        gelirler  (list): Gelir nesnelerinin listesi
        giderler  (list): Gider nesnelerinin listesi
    """
    try:
        tum_islemler = gelirler + giderler
        with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:
            yazici = csv.DictWriter(dosya, fieldnames=CSV_ALANLARI)
            yazici.writeheader()
            for islem in tum_islemler:
                yazici.writerow(islem.to_dict())
        print(f"  ✅  {len(tum_islemler)} kayıt '{dosya_adi}' dosyasına kaydedildi.")
    except PermissionError:
        print(f"  ❌  '{dosya_adi}' dosyasına yazma izni yok.")
    except Exception as hata:
        print("  ❌  CSV kaydetme sırasında hata oluştu:", hata)


def csv_oku(dosya_adi):
    """
    Belirtilen CSV dosyasını okuyarak Islem nesnelerini gelir/gider listelerine dağıtır.
    Dosya bulunamazsa uyarı verir ve boş listelerle devam edilir.

    Args:
        dosya_adi (str): Okunacak CSV dosyasının adı/yolu

    Returns:
        tuple: (gelirler listesi, giderler listesi)
    """
    gelirler = []
    giderler = []

    try:
        with open(dosya_adi, "r", newline="", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)
            for i, satir in enumerate(okuyucu, start=1):
                try:
                    islem = Islem(
                        satir["id"],
                        satir["tutar"],
                        satir["tarih"],
                        satir["aciklama"],
                        satir["tip"],
                    )
                    if islem.tip == "gelir":
                        gelirler.append(islem)
                    elif islem.tip == "gider":
                        giderler.append(islem)
                    else:
                        print(f"  ⚠  Satır {i}: bilinmeyen tip '{islem.tip}', atlandı.")
                except Exception:
                    print(f"  ⚠  Satır {i} okunamadı, atlandı.")

        print(f"  ✅  '{dosya_adi}' dosyasından {len(gelirler)} gelir, {len(giderler)} gider yüklendi.")

    except FileNotFoundError:
        print(f"  ℹ  '{dosya_adi}' bulunamadı. Boş listelerle başlanıyor.")
    except Exception as hata:
        print("  ❌  CSV okuma sırasında hata oluştu:", hata)

    return gelirler, giderler
