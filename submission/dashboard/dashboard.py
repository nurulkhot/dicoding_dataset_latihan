import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')
st.title('Visualisasi Data Temperature dan Hujan di Stasiun Gucheng')
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Location_of_Gucheng_within_Yunnan_%28China%29.png")
 
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://cdn.icon-icons.com/icons2/2745/PNG/512/temperature_icon_175973.png")
    st.text('Data Air Quality Sumber: https://github.com/marceloreis/HTI/tree/master')

import streamlit as st
 
st.title('Tren Temperature')
col1, col2, col3 = st.columns([1, 1, 1])
 
with col1:
    st.header("2014")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2014
    temp_2014 = temp_df[temp_df['year'] == 2014]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2014
    temp_2014_avg = temp_2014.groupby('month')['TEMP'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2014_avg.index, temp_2014_avg.values, marker='o', color='red')
    ax.set_title('Temperature di 2014 (Rata-Hujan per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Temperature')

    # Menambahkan grid
    ax.grid(True)
    
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)
    
with col2:
    st.header("2015")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2015
    temp_2015 = temp_df[temp_df['year'] == 2015]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2015
    temp_2015_avg = temp_2014.groupby('month')['TEMP'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2015_avg.index, temp_2015_avg.values, marker='o', color='red')
    ax.set_title('Temperature in 2015 (Rata-Hujan per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Temperature')

    # Menambahkan grid
    ax.grid(True)
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)
 
with col3:
    st.header("2016")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2016
    temp_2016 = temp_df[temp_df['year'] == 2016]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2014
    temp_2016_avg = temp_2016.groupby('month')['TEMP'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2016_avg.index, temp_2016_avg.values, marker='o', color='red')
    ax.set_title('Temperature in 2016 (Rata-Hujan per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Temperature')

    # Menambahkan grid
    ax.grid(True)
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)
 
import streamlit as st
 
st.title('Tren Curah Hujan')
tab1, tab2, tab3 = st.tabs(["2014", "2015", "2016"])
 
with tab1:
    st.header("2014")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2014
    temp_2014 = temp_df[temp_df['year'] == 2014]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2014
    temp_2014_avg = temp_2014.groupby('month')['RAIN'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2014_avg.index, temp_2014_avg.values, marker='o', color='red')
    ax.set_title('Hujan di 2014 (Rata-rata per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rain')

    # Menambahkan grid
    ax.grid(True)
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)
 
with tab2:
    st.header("2015")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2014
    temp_2015 = temp_df[temp_df['year'] == 2015]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2014
    temp_2015_avg = temp_2014.groupby('month')['RAIN'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2015_avg.index, temp_2015_avg.values, marker='o', color='red')
    ax.set_title('Hujan di 2015 (Rata-rata per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rain')

    # Menambahkan grid
    ax.grid(True)
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)
 
with tab3:
    st.header("2016")
    # Membaca data
    temp_df = pd.read_csv("D:/SEMESTER 7/GITHUB CLONE/dicoding_dataset_latihan/submission/dashboard/all_data.csv")

    # Filter data untuk tahun 2016
    temp_2016 = temp_df[temp_df['year'] == 2016]

    # Menghitung rata-rata temperatur per bulan untuk tahun 2016
    temp_2016_avg = temp_2016.groupby('month')['RAIN'].mean()

    # Membuat plot garis dengan rata-rata temperatur per bulan
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(temp_2016_avg.index, temp_2016_avg.values, marker='o', color='red')
    ax.set_title('Hujan di 2016 (Rata-rata per Bulan)')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Temperature')

    # Menambahkan grid
    ax.grid(True)
    # Tampilkan plot ke aplikasi Streamlit
    st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
 
with st.container():
    st.header("Scatterplot Hujan terhadap Temperatur")
    # Menghitung korelasi Pearson antara curah hujan (RAIN) dan temperatur (TEMP)
    correlation_value = temp_df['RAIN'].corr(temp_df['TEMP'])

    # Menampilkan nilai korelasi di Streamlit
    st.write(f"Nilai Korelasi Pearson antara Curah Hujan (RAIN) dan Temperatur (TEMP): {correlation_value:.2f}")

    # Membuat scatter plot untuk hubungan antara curah hujan (RAIN) dan temperatur (TEMP)
    fig, ax = plt.subplots(figsize=(8, 6))  # Mengatur ukuran plot
    ax.scatter(temp_df['RAIN'], temp_df['TEMP'], color='blue')  # Membuat scatter plot

    # Menambahkan label dan judul
    ax.set_title('Korelasi antara Curah Hujan (RAIN) dan Temperatur (TEMP)', fontsize=14)
    ax.set_xlabel('Curah Hujan (RAIN)', fontsize=12)
    ax.set_ylabel('Temperatur (TEMP)', fontsize=12)

    # Menambahkan grid
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    
    
    st.header("Temperature terhadap Hujan")
    # Menghitung korelasi Pearson antara curah hujan (TEMP) dan temperatur (RAIN)
    correlation_value = temp_df['TEMP'].corr(temp_df['RAIN'])

    # Menampilkan nilai korelasi di Streamlit
    st.write(f"Nilai Korelasi Pearson antara Temperature dan (Curah Hujan (RAIN): {correlation_value:.2f}")

    # Membuat scatter plot untuk hubungan antara curah hujan (TEMP) dan Curah Hujan (RAIN)
    fig, ax = plt.subplots(figsize=(8, 6))  # Mengatur ukuran plot
    ax.scatter(temp_df['TEMP'], temp_df['RAIN'], color='blue')  # Membuat scatter plot

    # Menambahkan label dan judul
    ax.set_title('Korelasi antara Temperature (TEMP) dan Curah Hujan (RAIN)', fontsize=14)
    ax.set_xlabel('Temperature (TEMP)', fontsize=12)
    ax.set_ylabel('Curah Hujan (RAIN)', fontsize=12)

    # Menambahkan grid
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

st.header("Clustering Data Temperature")
st.write("Scatterplot clustering temperature")

# Fungsi untuk mengkategorikan temperatur
def categorize_temp(temp):
    if temp < 10:
        return 'Dingin'
    elif 10 <= temp <= 20:
        return 'Sedang'
    else:
        return 'Panas'

# Membaca data dan mengkategorikan temperatur
temp_df['Kategori_TEMP'] = temp_df['TEMP'].apply(categorize_temp)
print(temp_df[['TEMP', 'Kategori_TEMP']])

# Membuat Scatter plot cluster
# Mapping kategori ke warna yang berbeda
color_mapping = {'Dingin': 'blue', 'Sedang': 'orange', 'Panas': 'red'}
temp_df['Color'] = temp_df['Kategori_TEMP'].map(color_mapping)

# Membuat scatter plot dengan warna berbeda untuk tiap cluster
fig, ax = plt.subplots(figsize=(8, 6))
for category, color in color_mapping.items():
    subset = temp_df[temp_df['Kategori_TEMP'] == category]
    ax.scatter(subset['RAIN'], subset['TEMP'], c=color, label=category, alpha=0.6)

# Menambahkan label dan judul
ax.set_title('Scatter Plot Temperatur dan Curah Hujan Berdasarkan Kategori')
ax.set_xlabel('Curah Hujan (RAIN)')
ax.set_ylabel('Temperatur (TEMP)')

# Menambahkan legenda
ax.legend(title='Kategori')

# Menampilkan plot di Streamlit
st.pyplot(fig)
 
 # membuat diagram batang cluster
 # Menghitung frekuensi dari setiap kategori
freq_counts = temp_df['Kategori_TEMP'].value_counts()

# Membuat plot menggunakan fig dan ax dari matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
freq_counts.plot(kind='bar', color=['blue', 'red', 'green'], ax=ax)

# Menambahkan label dan judul
ax.set_title('Distribusi Kategori Temperatur')
ax.set_xlabel('Kategori')
ax.set_ylabel('Frekuensi')

# Menambahkan grid
ax.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(fig)
with st.expander("Penjelasan"):
    st.write(
        """
        1. Area di stasiun klimatologi Gucheng memiliki tren temperatur yang serupa selama tiga tahun, yakni mengalami suhu terpanas pada sekitar bulan Juni-Juli dan suhu terdingin antara bulan Januari-Februari.  
        
        2. Tren curah hujan memiliki pola yang serupa, yakni hujan tertinggi di bulan Juni-Juli. Hal ini memang cukup aneh karena di bulan itu memiliki suhu tertinggi namun juga memiliki curah hujan yang tinggi.  
        
        3. Korelasi antara Curah Hujan dan Temperatur sebesar 0.04 yang menunjukkan korelasi yang sangat lemah atau hampir tidak ada korelasi.  
        
        4. Nilai curah hujan didominasi oleh nilai di sekitar 0 sehingga variasi nilai sangat sedikit.  
        
        5. Clustering dilakukan dengan membagi suhu menjadi tiga kelas yakni kelas dingin, sedang, dan panas. Hasil menunjukkan bahwa suhu didominasi oleh suhu dingin.
        """
    )