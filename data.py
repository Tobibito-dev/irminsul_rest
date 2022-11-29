import os
import json

path = './data'

data = {}


def update_data():
    for dirname in os.listdir(path):
        dir_path = os.path.join(path, dirname)
        data[dirname] = {}
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            with open(file_path, 'r') as file:
                data[dirname][filename.replace('.json', '')] = json.loads(file.read())
