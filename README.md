# Rekapitulasi Hasil Studi UGM
Program ini digunakan untuk rekapitulasi hasil studi mahasiswa UGM yang biasa menjadi kendala bagi mahasiswa yang ingin yudisium.

## Requirements
* Python 3.x
* Pandas

## Cara menggunakan
  1. Login [Palawa](https://palawa.ugm.ac.id/v14/index.php/system/auth/)
  2. Masuk ke Akademik > Mahasiswa > Rekap Nilai
  3. Blog dan copy seluruh tabel dari ujung kiri atas (**NO**) sampai ke nilai di ujung kanan bawah
  4. Paste di Excel dan save  
     ![Contoh](https://github.com/hermonjay/rekapitulasi_hasi_studi_ugm/blob/master/img/excel_sample.PNG)
  5. Jalankan program ```main.py``` pada terminal
  6. Masukkan nama file excel lengkap dengan ekstensi
     ![Contoh](https://github.com/hermonjay/rekapitulasi_hasi_studi_ugm/blob/master/img/input_sample_1.PNG)
  7. Informasi mengenai jumlah SKS yang telah diambil dan jumlah SKS di tiap nilai akan muncul     
  8. Jika ingin menghapus, masukkan ***KODE Mata Kuliah***, jika lebih dari dua, pisahkan dengan spasi
     ![Contoh](https://github.com/hermonjay/rekapitulasi_hasi_studi_ugm/blob/master/img/input_sample_2.PNG)
  9. Informasi lengkap setelah penghapusan akan muncul  
     ![Contoh](https://github.com/hermonjay/rekapitulasi_hasi_studi_ugm/blob/master/img/input_sample_3.PNG)

## Input gagal?
  1. Ganti variabel ```file``` pada baris 12 menjadi nama file,
     misal ```'rekap_nilai.xlsx'```
  2. Ganti variabel ```delete_subject``` pada baris 36 dan 37 menjadi list kode mata kuliah yang ingin dihapus,
     misal ```['MII1604', 'MMM2304', 'MIE2811']```
