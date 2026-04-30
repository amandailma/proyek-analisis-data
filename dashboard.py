import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set tema seaborn
sns.set_theme(style="white")

# 1. Helper Functions (Untuk menyiapkan data)
def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_unique_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_unique_id": "customer_count"}, inplace=True)
    bystate_df = bystate_df.sort_values(by="customer_count", ascending=False)
    
    # Mapping nama state
    state_mapping = {
        'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais',
        'RS': 'Rio Grande do Sul', 'PR': 'Paraná', 'SC': 'Santa Catarina',
        'BA': 'Bahia', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás'
    }
    bystate_df['state_name'] = bystate_df['customer_state'].map(state_mapping)
    return bystate_df

def create_order_freq_df(df):
    order_freq = df.groupby('customer_unique_id')['order_id'].count().reset_index()
    order_freq.columns = ['customer_unique_id', 'order_count']
    order_freq['buyer_type'] = order_freq['order_count'].apply(lambda x: 'One-Time Buyer' if x == 1 else 'Repeat Buyer')
    return order_freq

# 2. Load Data
all_df = pd.read_csv("main_data.csv")

# 3. Menyiapkan Dataframes
bystate_df = create_bystate_df(all_df)
order_freq = create_order_freq_df(all_df)

# =========================================================
# DASHBOARD UI (Streamlit)
# =========================================================

# Title
st.set_page_config(page_title="Olist E-Commerce Dashboard", page_icon="📦", layout="wide")
st.title("📦 Olist E-Commerce Dashboard (2017-2018)")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.markdown("### 📊 Ringkasan Data")
    st.info(f"Total Pelanggan: **{all_df['customer_unique_id'].nunique():,}**")
    st.info(f"Total Pesanan: **{all_df['order_id'].nunique():,}**")
    st.caption("Data difilter khusus untuk periode 1 Januari 2017 - 31 Desember 2018 guna memenuhi analisis yang berorientasi tindakan.")

# Layout Kolom
col1, col2 = st.columns(2)

# =========================================================
# VISUALISASI 1: Distribusi Geografis (Bar Chart)
# =========================================================
with col1:
    st.subheader("Distribusi Geografis Pelanggan (Top 10)")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_states = bystate_df.head(10)
    colors = ["blue" if i == 0 else "lightgrey" for i in range(len(top_states))]
    
    sns.barplot(
        x="customer_count",
        y="state_name",
        data=top_states,
        palette=colors,
        ax=ax
    )
    
    ax.set_ylabel("Negara Bagian", fontsize=12)
    ax.set_xlabel("Jumlah Pelanggan", fontsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.bar_label(ax.containers[0], padding=5, fmt='%d', fontsize=10)
    sns.despine()
    
    st.pyplot(fig)
    
    with st.expander("Lihat Insight"):
        st.write("Negara bagian **São Paulo** mendominasi pasar secara absolut, disusul oleh Rio de Janeiro dan Minas Gerais. Diperlukan optimalisasi rute logistik untuk area ini.")

# =========================================================
# VISUALISASI 2: Loyalitas Pelanggan (Pie Chart)
# =========================================================
with col2:
    st.subheader("Rasio Loyalitas Pelanggan")
    
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    buyer_counts = order_freq['buyer_type'].value_counts()
    colors_pie = ["lightblue", "orange"]
    explode = (0, 0.1)
    
    ax2.pie(
        buyer_counts.values, 
        labels=buyer_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors_pie, 
        explode=explode,
        textprops={'fontsize': 12},
        shadow=False
    )
    ax2.axis('equal') 
    
    st.pyplot(fig2)
    
    with st.expander("Lihat Insight"):
        st.write("Tingkat retensi pelanggan sangat rendah (Hanya **3.1% Repeat Buyer**). Olist sangat bergantung pada pelanggan baru. Perlu segera meluncurkan program loyalitas atau promosi untuk transaksi kedua.")

st.caption("Dicoding Data Analytics Project | Dashboard by Amanda Ilma")