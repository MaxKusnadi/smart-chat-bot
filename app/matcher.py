from app.word2vec import Word2Vec
from app.query_parser import Query_Parser
from app.google import analyze_syntax
from app.constants import SCORE_THRESHOLD

class Matcher:

    def __init__(self, all_funcs):
        self.all_funcs = all_funcs
        self.model = Word2Vec()
        self.query_parser = Query_Parser()

    def match(self, query_string):
        syntax_json = analyze_syntax(query_string)
        print(syntax_json)
        query_object = self.query_parser.parse(syntax_json)
        print("obj:{}\nverb:{}\n".format(query_object.obj, query_object.verb))
        if not query_object.is_valid():
            return None
        func_score_pair = [(func, self.similarity_between_query_and_function(query_object, func))
                           for func in self.all_funcs]
        func_score_pair = sorted(func_score_pair, key=lambda pair:pair[1],
                                 reverse=True)
        if func_score_pair[0][1] > SCORE_THRESHOLD:
            return func_score_pair[0][0]
        else:
            return None


    def similarity_between_query_and_function(self, query, func):
        obj_scores = [self.model.similarity_between_words(query.obj, noun)\
                      for noun in func.noun_keywords]
        verb_scores = [self.model.similarity_between_words(query.verb, verb)\
                       for verb in func.verb_keywords]
        print("{},{:.2},{:.2}".format(func,float(max(obj_scores)),float(max(verb_scores))))
        return score_func(max(obj_scores), max(verb_scores))

def score_func(obj_score, verb_score):
    return min(obj_score, verb_score)

if __name__ == "__main__":
    from functions import *
    from constants import ALL_FUNCS
    m = Matcher(ALL_FUNCS)
    while(1):
        print(m.match(input("input:\n")))
