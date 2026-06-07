# ============================================================
# finans_modeli.py  –  İşlem sınıfı (OOP)
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================


class Islem:
    """
    Bir gelir veya gider kaydını temsil eden sınıf.

    Özellikler (attributes):
        id       (int)   – Benzersiz kayıt numarası
        tutar    (float) – İşlem tutarı (TL)
        tarih    (str)   – İşlem tarihi  (YYYY-MM-DD)
        aciklama (str)   – Kısa açıklama
        tip      (str)   – 'gelir' veya 'gider'
    """

    def __init__(self, id, tutar, tarih, aciklama, tip):
        """Yeni bir Islem nesnesi oluşturur; tutar ve id uygun tiplere dönüştürülür."""
        self.id = int(id)
        self.tutar = float(tutar)
        self.tarih = tarih
        self.aciklama = aciklama
        self.tip = tip  # 'gelir' veya 'gider'

    def __str__(self):
        """İşlemi konsola okunabilir biçimde yazdırır."""
        return (
            f"[{self.id:>3}] {self.tip.upper():<6} | "
            f"{self.tarih} | {self.tutar:>10.2f} TL | {self.aciklama}"
        )

    def to_dict(self):
        """CSV kaydı ve DataFrame dönüşümü için sözlük döndürür."""
        return {
            "id": self.id,
            "tutar": self.tutar,
            "tarih": self.tarih,
            "aciklama": self.aciklama,
            "tip": self.tip,
        }
