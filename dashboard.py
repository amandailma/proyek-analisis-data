import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setup dasar
st.set_page_config(page_title="Olist Strategic Dashboard", layout="wide")
sns.set_theme(style="white")

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

all_df = load_data()

# SIDEBAR
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Panel")
    # Penyesuaian rentang waktu
    start_date, end_date = st.date_input(
        "Pilih Rentang Waktu",
        [all_df["order_purchase_timestamp"].min(), all_df["order_purchase_timestamp"].max()]
    )

# Filter Global
main_df = all_df[(all_df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) & 
                 (all_df["order_purchase_timestamp"] <= pd.to_datetime(end_date))]

# HEADER: KPI SECTION
st.title("📊Proyek Analisis Data: Olist E-Commerce Dataset")
st.markdown(f"**Periode Analisis:** {start_date} s/d {end_date}")

# Menghitung metrik dengan UNIQ (agar tidak double count karena duplikat baris)
col1, col2, col3 = st.columns(3)
with col1:
    total_cust = main_df['customer_unique_id'].nunique()
    st.metric("Total Unique Customers", f"{total_cust:,}")
with col2:
    total_orders = main_df['order_id'].nunique()
    st.metric("Total Verified Orders", f"{total_orders:,}")
with col3:
    # Revenue dihitung dari total payment unik
    total_rev = main_df.drop_duplicates(subset=['order_id', 'payment_value'])['payment_value'].sum()
    st.metric("Total Revenue", f"R$ {total_rev:,.2f}")

st.markdown("---")

# MENU UTAMA (3 TABS)
tab1, tab2, tab3 = st.tabs(["📈 Business Growth", "📍 Regional Insights", "🤝 Customer Loyalty"])

# TAB 1: BUSINESS GROWTH & TOP SPENDER
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Tren Pesanan Bulanan")
        monthly_df = main_df.resample(rule='ME', on='order_purchase_timestamp').order_id.nunique().reset_index()
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(monthly_df['order_purchase_timestamp'], monthly_df['order_id'], marker='o', color='steelblue', linewidth=2)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    with c2:
        st.subheader("Top 5 Spender (Loyal VIP)")
        # Menghitung total belanja per pelanggan unik
        top_spenders = main_df.groupby("customer_unique_id").payment_value.sum().sort_values(ascending=False).head(5).reset_index()
        top_spenders['short_id'] = top_spenders['customer_unique_id'].str[:8] + "..."
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x="payment_value", y="short_id", data=top_spenders, color="orange", ax=ax)
        ax.bar_label(ax.containers[0], fmt='R$ %.2f', padding=3)
        st.pyplot(fig)

    st.info("**Analisis Bisnis:** Tren bulanan menunjukkan stabilitas operasional, sementara identifikasi Top Spender memungkinkan tim pemasaran untuk menjalankan kampanye *Exclusive Loyalty Program* bagi pelanggan bernilai tinggi (High-Value Customers).")

# TAB 2: GEOGRAPHIC DISTRIBUTION
with tab2:
    st.subheader("Persebaran Pelanggan Berdasarkan Negara Bagian")
    state_mapping = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais', 'RS': 'Rio Grande do Sul', 'PR': 'Paraná'}
    
    geo_df = main_df.groupby("customer_state").customer_unique_id.nunique().sort_values(ascending=False).head(10).reset_index()
    geo_df['state_name'] = geo_df['customer_state'].map(state_mapping).fillna(geo_df['customer_state'])
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="customer_unique_id", y="state_name", data=geo_df, 
                palette=["blue" if i == 0 else "lightgrey" for i in range(10)], ax=ax)
    ax.bar_label(ax.containers[0], padding=3)
    st.pyplot(fig)
    
    st.write("**Insight Geografis:** Wilayah Tenggara (SP, RJ, MG) menguasai lebih dari 60% total basis pelanggan. Dominasi São Paulo yang sangat kontras menunjukkan perlunya pemusatan pusat distribusi (*fulfillment center*) di wilayah tersebut untuk menekan ongkos kirim dan mempercepat durasi pengiriman.")

# TAB 3: CUSTOMER LOYALTY
with tab3:
    st.subheader("Analisis Retensi: One-Time vs Repeat Buyer")
    order_freq = main_df.groupby('customer_unique_id').order_id.nunique().reset_index()
    order_freq['type'] = order_freq['order_id'].apply(lambda x: 'One-Time' if x == 1 else 'Repeat')
    counts = order_freq['type'].value_counts()
    
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(counts, labels=counts.index, autopct='%1.2f%%', colors=['lightblue', 'orange'], 
               explode=(0, 0.1), startangle=90)
        st.pyplot(fig)
    
    with col_b:
        st.write("### Rekomendasi Strategis Retensi:")
        st.error(f"Ditemukan bahwa pelanggan setia (Repeat Buyer) hanya sebesar { (counts['Repeat']/counts.sum()*100):.2f}%.")
        st.markdown("""
        1. **Incentive Purchase:** Berikan voucher 'Thank You' otomatis setelah pembelian pertama untuk merangsang transaksi kedua.
        2. **Subscription Model:** Pertimbangkan fitur berlangganan untuk kategori produk *fast-moving* (kebutuhan harian).
        3. **Remarketing:** Lakukan *retargeting ads* atau email marketing khusus untuk 96% pelanggan yang saat ini hanya berbelanja satu kali.
        """)

st.caption("Strategic Data Analysis Dashboard | Created by Amanda Ilma | 2026")