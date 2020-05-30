
import xml.etree.ElementTree as ET


def parse_xml(file_name):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    return root


def xml_list(file_pasred):
    xml_items = file_pasred.findall('channel/item')
    description_list = []
    for item in xml_items:
        description = item.find('description')
        description_list.extend(description.text.split())
    return description_list


def top_ten(des_list):
    word_dict = {}
    top_ten_list = []
    for word in des_list:
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


top_ten(xml_list(parse_xml('newsafr.xml')))
