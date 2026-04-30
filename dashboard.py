import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set tema 
sns.set_theme(style='white')

# 1. Load Data
# Mengambil data dari file CSV
def load_data():
    df = pd.read_csv("main_data.csv")
    if "order_purchase_timestamp" in df.columns:
        df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

main_df = load_data()

# 2. Header & Title Dashboard
st.header('E-Commerce Data Dashboard 📊')

# Membuat Sidebar di sebelah kiri
with st.sidebar:
    st.title("Olist Analysis")
    st.write("Dashboard ini menampilkan insight mengenai demografi pelanggan dan tingkat retensi dari Olist E-Commerce.")

# 3. Layout Utama (Angka Metrik)
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Customers", value=main_df['customer_unique_id'].nunique())
with col2:
    st.metric("Total Orders", value=main_df['order_id'].nunique())

# 4. Visualisasi 1: Top States (Bar Chart)
st.subheader("Top 10 Negara Bagian dengan Pelanggan Terbanyak")

# Mengubah singkatan wilayah menjadi nama panjang agar lebih mudah dibaca
state_mapping = {
    'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais',
    'RS': 'Rio Grande do Sul', 'PR': 'Paraná', 'SC': 'Santa Catarina',
    'BA': 'Bahia', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás'
}

bystate_df = main_df.groupby("customer_state").customer_unique_id.nunique().reset_index()
bystate_df.rename(columns={"customer_unique_id": "customer_count"}, inplace=True)
bystate_df['state_name'] = bystate_df['customer_state'].map(state_mapping).fillna(bystate_df['customer_state'])
top_states = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 5))
# Memberikan warna biru pada bar tertinggi, sisanya abu-abu
colors = ["blue" if i == 0 else "lightgrey" for i in range(len(top_states))]
sns.barplot(x="customer_count", y="state_name", data=top_states, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel("Jumlah Pelanggan")
sns.despine()
st.pyplot(fig)

# 5. Visualisasi 2: Buyer Type (Pie Chart)
st.subheader("Proporsi Pelanggan: One-Time vs Repeat Buyer")

order_freq = main_df.groupby('customer_unique_id')['order_id'].nunique().reset_index()
order_freq['buyer_type'] = order_freq['order_id'].apply(lambda x: 'One-Time Buyer' if x == 1 else 'Repeat Buyer')
sizes = order_freq['buyer_type'].value_counts().values
labels = order_freq['buyer_type'].value_counts().index

fig, ax = plt.subplots(figsize=(6, 6))
colors_pie = ["lightblue", "orange"]
explode = (0, 0.1) if len(sizes) > 1 else (0,)

ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie[:len(sizes)], autopct='%1.1f%%', startangle=90)
st.pyplot(fig)

# 6. Analisis Lanjutan: Top Spend (Monetary)
st.subheader("Top 5 Pelanggan dengan Pengeluaran Tertinggi (Monetary)")

if 'payment_value' in main_df.columns:
    rfm_df = main_df.groupby("customer_unique_id").payment_value.sum().reset_index()
    rfm_df.columns = ["customer_id", "monetary"]
    top_5_monetary = rfm_df.sort_values(by="monetary", ascending=False).head(5)
    # Memotong ID pelanggan agar tidak terlalu panjang di grafik
    top_5_monetary['short_id'] = top_5_monetary['customer_id'].str[:8] + "..."

    fig, ax = plt.subplots(figsize=(10, 5))
    colors_bar = ["blue", "lightgrey", "lightgrey", "lightgrey", "lightgrey"]
    sns.barplot(x="monetary", y="short_id", data=top_5_monetary, palette=colors_bar, ax=ax)
    ax.set_ylabel("Customer ID")
    ax.set_xlabel("Total Pengeluaran (BRL)")
    sns.despine()
    st.pyplot(fig)
else:
    st.write("Data payment_value tidak tersedia untuk analisis ini.")