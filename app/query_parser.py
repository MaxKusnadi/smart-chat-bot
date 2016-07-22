from app.constants import WH_TYPE

class Query:

    def __init__(self, syntax):
        self.syntax = syntax
        self.obj = None
        self.verb = None
        self.subj = None
        self.entities = None

    def is_valid(self):
        return self.obj and self.verb


class Query_Parser:

    def parse(self, syntax):
        syntax = trim_to_first_sentence(syntax)
        query = Query(syntax)
        query.obj = self.get_obj(syntax)
        query.verb = self.get_verb(syntax)
        query.subj = self.get_subj(syntax)
        if not query.obj:
            attr = self.get_attr(syntax)
            if attr:
                query.obj = attr
            else:
                query.obj = query.subj
        query.entities = self.get_entities(syntax)
        return query

    def get_attr(self, syntax):
        attr = next((token for token in syntax["tokens"]
                     if token["dependencyEdge"]["label"] == "ATTR" and token["lemma"] not in WH_TYPE), None)
        if attr:
            return attr["lemma"].lower()
        else:
            return None

    def get_obj(self, syntax):
        dobj = next((token for token in syntax["tokens"]
                     if "OBJ" in token["dependencyEdge"]["label"] and token["lemma"] not in WH_TYPE), None)
        if dobj:
            obj_index = syntax["tokens"].index(dobj)
            dobjs = [dobj] + [token for token in syntax["tokens"]
                              if token["dependencyEdge"]["headTokenIndex"]
                              == obj_index and
                              token["partOfSpeech"]["tag"] == "NOUN"]
            return " ".join([token["lemma"].lower()
                             for token in sorted(dobjs,
                                                 key=lambda token: token["text"]["beginOffset"])])
        else:
            return None

    def get_verb(self, syntax):
        root = next((token for token in syntax["tokens"]
                     if token["dependencyEdge"]["label"] == "ROOT"))
        if root["partOfSpeech"]["tag"] == "VERB":
            return root["lemma"].lower()
        else:
            return None

    def get_subj(self, syntax):
        subj = next((token for token in syntax["tokens"]
                     if  "SUBJ" in token["dependencyEdge"]["label"]), None)
        if subj:
            subj_index = syntax["tokens"].index(subj)
            subjs = [subj] + [token for token in syntax["tokens"]
                              if token["dependencyEdge"]["headTokenIndex"]
                              == subj_index and
                              token["partOfSpeech"]["tag"] == "NOUN"]
            return " ".join([token["lemma"].lower()
                             for token in sorted(subjs,
                                                 key=lambda token: token["text"]["beginOffset"])])
        else:
            return None

    def get_entities(self, syntax):
        nouns = [token for token in syntax["tokens"]
                 if token["partOfSpeech"]["tag"] == "NOUN"]
        result = []
        for noun in nouns:
            noun_index = syntax["tokens"].index(noun)
            group_noun = [noun] + [token for token in nouns
                                   if token["dependencyEdge"]["headTokenIndex"] == noun_index]
            result.append(" ".join([token["lemma"].lower()
                                    for token in sorted(group_noun,
                                                        key=lambda token: token["text"]["beginOffset"])]))
        return result


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
