import streamlit as st
import time

# Judul aplikasi
st.title("Total Plate Count Calculator")

# Deskripsi aplikasi
st.write("Hitung Total Koloni Bakteri Anda dengan Mudah!")

# Input untuk jumlah koloni
colony_count = st.number_input("Jumlah Koloni:", min_value=0, step=1)

# Input untuk volume sampel
sample_volume = st.number_input("Volume Sampel (mL):", min_value=0.0, step=0.1)

# Tombol untuk menghitung
if st.button("Hitung"):
    # Menampilkan animasi loading
    with st.spinner("Menghitung..."):
        time.sleep(2)  # Simulasi waktu pemrosesan
        if sample_volume > 0:
            total_plate_count = colony_count / sample_volume
            st.success(f"Hasil: Total Plate Count adalah {total_plate_count:.2f} koloni/mL")
        else:
            st.error("Volume sampel harus lebih besar dari 0.")

# Informasi tambahan
st.write("### Apa itu Total Plate Count?")
st.write("Total Plate Count (TPC) adalah metode untuk menghitung jumlah koloni mikroorganisme dalam sampel.")

st.write("### Tips untuk Penghitungan yang Akurat:")
st.write("- Pastikan untuk menghitung koloni dengan hati-hati.")
st.write("- Gunakan volume sampel yang tepat untuk hasil yang akurat.")

# Footer
st.write("Kontak: info@tpccalculator.com")
st.write("© 2023 TPC Calculator. Semua hak dilindungi.")
