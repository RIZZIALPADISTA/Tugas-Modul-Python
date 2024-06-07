def huruf_besar(huruf):
    jumlah = 0
    for teks in huruf:
        if teks.isupper():
            jumlah = jumlah + 1
    return jumlah