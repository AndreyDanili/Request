from pprint import pprint
import requests


def get_files_list():
    files_url = 'https://api.stackexchange.com//2.3/questions?fromdate=1640044800&todate=1640217600&' \
                    'order=desc&sort=activity&tagged=python&site=stackoverflow'
    response = requests.get(files_url).json()
    return response


def get_question():
    titles = []
    all_question = get_files_list()
    for question_title in all_question['items']:
        titles.append(question_title['title'])
    pprint(titles)


if __name__ == '__main__':
    get_question()
