class Question:
    """"
    A class to represent a question.
    ...
    Attributes:
    ----------
    text: str
        question which will be asked to user
    answer: boolean
        information that the answer should be True or False"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer