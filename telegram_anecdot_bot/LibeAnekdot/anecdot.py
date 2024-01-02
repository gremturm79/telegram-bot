import random


class Anecdote:

    @classmethod
    def anec_mixed(cls):
        with open('mixed/mixed.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        anec = content.split('\n')
        anc = anec[random.randint(1, 250)]
        return anc

    @classmethod
    def anec_sundry(cls):
        with open('sundry/sundry_1.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        anec = content.split('\n')
        anc = anec[random.randint(1, 250)]
        return anc

    @classmethod
    def anec_national(cls):
        with open('national/nation.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        anec = content.split('\n')
        anc = anec[random.randint(1, 250)]
        return anc