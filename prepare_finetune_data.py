import os
import json


src_dir = 'convos/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        lines = open_file(src_dir + file).splitlines()
        completion = lines.pop(-1)
        prompt = '\n'.join(lines).strip()
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)
    with open('survey.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')