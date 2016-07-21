from constants import CREATE_KEYWORDS, DELETE_KEYWORDS, QUERY_KEYWORDS, UPDATE_KEYWORDS

ALL_FUNCS = []

def create_decorator(behaviour_keywords):
    """
    Create a behaviour decorator, eg: query.

    Parameter:
    behaviour_keywords -- array of str, lower case verbs describing the behaviour

    eg.
    >> query = create_decorator(["get", "find"])
    """
    def behaviour(noun_keywords_):
        def decorator(fn):

            class Custom_Behaviour:

                def __init__(self):
                    self.verb_keywords = behaviour_keywords
                    self.noun_keywords = noun_keywords_

                def __str__(self):
                    return "<decorator.noun_keywords:{}>".format(self.noun_keywords)

                def __call__ (self, *args):
                    return fn(*args)

            cb = Custom_Behaviour()
            ALL_FUNCS.append(cb)
            return cb
        return decorator
    return behaviour



if __name__ == "__main__":
    from constants import CLASSROOM
    @create(CLASSROOM)
    def create_classroom():
        return True
    print(CREATE_KEYWORDS == create_classroom.verb_keywords)
    print(CLASSROOM == create_classroom.noun_keywords)
    print(create_classroom())