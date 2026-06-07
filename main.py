# ============================================================
# main.py  –  Konsol uygulaması giriş noktası
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

from islem_yonetimi import gelir_ekle, gider_ekle, islemleri_listele, islem_sil
from dosya_islemleri import csv_kaydet, csv_oku
from analiz import verileri_dataframe_yap, toplam_gelir_gider, aylik_analiz, numpy_istatistik
from gorsellestirme import aylik_grafik, gelir_gider_bar, pasta_grafik
from utils import menu_goster

VERI_DOSYASI = "veriler.csv"


def analiz_yap(gelirler, giderler):
    """
    Mevcut verileri DataFrame'e dönüştürüp toplam, aylık ve NumPy istatistiklerini ekrana yazdırır.

    Args:
        gelirler (list): Gelir nesnelerinin listesi
        giderler (list): Gider nesnelerinin listesi
    """
    df = verileri_dataframe_yap(gelirler, giderler)
    if df.empty:
        print("  ℹ  Analiz için kayıtlı veri yok.")
        return

    print("\n  ══ TOPLAM GELİR / GİDER ══")
    toplamlar = toplam_gelir_gider(df)
    print(f"  Toplam Gelir  : {toplamlar['toplam_gelir']:>12,.2f} ₺")
    print(f"  Toplam Gider  : {toplamlar['toplam_gider']:>12,.2f} ₺")
    bakiye = toplamlar["bakiye"]
    isaret = "+" if bakiye >= 0 else ""
    print(f"  Net Bakiye    : {isaret}{bakiye:>11,.2f} ₺")

    print("\n  ══ AYLIK ANALİZ ══")
    aylik = aylik_analiz(df)
    print(aylik.to_string())

    print("\n  ══ NUMPY İSTATİSTİKLERİ (tüm işlemler) ══")
    ist = numpy_istatistik(df)
    print(f"  Ortalama      : {ist['ortalama']:>10,.2f} ₺")
    print(f"  Minimum       : {ist['minimum']:>10,.2f} ₺")
    print(f"  Maksimum      : {ist['maksimum']:>10,.2f} ₺")
    print(f"  Standart Sapma: {ist['standart_sapma']:>10,.2f} ₺")


def grafik_goster(gelirler, giderler):
    """
    Tüm grafik fonksiyonlarını sırayla çalıştırır.

    Args:
        gelirler (list): Gelir nesnelerinin listesi
        giderler (list): Gider nesnelerinin listesi
    """
    df = verileri_dataframe_yap(gelirler, giderler)
    if df.empty:
        print("  ℹ  Grafik için kayıtlı veri yok.")
        return

    aylik_grafik(df)
    gelir_gider_bar(df)
    pasta_grafik(df)


def main():
    """
    Programın ana döngüsü; menüyü gösterip kullanıcı seçimine göre ilgili fonksiyonu çağırır.
    Başlangıçta CSV dosyası otomatik olarak yüklenir.
    """
    print("\n  Hoş geldiniz! Veriler yükleniyor...")
    gelirler, giderler = csv_oku(VERI_DOSYASI)

    while True:
        try:
            menu_goster()
            secim = input("  Seçiminiz (1-7): ").strip()

            if secim == "1":
                gelir_ekle(gelirler)

            elif secim == "2":
                gider_ekle(giderler)

            elif secim == "3":
                islemleri_listele(gelirler, giderler)

            elif secim == "4":
                analiz_yap(gelirler, giderler)

            elif secim == "5":
                grafik_goster(gelirler, giderler)

            elif secim == "6":
                csv_kaydet(VERI_DOSYASI, gelirler, giderler)

            elif secim == "7":
                csv_kaydet(VERI_DOSYASI, gelirler, giderler)
                print("\n  İyi günler! Veriler kaydedildi, program kapanıyor.\n")
                break

            else:
                print("  ⚠  Lütfen 1 ile 7 arasında bir seçim yapın.")

        except KeyboardInterrupt:
            print("\n\n  Program kullanıcı tarafından sonlandırıldı.")
            csv_kaydet(VERI_DOSYASI, gelirler, giderler)
            break
        except Exception as hata:
            print("  ❌  Beklenmeyen hata:", hata)


if __name__ == "__main__":
    main()
