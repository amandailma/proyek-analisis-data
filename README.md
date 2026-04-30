# Proyek Analisis Data: Olist E-Commerce Dataset 📊

## Deskripsi
Proyek ini merupakan hasil analisis data dari dataset E-Commerce Olist. Proyek ini mencakup seluruh siklus analisis data, mulai dari pengolahan data mentah hingga penyajian wawasan bisnis melalui dashboard interaktif. Fokus utama analisis ini adalah memahami distribusi geografis pelanggan, loyalitas pengguna, dan profil pelanggan dengan kontribusi pendapatan terbesar.

## Tahapan Analisis (Data Wrangling & EDA)
- **Data Gathering**: Mengintegrasikan berbagai tabel dataset Olist (customers, orders, payments, dll).
- **Data Assessing & Cleaning**: Menangani missing values, menghapus data duplikat, dan memastikan konsistensi tipe data (terutama kolom datetime).
- **Exploratory Data Analysis (EDA)**: Menjelajahi pola dasar data untuk menjawab pertanyaan bisnis terkait persebaran pelanggan dan tren pesanan.

## Wawasan Utama (Insights)
1. **Analisis Geografis**: Wilayah Tenggara Brazil (Sao Paulo & Rio de Janeiro) merupakan basis pelanggan terbesar. Hal ini menjadi peluang besar untuk optimalisasi distribusi logistik.
2. **Manual Grouping (Retensi)**: Ditemukan bahwa 96.9% pelanggan merupakan *One-Time Buyer*. Insight ini menunjukkan perlunya strategi pemasaran baru untuk meningkatkan loyalitas pelanggan.
3. **RFM Analysis (Monetary)**: Berhasil mengidentifikasi profil pelanggan "Top Spenders" untuk keperluan program loyalitas eksklusif atau penawaran produk premium.

## Struktur Proyek
- `/dashboard`: Berisi file aplikasi utama `dashboard.py` dan `main_data.csv`.
- `/data`: Berisi kumpulan dataset mentah (raw data) asli.
- `notebook.ipynb`: Dokumentasi teknis lengkap dari tahap pembersihan data hingga visualisasi.
- `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan.
- `url.txt`: Tautan akses dashboard publik.

## Cara Menjalankan Dashboard Secara Lokal
1. Setup Environment - Anaconda
	```conda create --name main-ds python=3.9
	conda activate main-ds
	pip install -r requirements.txt
2. Setup Environment - Shell/Terminal
	```mkdir proyek_analisis_data
	cd proyek_analisis_data
	pipenv install
	pipenv shell
	pip install -r requirements.txt
3. Run steamlit app
	```streamlit run dashboard.py

Proyek ini juga sudah dideploy secara online dan dapat diakses secara langsung melalui tautan berikut:
**https://8uyohbtxqp6sscbirsuhxj.streamlit.app/**
