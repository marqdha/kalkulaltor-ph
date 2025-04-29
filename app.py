import streamlit as st

# Judul aplikasi
st.title("Perhitungan Total Plate Count (TPC)")

# Deskripsi aplikasi
st.write("""
Aplikasi ini digunakan untuk menghitung Total Plate Count (TPC) berdasarkan jumlah koloni yang terhitung,
faktor pengenceran, dan banyaknya faktor pengenceran. 
Standar jumlah koloni yang diterima untuk perhitungan adalah antara 25 hingga 250 koloni.
Silakan masukkan nilai di bawah ini untuk melakukan perhitungan.
""")

# Input jumlah koloni
jumlah_koloni = st.number_input("Masukkan Jumlah Koloni (25-250):", min_value=0, step=1)

# Input faktor pengenceran
faktor_pengenceran = st.number_input("Masukkan Faktor Pengenceran:", min_value=1, step=1)

# Input banyaknya faktor pengenceran
banyak_faktor_pengenceran = st.number_input("Masukkan Banyaknya Faktor Pengenceran:", min_value=1, step=1)

# Tombol untuk menghitung TPC
if st.button("Hitung TPC"):
    if 25 <= jumlah_koloni <= 250:
        # Menghitung TPC
        tpc = (jumlah_koloni * faktor_pengenceran) / banyak_faktor_pengenceran
        st.success(f"Total Plate Count (TPC): {tpc:.2f} CFU/mL")
    else:
        st.error("Jumlah koloni harus antara 25 dan 250.")
