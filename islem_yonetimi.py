# ============================================================
# islem_yonetimi.py  –  Gelir/gider CRUD işlemleri
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol


def gelir_ekle(gelirler):
    """
    Kullanıcıdan tutar, tarih ve açıklama alarak yeni bir gelir kaydı oluşturur.
    Doğrulama geçilmezse kayıt yapılmaz ve kullanıcı bilgilendirilir.

    Args:
        gelirler (list): Mevcut gelir nesnelerinin tutulduğu liste
    """
    try:
        tutar = input("  Gelir tutarı (TL): ").strip()
        if not sayi_kontrol(tutar):
            print("  ⚠  Tutar sayısal bir değer olmalıdır.")
            return

        if float(tutar) <= 0:
            print("  ⚠  Tutar sıfırdan büyük olmalıdır.")
            return

        tarih = input("  Tarih (YYYY-MM-DD): ").strip()
        if not tarih_kontrol(tarih):
            print("  ⚠  Tarih formatı hatalı. Örnek: 2026-06-01")
            return

        aciklama = input("  Açıklama: ").strip()
        if not aciklama:
            aciklama = "Açıklama girilmedi"

        yeni_id = yeni_id_olustur(gelirler)
        yeni_gelir = Islem(yeni_id, float(tutar), tarih, aciklama, "gelir")
        gelirler.append(yeni_gelir)
        print(f"  ✅  Gelir kaydedildi  →  {yeni_gelir}")

    except Exception as hata:
        print("  ❌  Gelir eklenirken beklenmeyen hata:", hata)


def gider_ekle(giderler):
    """
    Kullanıcıdan tutar, tarih ve açıklama alarak yeni bir gider kaydı oluşturur.
    Doğrulama geçilmezse kayıt yapılmaz ve kullanıcı bilgilendirilir.

    Args:
        giderler (list): Mevcut gider nesnelerinin tutulduğu liste
    """
    try:
        tutar = input("  Gider tutarı (TL): ").strip()
        if not sayi_kontrol(tutar):
            print("  ⚠  Tutar sayısal bir değer olmalıdır.")
            return

        if float(tutar) <= 0:
            print("  ⚠  Tutar sıfırdan büyük olmalıdır.")
            return

        tarih = input("  Tarih (YYYY-MM-DD): ").strip()
        if not tarih_kontrol(tarih):
            print("  ⚠  Tarih formatı hatalı. Örnek: 2026-06-01")
            return

        aciklama = input("  Açıklama: ").strip()
        if not aciklama:
            aciklama = "Açıklama girilmedi"

        yeni_id = yeni_id_olustur(giderler)
        yeni_gider = Islem(yeni_id, float(tutar), tarih, aciklama, "gider")
        giderler.append(yeni_gider)
        print(f"  ✅  Gider kaydedildi  →  {yeni_gider}")

    except Exception as hata:
        print("  ❌  Gider eklenirken beklenmeyen hata:", hata)


def islemleri_listele(gelirler, giderler):
    """
    Tüm gelir ve gider kayıtlarını düzenli bir formatta konsola yazdırır.

    Args:
        gelirler (list): Gelir nesnelerinin listesi
        giderler (list): Gider nesnelerinin listesi
    """
    try:
        if not gelirler and not giderler:
            print("  ℹ  Henüz kayıtlı işlem bulunmuyor.")
            return

        print("\n  ─── GELİRLER ───")
        if not gelirler:
            print("  Gelir kaydı yok.")
        else:
            for gelir in gelirler:
                print(" ", gelir)

        print("\n  ─── GİDERLER ───")
        if not giderler:
            print("  Gider kaydı yok.")
        else:
            for gider in giderler:
                print(" ", gider)

    except Exception as hata:
        print("  ❌  Listeleme sırasında hata oluştu:", hata)


def islem_sil(gelirler, giderler, id):
    """
    Verilen ID'ye sahip işlemi gelir veya gider listesinden kaldırır.

    Args:
        gelirler (list): Gelir nesnelerinin listesi
        giderler (list): Gider nesnelerinin listesi
        id       (str|int): Silinecek işlemin ID değeri
    """
    try:
        silinecek_id = int(id)

        for islem in gelirler:
            if islem.id == silinecek_id:
                gelirler.remove(islem)
                print(f"  ✅  ID {silinecek_id} numaralı gelir kaydı silindi.")
                return

        for islem in giderler:
            if islem.id == silinecek_id:
                giderler.remove(islem)
                print(f"  ✅  ID {silinecek_id} numaralı gider kaydı silindi.")
                return

        print(f"  ⚠  ID {silinecek_id} bulunamadı.")

    except ValueError:
        print("  ⚠  ID sayısal olmalıdır.")
    except Exception as hata:
        print("  ❌  Silme işleminde beklenmeyen hata:", hata)
