import pickle
import streamlit as st
from streamlit_option_menu import option_menu

model = pickle.load(open('prediksi_mobil.sav', 'rb'))

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="grid-1x2",
        default_index=0,
    )

if selected == "Home":
    st.title(f"WELCOME TO CARSELL")
    st.markdown("Selamat datang di CARSELL! Website ini dirancang untuk membantu Anda memperkirakan harga mobil bekas dengan cepat dan akurat menggunakan model AI berbasis regresi linear. Pengalaman pengguna yang sederhana memastikan bahwa setiap orang dapat dengan mudah memperoleh estimasi harga mobil mereka.")
    
    st.title("")
    st.title(f"Antarmuka Pengguna Intuitif")
    st.markdown("Desain antarmuka yang bersih dan sederhana memungkinkan pengguna dengan mudah mengakses fitur-fitur prediksi harga. Anda hanya perlu memasukkan beberapa detail tentang mobil Anda untuk memulai proses.")
    
    st.title("")
    st.title(f"Input yang Dibutuhkan")
    st.markdown("Tahun Mobil: Masukkan tahun pembuatan mobil untuk memperoleh estimasi yang lebih akurat.")
    st.markdown("Kilometer Mobil (KM): Tentukan total jarak yang telah ditempuh oleh mobil.")
    st.markdown("Pajak Mobil: Input jumlah pajak yang terkait dengan mobil Anda.")
    st.markdown("Konsumsi BBM Mobil: Berikan informasi tentang konsumsi bahan bakar mobil (kilometer per liter).")
    st.markdown("Engine Size: Tentukan ukuran mesin mobil dalam liter.")

elif selected == "Projects":
    st.title(f"Sistem Prediksi Harga Mobil Bekas")
    
    year = st.number_input('Input Tahun Mobil')
    mileage = st.number_input('Input Km Mobil')
    tax = st.number_input('Input Pajak Mobil')
    mpg = st.number_input('Input Konsumsi BBM Mobil')
    engineSize = st.number_input('Input Engine Size')

    predict = ''

    if st.button('Prediksi Harga'):
        predict = model.predict([[year, mileage, tax, mpg, engineSize]])
        st.write('Prediksi Harga Mobil (Pound) : ', predict)
        st.write('Prediksi Harga Mobil (IDR) :', predict*19000)

elif selected == "Contact":
    st.title(f"Nama Anggota Kelompok :")
    st.title("")
    st.header("1. Robby Alamsyah S. P - 21082010166")
    st.header("2. Diky Wahyu Afandi - 22101021155")
    st.header("3. Khoirun Alfi Shahriani - 21030214014")
    st.header("4. Khusnul Khotimah - 22101091164")
    st.header("5. Moh. Alfarabi Susanto - 212410102090")
    st.header("6. Mutma Innah - 20051214026")
    st.title("")
    st.title("")
    st.title("")
    st.markdown(" Presented by Kelompok 7 - ENGINE")
