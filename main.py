from mod_ray import Answer2Questions
from tests import main_test
from flask import Flask
from flask import request
from flask import abort
from enum import Enum

import logging
import asyncio
import os

class FieldMessage(str, Enum):
    QUESTION = 'question' 
    ANSWER = 'answer'
    PARAMS = 'params'
    

TemplateRequest = {
    FieldMessage.QUESTION: '',
    FieldMessage.PARAMS: {}
} 

TemplateReponse = {
    FieldMessage.ANSWER: ''
} 

def create_logger(logger_name):
    logger = logging.getLogger(str(logger_name))
    logger.setLevel(logging.INFO)

    file_logger = logging.FileHandler('service_log.txt')

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_logger.setFormatter(formatter)

    logger.addHandler(file_logger)
    return logger


logger = create_logger("Service main thread")

def create_error_response(field_with_error):
    response = TemplateReponse
    response[FieldMessage.ANSWER] = f'Field {field_with_error} NOT found!'
    return response

def main(port):
    service = Flask('Service main thread')

    @service.route('/get_answer', methods=['POST'])
    def get_answer():
        for field in TemplateRequest.keys():
            if field not in request.json:
                return create_error_response(field)
            
        response = TemplateReponse
        response[FieldMessage.ANSWER] = Answer2Questions.Service(request.json[FieldMessage.QUESTION], FieldMessage.PARAMS).get_answer()
        return response
    logger.info(f'Server start!')
    service.run(port=port, debug=False)


if __name__ == '__main__':
    main(port=25000)
