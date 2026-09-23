import random
import customtkinter as ctk

# Arayüz Teması
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class FikirDislisiApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Fikir Dişlisi ⚙️ v1.0")
        self.geometry("600x650")
        self.resizable(False, False)

        # Fikir Veri Tabanı (Prosedürel Kombinasyon Yapısı)
        self.fikir_havuzu = {
            "Oyun": {
                "tur": ["Roguelike", "Top-down Shooter", "Bulmaca", "Simülasyon", "Strateji"],
                "tema": ["Cyberpunk", "Karanlık Orta Çağ", "Uzay / Derin Boşluk", "Post-Apotipik", "Retro 80'ler"],
                "twist": ["zaman her hareket ettiğinde duruyor", "sağlık puanı aynı zamanda merminiz", "harita her 30 saniyede bir rastgele dönüyor"]
            },
            "Oyun Modu": {
                "hedef_oyun": ["Minecraft", "Warband/Bannerlord", "GTA V", "Roblox"],
                "mekanik": ["Ekonomi & Ticaret Sistemleri", "Özel Boyut / Harita", "Sınıf Tabanlı Yetenekler", "Dalga Tabanlı Survival"],
                "detay": ["oyuncuların kendi krallığını kurduğu", "tamamen ses efektlerine odaklanan", "fizik tabanlı bulmacalar içeren"]
            },
            "Müzik": {
                "tarz": ["Synthwave / Chiptune", "Orkestral Koyu Fantastik", "Lo-Fi Beats", "Endüstriyel Metal"],
                "hissiyat": ["Gerilim ve Yarış", "Hüzünlü Keşif", "Epik Boss Savaşı", "Sakin Gece Atmosferi"],
                "enstruman": ["8-bit Synth + Elektro Gitar", "Çello + Ağır Baslar", "Akustik Gitar + Yağmur Sesi"]
            },
            "Map Tasarımı": {
                "ortam": ["Terk Edilmiş Askeri Üs", "Yüzen Adalar Ekosistemi", "Siberpunk Ara Sokak", "Zindan Kompleksi"],
                "odak": ["Dikey Hareketlilik ve Tırmanma", "Dar Koridor Çatışmaları", "Gizli Geçitler ve Bulmacalar"]
            },
            "3D Model": {
                "stil": ["Low-Poly", "Stylized PBR", "Voxel", "Retro PS1 Style"],
                "obje": ["Antik Efsunlu Kılıç", "Mekanik Siber Göz", "Terk Edilmiş Sci-Fi Arabası", "Mantar Evi"]
            }
        }

        self.setup_ui()

    def setup_ui(self):
        # Header
        self.title_label = ctk.CTkLabel(
            self, text="FİKİR DİŞLİSİ", font=ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(pady=(20, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Kreatif projelerin için rastgele ve uyumlu konsept üretici",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        )
        self.subtitle_label.pack(pady=(0, 20))

        # 1. TEMA SEÇİMİ (Kategori)
        self.kategori_frame = ctk.CTkFrame(self)
        self.kategori_frame.pack(pady=10, padx=30, fill="x")

        self.kategori_label = ctk.CTkLabel(
            self.kategori_frame, text="Kategori Seçin:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.kategori_label.pack(pady=(10, 5))

        self.kategori_var = ctk.StringVar(value="Oyun")
        self.kategori_selector = ctk.CTkSegmentedButton(
            self.kategori_frame,
            values=list(self.fikir_havuzu.keys()),
            variable=self.kategori_var,
        )
        self.kategori_selector.pack(pady=(0, 15), padx=10)

        # 2. ANA BUTON (Dişliyi Çalıştır)
        self.generate_btn = ctk.CTkButton(
            self,
            text="⚙️ DİŞLİYİ ÇALIŞTIR",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=50,
            corner_radius=25,
            fg_color="#1f538d",
            hover_color="#14375e",
            command=self.fikir_uret,
        )
        self.generate_btn.pack(pady=20, padx=50, fill="x")

        # 3. SONUÇ EKRANI
        self.result_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=10)
        self.result_frame.pack(pady=10, padx=30, fill="both", expand=True)

        self.result_title = ctk.CTkLabel(
            self.result_frame,
            text="Üretilen Konsept",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#3B82F6",
        )
        self.result_title.pack(pady=(15, 5))

        self.result_textbox = ctk.CTkTextbox(
            self.result_frame,
            font=ctk.CTkFont(size=14),
            wrap="word",
            state="disabled",
            fg_color="transparent",
        )
        self.result_textbox.pack(pady=10, padx=15, fill="both", expand=True)

    def fikir_uret(self):
        kat = self.kategori_var.get()
        veri = self.fikir_havuzu[kat]
        metin = ""

        if kat == "Oyun":
            metin = f"📌 Tür: {random.choice(veri['tur'])}\n\n🎨 Atmosfer: {random.choice(veri['tema'])}\n\n💡 Ana Mekanik / Twist: Oyunda {random.choice(veri['twist'])}."
        elif kat == "Oyun Modu":
            metin = f"🎮 Hedef Oyun: {random.choice(veri['hedef_oyun'])}\n\n⚙️ Mod Türü: {random.choice(veri['mekanik'])}\n\n📝 Konsept: Oyuna {random.choice(veri['detay'])} bir yapı kazandır."
        elif kat == "Müzik":
            metin = f"🎵 Tarz: {random.choice(veri['tarz'])}\n\n🎭 Hissiyat/Saha: {random.choice(veri['hissiyat'])}\n\n🎸 Öne Çıkan Enstrümanlar: {random.choice(veri['enstruman'])}."
        elif kat == "Map Tasarımı":
            metin = f"🗺️ Harita Teması: {random.choice(veri['ortam'])}\n\n🎯 Tasarım Odak Noktası: {random.choice(veri['odak'])}."
        elif kat == "3D Model":
            metin = f"📐 Görsel Stil: {random.choice(veri['stil'])}\n\n📦 Obje/Karakter: {random.choice(veri['obje'])}."

        # Ekrana Yazdır
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.result_textbox.insert("1.0", metin)
        self.result_textbox.configure(state="disabled")


if __name__ == "__main__":
    app = FikirDislisiApp()
    app.mainloop()
