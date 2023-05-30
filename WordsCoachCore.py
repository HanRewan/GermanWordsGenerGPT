from DictCore import *
import random
import inspect
import os


class WordsCoach:

    def __init__(self, dict):
        self.dict = self.reformDict(dict)
        self.function_dict = {
            "Quest": "BatchQuestions",
            "ls": "list"
        }

        running = True

        while running:

            data = input("WordsCoach" + "$ ").split()

            if len(data) == 0:
                continue
            if data[0] == "exit":
                break

            if data[0] in self.function_dict:
                data[0] = self.function_dict[data[0]]
            else:
                print("Такої команди не існує. Щоб побачити перелік усіх команди введіть команду help.")
                continue

            curr_function = getattr(WordsCoach, data[0])

            for i in range(len(data)):
                if data[i].isdigit():
                    data[i] = int(data[i])

            data[0] = self

            argssign = str(inspect.signature(curr_function))
            argsstr = ""
            for i in range(len(argssign)):
                if i == 0 or i == len(argssign) - 1:
                    continue
                argsstr += argssign[i]

            args = argsstr.split(", ")

            neclen = 0
            if args[len(args) - 1] == "*args":
                neclen = len(args)
            else:
                for elem in args:
                    if not ('=' in elem):
                        neclen += 1
            if neclen > len(data):
                print("Був пропущенний один з обов'язкових аргументів функції")
                print(args)
                continue

            curr_function(*data)

    def reformDict(self, dict):
        for theme in dict:
            for i in range(len(dict[theme])):
                dict[theme][i] = Word(dict[theme][i])

        return dict



    def AskQuestions(self, batch):
        play = 1
        while play:
            wrong = 0
            random.shuffle(batch)
            for word in batch:
                ans = str(input(word.translation + " - "))

                if ans != word.phrase:
                    wrong = 1
                    print("Wrong answer.\n" + word.translation + " - " + word.phrase)
                    for i in range(2):
                        input(word.translation + " - ")

            if not wrong:
                play = 0
            input("After entering terminal will be cleared. ")
            os.system('cls' if os.name == 'nt' else 'clear')

    def BatchQuestions(self, name, size):
        batch = []
        for word in self.dict[name]:
            batch.append(word)
            if len(batch) == size:
                self.AskQuestions(batch)
                batch.clear()

        if len(batch) > 0:
            self.AskQuestions(batch)
            batch.clear()

    def list(self):
        for theme in self.dict:
            print(theme)