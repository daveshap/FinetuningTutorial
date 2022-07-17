import os
import json


src_dir = 'completions/'
prompt_dir = 'prompts/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        completion = open_file(src_dir + file)
        prompt = open_file(prompt_dir + file)
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)
    with open('plots.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')