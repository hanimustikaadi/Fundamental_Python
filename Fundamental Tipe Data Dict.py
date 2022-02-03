"""
Tipe Data Dictionary menghubungkan antara Key dan Value
Kvp = Key Value Pair
Dictionary= kamus
"""

kamus_data_ing = {'anak':'son','istri':'wife','ayah':'father','ibu':'mother'}

print(kamus_data_ing)
print(kamus_data_ing['anak'])
print(kamus_data_ing['istri'])
print(kamus_data_ing['ayah'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')

data_dari_server_gojek = {
    'tanggal' : '2020-06-10',
    'driver list' : [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}

print (data_dari_server_gojek)
print (f"\nDriver di sekitar sini {data_dari_server_gojek['driver list']}")
print (f"\nDriver di sekitar sini {data_dari_server_gojek['driver list'][0]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver list'][0]['jarak']} meter")
