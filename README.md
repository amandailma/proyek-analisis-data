# Proyek Analisis Data: Olist E-Commerce Dataset 📊

## Deskripsi
Proyek ini merupakan hasil analisis mendalam terhadap dataset E-Commerce Olist untuk memahami dinamika pasar di Brazil. Fokus utama analisis ini adalah membedah distribusi geografis pelanggan dan mengevaluasi tingkat retensi pengguna guna memberikan rekomendasi strategis bagi pertumbuhan bisnis. Analisis dibatasi secara ketat pada periode operasional **Januari 2017 hingga Desember 2018** untuk memastikan relevansi data sesuai prinsip SMART.

## Tahapan Analisis (Data Science Lifecycle)
*   **Data Gathering**: Mengintegrasikan berbagai tabel dari dataset Olist (customers, orders, dan payments).
*   **Data Assessing & Cleaning**: Menangani *missing values*, memastikan konsistensi tipe data (terutama konversi kolom datetime), serta melakukan filtering data berbasis waktu (2017-2018).
*   **Exploratory Data Analysis (EDA)**: Menjelajahi pola persebaran pelanggan antar wilayah dan menganalisis perilaku pembelian ulang (loyalitas).
*   **Data Visualization**: Menyajikan temuan dalam bentuk visualisasi yang memenuhi prinsip integritas data (Tufte's principles).

## Wawasan Utama (Insights)
1.  **Analisis Geografis (Dominasi Tenggara)**: Aktivitas ekonomi Olist masih sangat terpusat di wilayah Tenggara Brazil. **São Paulo (SP)** memimpin jauh dengan lebih dari 40.000 pelanggan unik. Hal ini menunjukkan perlunya efisiensi logistik di wilayah padat dan strategi ekspansi di wilayah yang masih sepi.
2.  **Analisis Retensi (Tantangan Loyalitas)**: Ditemukan bahwa **96,9%** pelanggan merupakan *One-Time Buyer*. Angka *Repeat Buyer* yang hanya menyentuh **3,1%** menjadi sinyal urgensi bagi tim bisnis untuk segera merancang program loyalitas atau CRM guna meningkatkan *Customer Lifetime Value*.
3. **RFM Analysis (Monetary)**: Berhasil mengidentifikasi profil pelanggan "Top Spenders" untuk keperluan program loyalitas eksklusif atau penawaran produk premium.

## Struktur Proyek
- `/dashboard`: Berisi file aplikasi utama `dashboard.py` dan dataset yang telah dibersihkan `main_data.csv`.
- `/data`: Kumpulan dataset mentah (raw data) asli dari Olist.
- `notebook.ipynb`: Dokumentasi teknis lengkap mulai dari tahap *wrangling*, EDA, hingga visualisasi.
- `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan untuk menjalankan lingkungan proyek.
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
	 ```bash
    streamlit run dashboard.py

Proyek ini juga sudah dideploy secara online dan dapat diakses secara langsung melalui tautan berikut:
**https://8uyohbtxqp6sscbirsuhxj.streamlit.app/**
