class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

    def __str__(self):
        return f"{self.data}"
