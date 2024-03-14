meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "FOMO" : "Takut kehilangan hal-hal terbaru",
            "FYI" : "Informasi untukmu",
            "TYSM" : "Thank You So Much atau Terima kasih banyak",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("makna kata", word, "adalah", meme_dict[word])
else:
    print("makna kata tidak ditemukan")
