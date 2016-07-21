from gensim.models.word2vec import Word2Vec
model = Word2Vec.load_word2vec_format("static/word2vec_model.bin", binary=True)

if __name__ == "__main__":
    while 1:
        print(model.most_similar(input()))