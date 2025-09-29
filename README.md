# 🚀 Ultra-Futuristik 3D Web Tasarım Ajansı

Premium 3D web deneyimleri sunan, Flask tabanlı modern web sitesi projesi.

## 📋 Proje Yapısı

```
dm/
├── app.py                      # Flask backend
├── requirements.txt            # Python bağımlılıkları
├── README.md                   # Bu dosya
├── static/
│   └── style.css              # Global CSS (isteğe bağlı)
└── templates/
    ├── index.html             # Ana sayfa
    ├── product.html           # 3D Ürün Showcase
    ├── portfolio.html         # Immersive Portfolio
    ├── showroom.html          # Sanal Showroom
    ├── restaurant.html        # Restoran 3D Menü
    └── dashboard.html         # Kurumsal Dashboard
```

## 🎯 Özellikler

### Ana Sayfa (index.html)
- ✨ 5000 parçacıklı particle sistem
- 🌀 Dönen 3D geometriler (Torus, Icosahedron)
- 🎨 Cyberpunk/Neon tasarım
- 📱 Responsive tasarım
- 🔄 Smooth scroll animasyonları
- 💫 Glassmorphism efektleri

### Template 1: 3D Ürün Showcase (product.html)
- 🛍️ 360° dönen ürün görselleştirme
- 🛒 İnteraktif sepet sistemi
- 🔍 Zoom ve detay görüntüleme
- ⚡ Three.js ile gerçek zamanlı 3D rendering
- 💳 Sepete ekleme animasyonları

### Template 2: Immersive Portfolio (portfolio.html)
- 🎨 6 farklı 3D proje kartı
- 🌟 Hover efektleri ile interaktif galeri
- 📊 Modal detay sayfaları
- 🎭 Particle background
- 🖼️ Kategorize edilmiş projeler

### Template 3: Sanal Showroom (showroom.html)
- 🎮 First-person navigasyon
- ⌨️ WASD kontrolleri
- 🏃 Koşma ve zıplama mekaniği
- 🖱️ Mouse look sistemi
- 🎯 Interaktif objeler
- 📍 Minimap (hazır container)
- 💡 5 farklı 3D ürün sergileme alanı

**Kontroller:**
- `W/A/S/D` - Hareket
- `SPACE` - Zıpla
- `SHIFT` - Koş
- `FARE` - Etrafına bak
- `E` - Obje ile etkileşim

### Template 4: Restoran 3D Menü (restaurant.html)
- 🍽️ 9 farklı yemek kategorisi
- 🥘 3D yemek modelleri
- 📋 Kategori filtreleme
- 🛒 Sipariş sistemi
- 💰 Miktar seçimi
- 🎨 Lezzetli ambient atmosfer

**Kategoriler:**
- Başlangıçlar
- Ana Yemekler
- Tatlılar
- İçecekler

### Template 5: Kurumsal Dashboard (dashboard.html)
- 📊 3D Bar Chart görselleştirme
- 📈 Chart.js ile 4 farklı grafik (Line, Doughnut, Bar, Radar)
- 💹 Gerçek zamanlı veri güncelleme
- 📋 İşlem tablosu
- 🎯 KPI kartları
- 📱 Responsive sidebar
- 🌟 Gradient istatistik kartları

## 🛠️ Kurulum

### 1. Python Ortamını Hazırlayın

```bash
# Virtual environment oluşturun (opsiyonel ama önerilir)
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Çalıştırın

```bash
python app.py
```

Tarayıcınızda açın: `http://localhost:5000`

## 🌐 Route Yapısı

| Route | Açıklama |
|-------|----------|
| `/` | Ana sayfa |
| `/template/product` | 3D Ürün Showcase |
| `/template/portfolio` | Portfolio Galerisi |
| `/template/showroom` | Sanal Showroom |
| `/template/restaurant` | Restoran Menü |
| `/template/dashboard` | Dashboard |
| `/api/contact` | İletişim formu API (POST) |
| `/api/cart/add` | Sepete ekleme API (POST) |

## 🎨 Teknoloji Stack

### Frontend
- **Three.js (r128)** - 3D grafik rendering
- **Chart.js (3.9.1)** - 2D data görselleştirme
- **Vanilla JavaScript** - DOM manipülasyonu
- **CSS3** - Animasyon ve efektler
- **HTML5 Canvas** - 3D rendering surface

### Backend
- **Flask** - Python web framework
- **Python 3.x** - Backend dil

### 3D Efektler
- ✨ Particle sistemler
- 🌀 Rotating geometries
- 💫 Wireframe rendering
- 🎨 Standard/Basic materials
- 💡 Point & Directional lighting
- 🌫️ Fog effects

## 🎮 Kullanım Senaryoları

### E-ticaret Sitesi
`product.html` template'ini kullanarak ürünlerinizi 360° gösterin.

### Ajans/Freelancer Portfolio
`portfolio.html` ile projelerinizi etkileyici şekilde sergileyin.

### Sanal Mağaza/Fuarlar
`showroom.html` ile ziyaretçilerinize sanal tur deneyimi sunun.

### Restoran/Cafe
`restaurant.html` ile menünüzü interaktif hale getirin.

### Kurumsal Raporlama
`dashboard.html` ile verilerinizi görselleştirin.

## 🔧 Özelleştirme

### Renk Paleti Değiştirme

Ana sayfa (Cyan/Purple/Pink):
```css
/* index.html içinde */
background: linear-gradient(to right, #00ffff, #a855f7, #ec4899);
```

Product (Purple/Blue):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Portfolio (Magenta/Cyan):
```css
background: linear-gradient(to right, #ff00ff, #00ffff);
```

### 3D Model Değiştirme

```javascript
// Geometry değiştirme örneği
const geometry = new THREE.BoxGeometry(2, 2, 2); // Küp
// veya
const geometry = new THREE.SphereGeometry(1, 32, 32); // Küre
// veya
const geometry = new THREE.TorusKnotGeometry(1, 0.3, 100, 16); // Torus Knot
```

### API Entegrasyonu

```python
# app.py içinde
@app.route("/api/custom-endpoint", methods=["POST"])
def custom_endpoint():
    data = request.get_json()
    # Veritabanı işlemleri
    # Email gönderimi
    # Ödeme işlemleri vb.
    return jsonify({"status": "success"})
```

## 📊 Performans Optimizasyonu

- ✅ Canvas rendering optimization
- ✅ Particle count ayarlanabilir
- ✅ RequestAnimationFrame kullanımı
- ✅ Event listener cleanup
- ✅ Responsive canvas resize

## 🐛 Sorun Giderme

### Three.js yüklenmiyor
```html
<!-- CDN linkini kontrol edin -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

### 3D scene görünmüyor
- Canvas elementinin z-index değerini kontrol edin
- Canvas boyutlarının doğru ayarlandığından emin olun
- Browser console'da hata var mı kontrol edin

### Flask başlamıyor
```bash
# Port değiştirin
python app.py --port 8000
```

## 📱 Responsive Tasarım

Tüm template'ler mobil uyumludur:
- 📱 < 768px: Mobil layout
- 💻 768px - 1024px: Tablet layout
- 🖥️ > 1024px: Desktop layout

## 🚀 Production Deployment

### Gunicorn ile (Linux)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Nginx Reverse Proxy
```nginx
location / {
    proxy_pass http://localhost:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## 📄 Lisans

Bu proje eğitim amaçlıdır. Ticari kullanım için lisans gerekir.

## 👨‍💻 Geliştirici

CyberDesign Team - Ultra-futuristik web deneyimleri

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📞 İletişim

Sorularınız için: contact@cyberdesign.com

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!