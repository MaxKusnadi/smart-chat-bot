

class Query:

    def __init__(self, syntax):
        self.syntax = syntax
        self.obj = None
        self.verb = None

    def is_valid(self):
        return self.obj and self.verb


class Query_Parser:

    def parse(self, syntax):
        syntax = trim_to_first_sentence(syntax)
        query = Query(syntax)
        query.obj = self.get_obj(syntax)
        query.verb = self.get_verb(syntax)
        return query

    def get_obj(self, query):
        dobj = next((token for token in query["tokens"]
                     if token["dependencyEdge"]["label"] == "DOBJ"), None)
        if dobj:
            obj_index = query["tokens"].index(dobj)
            dobjs = [dobj] + [token for token in query["tokens"]
                              if token["dependencyEdge"]["headTokenIndex"]
                              == obj_index and
                              token["partOfSpeech"]["tag"] == "NOUN"]
            return " ".join([token["lemma"].lower()
                             for token in sorted(dobjs,
                                                 key=lambda token: token["text"]["beginOffset"])])
        else:
            return None

    def get_verb(self, query):
        root = next((token for token in query["tokens"]
                     if token["dependencyEdge"]["label"] == "ROOT"))
        if root["partOfSpeech"]["tag"] == "VERB":
            return root["lemma"].lower()
        else:
            return None


def trim_to_first_sentence(syntax):
    if len(syntax["sentences"]) == 1:
        return syntax

    break_index = syntax["sentences"][1]["text"]["beginOffset"]
    syntax["tokens"] = [token for token in syntax["tokens"]
                        if token["text"]["beginOffset"] < break_index]
    return syntax

if __name__ == "__main__":
    from json import loads
    with open("test/google_json_output.sample", "r") as f:
        syntax = f.read()
        print(syntax != "")
        qp = Query_Parser()
        q = qp.parse(loads(syntax))
        print(q.noun)
        print(q.verb)
