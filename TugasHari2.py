# soal no 1

# Persiapan membuat data
import pandas as pd
import random

pelajaran = ['Matematika', 'Fisika', 'Biologi', 'Kimia', 'Geologi', 'Ekonomi']
kelas = ['12A', '12B', '12C', '12D']

hasil_nilai = {
    'siswa_id' : range(1, 21),
    'pelajaran' : [random.choice(pelajaran) for i in range(20)],
    'nilai' : [random.choice(range(0, 100)) for i in range(20)],
    'jenis-kelamin' : [random.choice(['laki-laki', 'perempuan']) for i in range(20)],
    'kelas' : [random.choice(kelas) for i in range(20)]
}

df = pd.DataFrame(hasil_nilai)
df.head()

# Lakukan indexing terhadap dataframe untuk mengakses column nilai dan kelas saja

list_ambil = ['nilai', 'kelas']
df[list_ambil]

# Lakukan indexing terhadap dataframe untuk mengakses row 5 sampai 10 beserta column pelajaran dan nilai

df.iloc[5:11, 1:3]

# soal no 2

# Tampilkan semua data siswa pada mata pelajaran Ekonomi dan Fisika

ekonomi = df['pelajaran'] == 'Ekonomi'
fisika = df['pelajaran'] == 'Fisika'

df[(ekonomi) | (fisika)] 

# Tampilkan semua data siswa yang mempunyai nilai lebih dari 50 di mata pelajaran Kimia

kimia = df['pelajaran'] == 'Kimia' 
nilai = df['nilai'] > 50

df[(kimia) & (nilai)]

# Tampilkan semua data yang mempunyai nilai lebih dari 70, berjnis kelamin perempuan dan di kelas 12C

nilai = df['nilai'] > 70
gender = df['jenis-kelamin'] == 'perempuan'
kelas = df['kelas'] == '12C'

df[(nilai) & (gender) & (kelas)]

# soal no 3

# lakukan data transformasi terhadap column 'nilai' dengan fungsi transformasi, berikut rumus dari normalisasi

def transformasi(x):
    custom = x - x.min() / x.max() - x.min()
    return custom

df[['nilai']].apply(transformasi)