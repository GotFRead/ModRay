
class ModuleLogicAutoAnswer:

    def __init__(self) -> None:
        pass

    def __delattr__(self, __name: str) -> None:
        pass


class Answer2Questions:
    Answer2Questions = {
        'Give_me_operator': 'Connection with operator...',
        'Give_me_path_to_join': '123.0.0.123'
    }

    @staticmethod
    def check_avalible_answer(question: str):
        if question in Answer2Questions.Answer2Questions.keys():
            print(Answer2Questions.Answer2Questions[question])


if __name__ == '__main__':
    pass
