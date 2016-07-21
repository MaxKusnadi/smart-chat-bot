from gensim.models import word2vec

from app.constants import WORD2VEC_MODEL_PATH


class Word2Vec:

    def __init__(self):
        self.model = word2vec.Word2Vec.load_word2vec_format(WORD2VEC_MODEL_PATH, binary=True)

    def similarity_between_words(self, word1, word2):
        assert(word1.islower())
        assert(word2.islower())
        try:
            score = self.model.similarity(word1, word2)
        except KeyError:
            score = 0
        return score

if __name__ == "__main__":
    model = Word2Vec()
    print(model.similarity_between_words("get", "find") > 
          model.similarity_between_words("get", "delete"))