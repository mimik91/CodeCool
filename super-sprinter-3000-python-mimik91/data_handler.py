import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
FILE_PATH='/home/dominik/Desktop/CodeCool/super-sprinter-3000-python-mimik91/test/data.csv'


def get_all_user_story():
    with open(FILE_PATH, 'rt')as f:
        stories=csv.reader(f)
        stories_dic={}
        n=0
        for row in stories:
            stories_dic[n]=row
            n=n+1
        del stories_dic[0]
        return stories_dic



get_all_user_story()