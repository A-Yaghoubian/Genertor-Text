import random
import os

dir = os.path.dirname(__file__)
def generate(tweets_num, pos_dict, lens):
    generated_texts = []
    for num in range(tweets_num):
        generated_text = ''
        text_len = random.randint(min(lens), max(lens))
        for index in range(text_len):
            words = list(pos_dict[index].keys())
            freqs = list(pos_dict[index].values())
            selected_word = random.choices(words, freqs)[0]
            generated_text = generated_text + selected_word + ' '

        generated_texts.append(generated_text)
        with open(dir + '/generatedText.txt', 'a+') as f:
            f.write(generated_text + '\n')

    return generated_texts

