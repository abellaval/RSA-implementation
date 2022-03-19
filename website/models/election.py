class Election:

    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 candidates,
                 results=None):
        if results is None:
            results = []
        self.id = id
        self.name = name
        self.description = description
        self.candidates = candidates
        self.results = results
