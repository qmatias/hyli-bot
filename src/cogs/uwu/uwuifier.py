import random
import re

from utils import is_uri


class Uwuifier:
    def __init__(self,
                 faces: float = 0.05,
                 actions: float = 0.075,
                 stutters: float = 0.1,
                 words: float = 0.7,
                 exclamations: float = 1):
        self.faces_chance = faces
        self.actions_chance = actions
        self.stutters_chance = stutters
        self.words_chance = words
        self.exclamations_chance = exclamations
    
    rng = random.Random()

    faces: list[str] = ['(・`ω´・)', ';;w;;', 'OwO', 'UwU',
                        '>w<', '^w^', 'ÚwÚ', '^-^', ':3', 'x3']
    exclamations: list[str] = ['!?', '?!!', '?!?1', '!!11', '?!?!']
    actions: list[str] = [
        '*blushes*', '*whispers to self*', '*cries*', '*screams*', '*sweats*', '*twerks*',
        '*runs away*', '*screeches*', '*walks away*', '*sees bulge*', '*looks at you*',
        '*notices buldge*', '*starts twerking*', '*huggles tightly*', '*boops your nose*'
    ]
    uwu_map: list[list[str]] = [
        [r'(?:r|l)', 'w'],
        [r'(?:R|L)', 'W'],
        [r'n([aeiou])', 'ny\1'],
        [r'N([aeiou])', 'Ny\1'],
        [r'N([AEIOU])', 'Ny\1'],
        [r'ove', 'uv']
    ]

    SEPERATOR = ' '

    @staticmethod
    def get_capital_percentage(string: str):
        uppercase = len(re.findall(r'[A-Z]', string))
        total = len(re.findall(r'[A-Za-z]', string))
        return uppercase / total

    def uwuify_sentence(self, sentence: str):
        self.rng.seed(sentence)
        words = sentence.split(self.SEPERATOR)
        new_sentence = self.SEPERATOR.join(self.uwuify_word(w) for w in words)
        if sentence == new_sentence:
            new_sentence = new_sentence + self.SEPERATOR + \
                self.rng.choice(self.faces + self.actions)
        return new_sentence

    def uwuify_word(self, word: str):
        # uwuify the word
        if (not is_uri(word)):
            for (regex, replacement) in self.uwu_map:
                if self.rng.random() < self.words_chance:
                    word = re.sub(regex, replacement, word)

        # uwuify exclamations
        if self.rng.random() < self.exclamations_chance:
            word = re.sub(
                r'[?!]+$', lambda m: self.rng.choice(self.exclamations), word)

        # uwuify spaces
        face_threshold = self.faces_chance
        action_threshold = self.actions_chance + face_threshold
        stutter_threshold = self.stutters_chance + action_threshold

        try:
            first_character = word[0]
        except IndexError:
            first_character = None
        rng = self.rng.random()
        if (rng <= face_threshold and self.faces):
            word = word + ' ' + self.rng.choice(self.faces)
        elif (rng <= action_threshold and self.actions):
            word = word + ' ' + self.rng.choice(self.actions)
        elif (rng <= stutter_threshold and first_character and not is_uri(word)):
            stutter = self.rng.randint(1, 3)
            word = (first_character + '-') * stutter + word

        return word
