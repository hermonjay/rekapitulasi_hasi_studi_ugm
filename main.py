"""
Program rekapitulasi hasil studi, berguna untuk yudisium
Fitur: hitung IPK, jumlah SKS, jumlah SKS di tiap nilai,
       penghapusan SKS, keterangan IPK dan mata kuliah setelah penghapusan
Copyright by hermonjay       
"""

import pandas as pd
from utils import calculate_gpa, count_per_grade

# Persiapan data
file = input('Masukkan nama file: ')
rekap_sebelum = pd.read_excel(file)
rekap_sebelum = rekap_sebelum.drop(rekap_sebelum.index[0])
rekap_sebelum = rekap_sebelum.dropna()
del rekap_sebelum['NO']
rekap_sebelum = rekap_sebelum.set_index('KODE')

# Hitung SKS
total_sks_sebelum = rekap_sebelum['SKS'].sum()

# Hitung total BOBOT * SKS
total_bobot_sebelum = rekap_sebelum['SKS*BOBOT'].sum()

# Hitung IPK
ipk_sebelum = calculate_gpa(total_sks_sebelum, total_bobot_sebelum)

# SEBELUM
print("\n=====SEBELUM=============================")
print('\nJumlah SKS yang telah diambil: %d\n' % total_sks_sebelum)
count_per_grade(rekap_sebelum)
print('\nIPK: %.3f' % ipk_sebelum)

# UBAH NILAI
print("\n=====UBAH NILAI==========================")
delete_subject = input('\nMasukkan KODE yang ingin dihapus: ')
delete_subject = [x for x in delete_subject.split()]
rekap_sesudah = rekap_sebelum
delete_subject = ['MII1604', 'MMM2304']
rekap_hapus = pd.DataFrame(columns=rekap_sebelum.columns)

for i in delete_subject:
    for j in rekap_sesudah.index:
        if i == j:            
            rekap_hapus = rekap_hapus.append(rekap_sebelum.loc[i])
            rekap_sesudah = rekap_sesudah.drop(i)                    

# Hitung SKS
total_sks_sesudah = rekap_sesudah['SKS'].sum()

# Hitung total BOBOT * SKS
total_bobot_sesudah = rekap_sesudah['SKS*BOBOT'].sum()

# Hitung IPK
ipk_sesudah = calculate_gpa(total_sks_sesudah, total_bobot_sesudah)

print('\nMenghapus %d SKS' % (total_sks_sebelum - total_sks_sesudah))
print('Jumlah SKS menjadi: %d\n' % total_sks_sesudah)
count_per_grade(rekap_sesudah)
print('\nIPK menjadi: %.3f' % ipk_sesudah)

# KETERANGAN
print("\n=====KETERANGAN==========================")
print("\nTelah menghapus:")
print(rekap_hapus)