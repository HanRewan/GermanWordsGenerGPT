import WordsCoachCore
import json



with open('DictGe.json') as json_file:
    data = json.load(json_file)
    Coach = WordsCoachCore.WordsCoach(data)
