import openai
import json

api_key = "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"
openai.api_key = api_key


#def generate_question():
    #return "Please give me at least 16 main German articles for all genders and cases in the format: article - word ending in this case and gender - type of the word (noun, verb, e.t.) - gender and case. Please don`t give any remarks, punkts, explanations or additional information."

def generate_question():
    return "Please give me at least 30 main German verbs in the format: word - article (if it does not have article just put # here) - type of the word (noun, verb, e.t.) - translation. Please don`t give any remarks, punkts, explanations or additional information."

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


def getWordList(name):
    word_list = generate_response(generate_question()).split("\n")
    word_list[:] = (value for value in word_list if value != '')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split(' - ')
        word_list[i][1] = word_list[i][1].lower()
        word_list[i][2] = word_list[i][2].lower()
    word_list[:] = (value for value in word_list if len(value) == 4)
    print(name + " successfully loaded.")
    print(word_list)
    return word_list


with open('DictGe.json') as json_file:
    Word_dict = json.load(json_file)

Word_dict["mainVerbs"] = getWordList("mainVerbs")
print(Word_dict)
input()
with open("DictGe.json", "w") as outfile:
    json.dump(Word_dict, outfile)
