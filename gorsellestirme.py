# ============================================================
# gorsellestirme.py  –  Matplotlib / Seaborn grafikleri
# BGY210 Python Programlama-II  |  Mahmuthan Erdinç  |  24902005
# ============================================================

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from analiz import toplam_gelir_gider, aylik_analiz

# Grafiklerde tutarlı renk paleti
RENK_GELIR = "#2ecc71"   # Yeşil
RENK_GIDER = "#e74c3c"   # Kırmızı
RENK_BAKIYE = "#3498db"  # Mavi
GRAFIK_KLASORU = "grafikler"

# Seaborn tarzını etkinleştir
sns.set_theme(style="whitegrid", palette="pastel")


def _klasor_hazirla():
    """Grafik klasörü yoksa oluşturur."""
    if not os.path.exists(GRAFIK_KLASORU):
        os.makedirs(GRAFIK_KLASORU)


def aylik_grafik(df):
    """
    Aylık gelir ve gider değerlerini karşılaştıran çizgi + alan grafiği oluşturur.
    Grafik hem ekranda gösterilir hem de 'grafikler/aylik_grafik.png' olarak kaydedilir.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo
    """
    try:
        if df.empty:
            print("  ℹ  Aylık grafik için veri yok.")
            return

        aylik = aylik_analiz(df)
        if aylik.empty:
            print("  ℹ  Aylık grafik için yeterli veri yok.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))

        aylar = aylik.index.tolist()
        gelir_deger = aylik["gelir"].tolist()
        gider_deger = aylik["gider"].tolist()

        ax.plot(aylar, gelir_deger, marker="o", linewidth=2.5,
                color=RENK_GELIR, label="Gelir", zorder=3)
        ax.fill_between(aylar, gelir_deger, alpha=0.15, color=RENK_GELIR)

        ax.plot(aylar, gider_deger, marker="s", linewidth=2.5,
                color=RENK_GIDER, label="Gider", zorder=3)
        ax.fill_between(aylar, gider_deger, alpha=0.15, color=RENK_GIDER)

        # Nokta değerlerini göster
        for x, y in enumerate(gelir_deger):
            ax.annotate(f"{y:,.0f}", (aylar[x], y),
                        textcoords="offset points", xytext=(0, 8),
                        ha="center", fontsize=9, color=RENK_GELIR, fontweight="bold")
        for x, y in enumerate(gider_deger):
            ax.annotate(f"{y:,.0f}", (aylar[x], y),
                        textcoords="offset points", xytext=(0, -16),
                        ha="center", fontsize=9, color=RENK_GIDER, fontweight="bold")

        ax.set_title("Aylık Gelir & Gider Karşılaştırması", fontsize=14, fontweight="bold", pad=15)
        ax.set_xlabel("Ay", fontsize=11)
        ax.set_ylabel("Tutar (TL)", fontsize=11)
        ax.legend(fontsize=10)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, _: f"{val:,.0f} ₺"))
        plt.tight_layout()

        _klasor_hazirla()
        kayit_yolu = os.path.join(GRAFIK_KLASORU, "aylik_grafik.png")
        plt.savefig(kayit_yolu, dpi=150, bbox_inches="tight")
        plt.show()
        print(f"  ✅  Aylık grafik kaydedildi → {kayit_yolu}")

    except Exception as hata:
        print("  ❌  Aylık grafik oluşturulurken hata:", hata)


def gelir_gider_bar(df):
    """
    Toplam gelir ve toplam gideri yan yana gösteren renkli sütun grafiği oluşturur.
    'grafikler/gelir_gider_bar.png' olarak kaydedilir.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo
    """
    try:
        if df.empty:
            print("  ℹ  Bar grafik için veri yok.")
            return

        toplamlar = toplam_gelir_gider(df)
        etiketler = ["Gelir", "Gider"]
        degerler = [toplamlar["toplam_gelir"], toplamlar["toplam_gider"]]
        renkler = [RENK_GELIR, RENK_GIDER]

        fig, ax = plt.subplots(figsize=(7, 5))
        cubuklar = ax.bar(etiketler, degerler, color=renkler,
                          width=0.45, edgecolor="white", linewidth=1.5)

        # Her çubuğun üstüne değeri yaz
        for cubuk, deger in zip(cubuklar, degerler):
            ax.text(
                cubuk.get_x() + cubuk.get_width() / 2,
                cubuk.get_height() + max(degerler) * 0.015,
                f"{deger:,.2f} ₺",
                ha="center", va="bottom", fontsize=11, fontweight="bold"
            )

        # Bakiye bilgisi
        bakiye = toplamlar["bakiye"]
        bakiye_renk = RENK_BAKIYE if bakiye >= 0 else RENK_GIDER
        ax.set_title(
            f"Toplam Gelir & Gider  |  Net Bakiye: {bakiye:+,.2f} ₺",
            fontsize=13, fontweight="bold", color=bakiye_renk, pad=12
        )
        ax.set_ylabel("Tutar (TL)", fontsize=11)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, _: f"{val:,.0f} ₺"))
        ax.set_ylim(0, max(degerler) * 1.18)
        sns.despine()
        plt.tight_layout()

        _klasor_hazirla()
        kayit_yolu = os.path.join(GRAFIK_KLASORU, "gelir_gider_bar.png")
        plt.savefig(kayit_yolu, dpi=150, bbox_inches="tight")
        plt.show()
        print(f"  ✅  Bar grafik kaydedildi → {kayit_yolu}")

    except Exception as hata:
        print("  ❌  Bar grafik oluşturulurken hata:", hata)


def pasta_grafik(df):
    """
    Gelir ve gider oranlarını donut tarzında pasta grafiğiyle gösterir.
    'grafikler/pasta_grafik.png' olarak kaydedilir.

    Args:
        df (pd.DataFrame): verileri_dataframe_yap ile elde edilen tablo
    """
    try:
        if df.empty:
            print("  ℹ  Pasta grafik için veri yok.")
            return

        toplamlar = toplam_gelir_gider(df)
        degerler = [toplamlar["toplam_gelir"], toplamlar["toplam_gider"]]

        if sum(degerler) == 0:
            print("  ℹ  Pasta grafiği için yeterli veri yok.")
            return

        etiketler = ["Gelir", "Gider"]
        renkler = [RENK_GELIR, RENK_GIDER]
        patlama = (0.04, 0.04)  # Dilimler hafif ayrık

        fig, ax = plt.subplots(figsize=(7, 6))
        wedges, texts, autotexts = ax.pie(
            degerler,
            labels=None,
            colors=renkler,
            autopct="%1.1f%%",
            startangle=90,
            explode=patlama,
            wedgeprops={"edgecolor": "white", "linewidth": 2},
            pctdistance=0.75,
        )

        # Donut efekti – ortaya beyaz daire
        merkez_cember = plt.Circle((0, 0), 0.45, color="white")
        ax.add_patch(merkez_cember)

        # Stilize yüzde yazıları
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_fontweight("bold")
            autotext.set_color("white")

        # Tutarları legend'a ekle
        legend_etiketleri = [
            f"Gelir  –  {toplamlar['toplam_gelir']:,.2f} ₺",
            f"Gider  –  {toplamlar['toplam_gider']:,.2f} ₺",
        ]
        legend_parcalar = [
            mpatches.Patch(color=RENK_GELIR, label=legend_etiketleri[0]),
            mpatches.Patch(color=RENK_GIDER, label=legend_etiketleri[1]),
        ]
        ax.legend(handles=legend_parcalar, loc="lower center",
                  bbox_to_anchor=(0.5, -0.08), fontsize=10, frameon=False)

        ax.set_title("Gelir & Gider Oranları", fontsize=14, fontweight="bold", pad=20)
        plt.tight_layout()

        _klasor_hazirla()
        kayit_yolu = os.path.join(GRAFIK_KLASORU, "pasta_grafik.png")
        plt.savefig(kayit_yolu, dpi=150, bbox_inches="tight")
        plt.show()
        print(f"  ✅  Pasta grafik kaydedildi → {kayit_yolu}")

    except Exception as hata:
        print("  ❌  Pasta grafik oluşturulurken hata:", hata)
