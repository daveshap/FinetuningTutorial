import openai
from time import time,sleep
from uuid import uuid4


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('openaiapikey.txt')

genres = [
    'romance & comedy',
    'crime & mystery',
    'action & adventure',
    'high fantasy',
    'science fiction',
    'horror & thriller'
]

modifiers = [
    'cerebral & suspenseful',
    'heartwarming & lighthearted',
    'tragic & heartwrenching',
    'supernatural & otherworldly',
    'action-packed & exciting',
    'gritty & dark',
]

places = [
    'France',
    'Japan',
    'England',
    'America',
    'South Africa',
    'India',
    'China',
    'Egypt',
    'Italy'
]

periods = [
    'the Renaissance',
    'the 1920s',
    'the 1960s',
    'the 1990s',
    'the near future',
    'the distant future',
]

def gpt3_completion(prompt, engine='text-davinci-002', temp=1.0, top_p=1.0, tokens=1000, freq_pen=0.0, pres_pen=0.0, stop=['asdfasdf', 'asdasdf']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            #text = re.sub('\s+', ' ', text)
            filename = '%s_gpt3.txt' % time()
            save_file('gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)


if __name__ == '__main__':
    count = 0
    for genre in genres:
        for modifier in modifiers:
            for place in places:
                for period in periods:
                    count += 1
                    prompt = open_file('prompt.txt')
                    prompt = prompt.replace('<<GENRE>>', genre)
                    prompt = prompt.replace('<<MODIFIER>>', modifier)
                    prompt = prompt.replace('<<PLACE>>', place)
                    prompt = prompt.replace('<<PERIOD>>', period)
                    prompt = prompt.replace('<<UUID>>', str(uuid4()))
                    print('\n\n', prompt)
                    completion = gpt3_completion(prompt)
                    outprompt = 'Genre: %s\nLocation: %s\nPeriod: %s\nModifier: %s\n\nPLOT OUTLINE: ' % (genre, place, period, modifier)
                    filename = (place + period + genre + modifier).replace(' ','').replace('&','') + '%s.txt' % time()
                    save_file('prompts/%s' % filename, outprompt)
                    save_file('completions/%s' % filename, completion)
                    print('\n\n', outprompt)
                    print('\n\n', completion)
                    if count > 500:
                        exit()
    #print(count)