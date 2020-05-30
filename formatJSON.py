
import json


def read_json(file_name):
    with open(file_name, encoding='utf-8') as fj:
        data = json.load(fj)
        data_list = []
        for item in data['rss']['channel']['items']:
            data_list.append(item['description'])
    return data_list


def top_ten_json(description):
    word_dict = {}
    top_ten_list = []
    for item in description:
        words = item.split()
        for word in words:
            if len(word) > 6:
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
                else:
                    word_dict[word.lower()] = 1
            else:
                continue
    for key, value in word_dict.items():
        top_ten_list.append((value, key))
    top_ten_list.sort(reverse=True)
    for item in top_ten_list[0:10]:
        print(f'{item[1]}: {item[0]}')


top_ten_json(read_json('newsafr.json'))
