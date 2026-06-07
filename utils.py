# ============================================================
# utils.py  –  Yardımcı fonksiyonlar
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

from datetime import datetime


def yeni_id_olustur(liste):
    """
    Verilen listedeki en büyük ID değerini bulup 1 artırarak yeni ID üretir.
    Liste boşsa 1 döndürür.

    Args:
        liste (list): Islem nesnelerinden oluşan liste

    Returns:
        int: Kullanılabilecek yeni benzersiz ID
    """
    if not liste:
        return 1
    return max(islem.id for islem in liste) + 1


def tarih_kontrol(tarih):
    """
    Tarihin YYYY-MM-DD formatına uygun olup olmadığını kontrol eder.

    Args:
        tarih (str): Kontrol edilecek tarih string'i

    Returns:
        bool: Format doğruysa True, yanlışsa False
    """
    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def sayi_kontrol(deger):
    """
    Girilen string değerinin float'a dönüştürülüp dönüştürülemeyeceğini kontrol eder.

    Args:
        deger (str): Kullanıcıdan alınan değer

    Returns:
        bool: Sayıya çevrilebiliyorsa True, aksi halde False
    """
    try:
        float(deger)
        return True
    except ValueError:
        return False


def menu_goster():
    """Programın ana menüsünü konsola yazdırır."""
    print("\n" + "═" * 38)
    print("   💰  KİŞİSEL FİNANS TAKİP SİSTEMİ  💰")
    print("═" * 38)
    print("  1.  Gelir Ekle")
    print("  2.  Gider Ekle")
    print("  3.  İşlemleri Listele")
    print("  4.  Analiz Yap")
    print("  5.  Grafik Göster")
    print("  6.  CSV Kaydet")
    print("  7.  Çıkış")
    print("═" * 38)
