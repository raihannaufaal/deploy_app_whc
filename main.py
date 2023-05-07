import streamlit as st

st.title(':green[Menghitung (%) Kemampuan Daging Dalam Mengikat Air]')

st.write("---")
st.write('**Webapps ini dibuat untuk memudahkan dalam menghitung (%) kemampuan daging dalam mengikat air (Water Holding Capacity) menggunakan metode kertas saring.**')
st.write('Water holding capacity (WHC), merupakan kemampuan untuk menahan air yang terdapat pada jaringan daging sehingga dijadikan salah satu indikator yang digunakan untuk mengetahui kemampuan daging dalam mengikat air.')
st.write("---")

st.write('**Rumus Mencari Daya Ikat Air (WHC)**')
st.write('Luas bercak air = πr²')
st.write('mg H2O = (luas bercak air(cm²)/0.0948) - 8.0')
st.write('Kadar area basah = (mg H2O/bobot sampel) × 100%')
st.write('Daya ikat air (WHC) = % Kadar air - % Kadar area basah')
st.write('---')

jari_jari=st.number_input('Masukkan besarnya jari-jari yang terukur pada kertas milimeter (_cm_)')
bobot_sampel=st.number_input('Masukkan bobot sampel daging yang ditimbang (_mg_)')
kadar_air=st.number_input('Masukkan nilai kadar air dalam daging (_biasanya berkisar antara 60-70%_)')
tombol=st.button('Hitung')
if tombol:
    luas_bercak_air=round(3.14*(jari_jari**2),4)
    mg_H2O=round((luas_bercak_air/0.0948)-(8.0),4)
    kadar_area_basah=round((mg_H2O/bobot_sampel)*(100),2)
    daya_ikat_air=round(kadar_air-kadar_area_basah,2)
    st.success(f'Luas Bercak Air adalah {luas_bercak_air} cm²')
    st.success(f'mg H2O adalah {mg_H2O} mg')
    st.success(f'Kadar Area Basah adalah {kadar_area_basah} %')
    st.success(f'Daya Ikat Air Dari Sampel Daging adalah {daya_ikat_air} %')
    
else:
    result="Isikan terlebih dahulu"



    

