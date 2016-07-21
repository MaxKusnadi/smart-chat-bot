from word2vec import Word2Vec
from query_parser import Query_Parser
from google import analyze_syntax
from json import loads

class Matcher:

    def __init__(self, all_funcs):
        self.all_funcs = all_funcs
        self.model = Word2Vec()
        self.query_parser = Query_Parser

    def match(self, query_string):
        syntax_json = loads(analyze_syntax(query_string))
        query_object = self.query_parser.parse(syntax_json)

    def score_func(self, )
