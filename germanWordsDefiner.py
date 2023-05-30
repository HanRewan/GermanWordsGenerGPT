import openai
import json

api_key = "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"
openai.api_key = api_key


def generate_question(them):
    return "Please give me at least 16 main German words related to " + them + " in the format: word - article (if it does not have article just put # here) - type of the word (noun, verb, e.t.) - translation (in ukrainian). Please don`t give any remarks, explanations or additional information."

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]


def getWordList(topic):
    word_list = generate_response(generate_question(topic)).split("\n")
    word_list[:] = (value for value in word_list if value != '')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split(' - ')
        word_list[i][1] = word_list[i][1].lower()
        word_list[i][2] = word_list[i][2].lower()
    word_list[:] = (value for value in word_list if len(value) == 4)
    print(topic + " successfully loaded.")
    print(word_list)
    return word_list


Word_dict = {}

with open("Themes", "r") as file:
    for line in file:
        line = line.replace('    ', '').replace("\n", '')
        word_list = getWordList(line)
        Word_dict[line] = word_list


print(Word_dict)

with open("DictGe.json", "w") as outfile:
    json.dump(Word_dict, outfile)

