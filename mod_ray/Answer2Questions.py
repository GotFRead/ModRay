import json
from fuzzywuzzy import fuzz

class Service:
    Services_message = {
        'Give_me_operator': 'Connection with operator...',
        'Give_me_path_to_join': '123.0.0.123',
        'Start_message': 'Service started!',
        'Service_fail':'Service raise error!'
    }
    def __init__(self, request, params) -> None:
        self.config = config['autoanswer']
        self.accuracy = 80 if 'accuracy' not in params else params['accuracy']
        self.request = request

    def get_answer(self):
        list_results = list()
        for request_from_config in self.config:
            list_results.append(int(fuzz.token_sort_ratio(request_from_config, self.request)))
        
        max_acc = max(list_results)

        if max_acc < self.accuracy:
            return f"I don't know answer on this question: {self.request}" 
        else:
            return self.get_answer_to_position(list_results.index(max_acc))

    def get_answer_to_position(self, position):
        count = 0
        for answer in self.config:
            if position == count:
                return self.config[answer]
            count +=1


def get_config(path_to_config = r'C:\Users\Aleksey ^_^\Desktop\ModRay\ModRay\mod_ray\configs\a2q.ini'):
    with open(path_to_config, 'r') as save:
        config = json.load(save)
        if config is not None:
            return config
        else:
            raise FileNotFoundError
    
config = get_config()

if __name__ == '__main__':
    pass
