def calculate_gpa(total_SKS, total_bobot):
    return total_bobot / total_SKS

def count_per_grade(dataFrame):
    a = 0
    a_min = 0
    a_per_b = 0
    b_plus = 0
    b = 0
    b_min = 0
    b_per_c = 0
    c_plus = 0
    c = 0
    c_min = 0
    d = 0
    e = 0
    for i in range(len(dataFrame['NILAI'])):
        if dataFrame['NILAI'][i] == 'A': a += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'A-': a_min += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] =='A/B': a_per_b += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'B+': b_plus += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'B': b += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'B-': b_min += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'B/C': b_per_c += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'C+': c_plus += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'C': c += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'C-': c_min += dataFrame['SKS'][i]
        elif dataFrame['NILAI'][i] == 'D': d += dataFrame['SKS'][i]
        else: e += dataFrame['SKS'][i]    
        
    print('Nilai A: %d \tNilai A-: %d \tNilai A/B: %d \tNilai B+: %d' % (a, a_min, a_per_b, b_plus))
    print('Nilai B: %d \tNilai B-: %d \tNilai B/C: %d \tNilai C+: %d' % (b, b_min, b_per_c, c_plus))
    print('Nilai C: %d \tNilai C-: %d \tNilai D  : %d \tNilai E : %d' % (c, c_min, d, e))

    