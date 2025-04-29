import streamlit as st
import time

# Fungsi untuk menampilkan tampilan awal
def show_intro():
    st.title("Selamat Datang di Total Plate Count Calculator")
    st.write("Hitung Total Koloni Bakteri Anda dengan Mudah!")
    
    # Menampilkan gambar (pastikan Anda memiliki gambar di direktori yang sama)
    st.image("lab-background.jpg", use_column_width=True)
    
    # Menampilkan tombol untuk melanjutkan ke kalkulator
    if st.button("Masuk ke Kalkulator"):
        return True
    return False

# Fungsi untuk menampilkan kalkulator
def show_calculator():
    st.title("Total Plate Count Calculator")

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

# Menampilkan tampilan awal
if show_intro():
    # Jika tombol ditekan, tampilkan kalkulator
    show_calculator()
