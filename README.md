# FastAPI Kullanıcı Yönetim Sistemi

Bu proje, FastAPI kullanılarak geliştirilmiş kapsamlı bir kullanıcı yönetim sistemidir. Kullanıcı tipleri, roller ve profil yönetimi gibi temel özellikleri içerir.

## Özellikler

- 🔐 JWT tabanlı kimlik doğrulama
- 👥 Kullanıcı yönetimi (CRUD işlemleri)
- 📁 Profil fotoğrafı yükleme
- 🔄 Kullanıcı tipleri yönetimi
- ✨ Modern ve güvenli API tasarımı

## Proje Yapısı

```
app/
├── __init__.py
├── main.py              # FastAPI ana uygulama
├── database.py          # Veritabanı bağlantısı
├── auth/               # Kimlik doğrulama modülü
│   ├── __init__.py
│   ├── routes.py       # Auth endpoint'leri
│   ├── schemas.py      # Auth şemaları
│   └── views.py        # Auth iş mantığı
├── users/             # Kullanıcı modülü
│   ├── __init__.py
│   ├── models.py      # Kullanıcı modeli
│   ├── routes.py      # Kullanıcı endpoint'leri
│   ├── schemas.py     # Kullanıcı şemaları
│   └── views.py       # Kullanıcı iş mantığı
├── user_types/        # Kullanıcı tipleri modülü
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── views.py
└── user_roles/        # Kullanıcı rolleri modülü
    ├── __init__.py
    ├── models.py
    ├── routes.py
    ├── schemas.py
    └── views.py
```

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [proje-url]
cd [proje-dizini]
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
# Windows için
venv\Scripts\activate
# Linux/Mac için
source venv/bin/activate
```

3. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Uygulamayı çalıştırın:
```bash
uvicorn app.main:app --reload
```

## API Endpoint'leri

### Kimlik Doğrulama
- `POST /api/auth/login` - Kullanıcı girişi ve token alma

### Kullanıcılar
- `GET /api/users/` - Tüm kullanıcıları listele
- `GET /api/users/{user_id}` - Belirli bir kullanıcıyı getir
- `POST /api/users/` - Yeni kullanıcı oluştur
- `PUT /api/users/` - Kullanıcı bilgilerini güncelle
- `DELETE /api/users/` - Kullanıcı sil

### Kullanıcı Tipleri
- `GET /api/user-types/` - Tüm kullanıcı tiplerini listele
- `POST /api/user-types/` - Yeni kullanıcı tipi oluştur
- `PUT /api/user-types/` - Kullanıcı tipi güncelle
- `DELETE /api/user-types/` - Kullanıcı tipi sil

### Kullanıcı Rolleri
- `GET /api/user-roles/` - Tüm rolleri listele
- `POST /api/user-roles/` - Yeni rol oluştur
- `PUT /api/user-roles/` - Rol güncelle
- `DELETE /api/user-roles/` - Rol sil

## Özellik Detayları

### Kullanıcı Yönetimi
- Email doğrulama
- Güvenli şifre hashleme
- Profil fotoğrafı yükleme (JPEG, PNG, JPG)
- Çoklu rol atama
- Aktif/pasif kullanıcı durumu

### Güvenlik
- JWT tabanlı kimlik doğrulama
- Güvenli dosya yükleme kontrolleri
- Şifre hashleme (bcrypt)

### Dosya Yönetimi
- Otomatik upload dizini oluşturma
- Güvenli dosya adı oluşturma
- Dosya boyutu ve tip kontrolü
- Statik dosya sunumu

## Teknik Detaylar

- FastAPI 0.109.2
- SQLAlchemy 2.0.27
- Pydantic 2.6.1
- JWT kimlik doğrulama
- SQLite veritabanı (geliştirme için)
- Async/await desteği
- OpenAPI (Swagger) dokümantasyonu

## API Dokümantasyonu

API dokümantasyonuna aşağıdaki URL'lerden erişebilirsiniz:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Geliştirme

1. Yeni bir özellik eklemek için:
   - İlgili modülde models.py'da modeli tanımlayın
   - schemas.py'da Pydantic modellerini oluşturun
   - views.py'da iş mantığını yazın
   - routes.py'da endpoint'leri tanımlayın

2. Veritabanı değişiklikleri için:
   - models.py'da gerekli değişiklikleri yapın
   - Veritabanını yeniden oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın. 