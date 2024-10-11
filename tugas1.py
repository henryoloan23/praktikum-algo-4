n = int(input('Jumlah = '))

for baris in range(n, 0 , -1):
    for kolom in range(1, baris + 1):
        print(baris, end='')
    print()