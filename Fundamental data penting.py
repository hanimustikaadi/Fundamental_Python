print('tipe data saklar = tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print("\ntipe data list\daftar/array")
anak = ['Eko','Dwi','Tri','Catur']
print(anak)
anak.append('Limo')
print(anak)

print('Sapa anak ke 2')
print(f'\nHai {anak[1]}')

print('Sapa semua anak')
for a in range(0, len(anak)):
    print(f'{a+1}, Hai {anak[a]}')