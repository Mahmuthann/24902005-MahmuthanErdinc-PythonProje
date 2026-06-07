# ============================================================
# analiz.py  –  Pandas & NumPy analizleri
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

import pandas as pd
import numpy as np


def verileri_dataframe_yap(gelirler, giderler):
    """
    Gelir ve gider listelerini birleştirerek temiz bir pandas DataFrame oluşturur.
    tarih sütunu datetime'a, tutar sütunu float'a dönüştürülür.
    Dönüştürülemeyen satırlar çıkarılır.

    Args:
        gelirler (list): Gelir nesnelerinin listesi
        giderler (list): Gider nesnelerinin listesi

    Returns:
        pd.DataFrame: Birleştirilmiş ve temizlenmiş veri tablosu
    """
    try:
        tum_islemler = gelirler + giderler
        if not tum_islemler:
            return pd.DataFrame()

        veriler = [islem.to_dict() for islem in tum_islemler]
        df = pd.DataFrame(veriler)

        df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
        df["tutar"] = pd.to_numeric(df["tutar"], errors="coerce")
        df = df.dropna(subset=["tarih", "tutar"])
        df = df.reset_index(drop=True)
        return df

    except Exception as hata:
        print("  ❌  DataFrame oluşturulurken hata:", hata)
        return pd.DataFrame()


def toplam_gelir_gider(df):
    """
    DataFrame üzerinden toplam gelir, toplam gider ve net bakiyeyi hesaplar.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo

    Returns:
        dict: {'toplam_gelir': float, 'toplam_gider': float, 'bakiye': float}
    """
    try:
        if df.empty:
            return {"toplam_gelir": 0.0, "toplam_gider": 0.0, "bakiye": 0.0}

        toplam_gelir = df[df["tip"] == "gelir"]["tutar"].sum()
        toplam_gider = df[df["tip"] == "gider"]["tutar"].sum()
        bakiye = toplam_gelir - toplam_gider

        return {
            "toplam_gelir": float(toplam_gelir),
            "toplam_gider": float(toplam_gider),
            "bakiye": float(bakiye),
        }
    except Exception as hata:
        print("  ❌  Toplam hesaplanırken hata:", hata)
        return {"toplam_gelir": 0.0, "toplam_gider": 0.0, "bakiye": 0.0}


def aylik_analiz(df):
    """
    İşlemleri ay bazında gruplayarak gelir, gider ve bakiye sütunlarını içeren
    pivot tablo oluşturur.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo

    Returns:
        pd.DataFrame: Aylık özet tablo (ay, gelir, gider, bakiye)
    """
    try:
        if df.empty:
            return pd.DataFrame()

        kopya = df.copy()
        kopya["ay"] = kopya["tarih"].dt.to_period("M").astype(str)

        aylik = kopya.pivot_table(
            values="tutar",
            index="ay",
            columns="tip",
            aggfunc="sum",
            fill_value=0,
        )

        # Sütunlar eksik olabilir (sadece gelir veya sadece gider varsa)
        if "gelir" not in aylik.columns:
            aylik["gelir"] = 0.0
        if "gider" not in aylik.columns:
            aylik["gider"] = 0.0

        aylik["bakiye"] = aylik["gelir"] - aylik["gider"]
        aylik.columns.name = None  # pivot başlığını temizle
        return aylik

    except Exception as hata:
        print("  ❌  Aylık analiz sırasında hata:", hata)
        return pd.DataFrame()


def numpy_istatistik(df):
    """
    NumPy kullanarak tüm tutar değerleri üzerinde temel istatistikleri hesaplar.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo

    Returns:
        dict: ortalama, minimum, maksimum, standart_sapma (hepsi float)
    """
    bos = {"ortalama": 0.0, "minimum": 0.0, "maksimum": 0.0, "standart_sapma": 0.0}
    try:
        if df.empty:
            return bos

        tutarlar = df["tutar"].to_numpy(dtype=float)
        return {
            "ortalama": float(np.mean(tutarlar)),
            "minimum": float(np.min(tutarlar)),
            "maksimum": float(np.max(tutarlar)),
            "standart_sapma": float(np.std(tutarlar)),
        }
    except Exception as hata:
        print("  ❌  NumPy istatistik hesaplanırken hata:", hata)
        return bos
