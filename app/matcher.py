from word2vec import Word2Vec
from query_parser import Query_Parser
from google import analyze_syntax

class Matcher:

    def __init__(self, all_funcs):
        self.all_funcs = all_funcs
        self.model = Word2Vec()
        self.query_parser = Query_Parser

    def match(self, query_string):
        syntax_json = analyze_syntax(query_string)
        query_object = self.query_parser.parse(syntax_json)
        func_score_pair = [(func, similarity_between_query_and_function(query_object, func))
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
        return score_func(max(obj_scores), max(verb_scores))

def score_func(obj_score, verb_score):
    return min(obj_score, verb_score)

if __name__ == "__main__":
    # from decorator import create_classroom
    from type import create
    from constants import CLASSROOM
    @create(CLASSROOM)
    def create_classroom():
        return True
    m = Matcher([create_classroom])
    print(m.match("Create a classroom."))
