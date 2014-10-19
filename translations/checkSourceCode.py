"""
Since the translated source code should still keep the line numbers intact,
this script checks that the lines are loosely the same as the original.

This script works by comparing Python keywords, parentheses, module
identifiers, and other things that won't change in a translation. These are
called "aspects", and aspects will be universal across all Python code.

This is not fullproof, but it is a pretty good check.
"""

import unittest
import os
import re

stringPat = re.compile(r"""('.*?')|(".*?")""")
commentPat = re.compile(r"#(.*)")

# Whole world aspects will have the entire aspect word by itself.
WHOLE_WORD_ASPECTS = ('import', 'for', 'in', '<', '>', '<=', '>=', '!=', '=', '==', '+=', '-=', '%%s', '%%', '#', 'None', 'while', 'if', 'elif', 'else:', 'def', 'return', 'and', 'or', 'not', 'break', 'continue')
# Function aspects will have the name followed by an opening parenthesis.
FUNCTION_ASPECTS = ('range', 'len', 'print', 'input', 'append', 'randint', 'bool', 'int', 'str', 'float', 'list', 'tuple', 'dict', 'lower', 'upper', 'reverse', 'append', 'split', 'choice', 'join', 'sort', 'shuffle', 'abs', 'remove', 'chr', 'ord', 'isalpha', 'isupper', 'islower', 'remove', 'round', 'render', 'fill', 'circle', 'ellipse', 'polygon', 'rect', 'PixelArray', 'blit', 'update', 'quit', 'colliderect', 'scale', 'move_ip', 'set_pos')
# "Any" aspects can show up next to other characters (i.e. they're not whole words)
ANY_ASPECTS = ('[', ']', '(', ')')

def getAspects(filename):
    lineAspects = {}

    fo = open(filename)
    lineNum = 1
    for line in fo.readlines():
        # modify the python source to take out the strings so they don't confuse the unit tests
        line = line.replace('\\"', '').replace("\\'", '')
        line = stringPat.sub('STRING', line)
        # TODO - Need to detect multi-line strings.
        # modify the python source to remove comments
        line = commentPat.sub('COMMENT', line)

        aspects = {'whole':[], 'function':[], 'any':[], 'blank':False}

        if line.strip() == '':
            aspects['blank'] = True
            lineAspects[lineNum] = aspects
            lineNum += 1
            continue

        words = line.split()
        for wholeWordAspect in WHOLE_WORD_ASPECTS:
            if wholeWordAspect in words:
                aspects['whole'].append(wholeWordAspect)

        for functionAspect in FUNCTION_ASPECTS:
            if functionAspect + '(' in line:
                if 'Word(' in line:
                    continue # hack
                aspects['function'].append(functionAspect)

        for anyAspect in ANY_ASPECTS:
            if anyAspect in line:
                aspects['any'].append(anyAspect)

        lineAspects[lineNum] = aspects
        lineNum += 1
    fo.close()
    return lineAspects


# Load the metrics for the original English programs.
ORIG = {}
for pythonScript in ('AISim1', 'AISim2', 'AISim3', 'animation', 'bagels',
                     'buggy', 'bugs', 'cipher', 'coinFlips', 'collisionDetection',
                     'dodger', 'dodgerfullscreen', 'dragon', 'gorilla', 'guess',
                     'hangman', 'hangman2', 'hello', 'jokes', 'pygameHelloWorld',
                     'pygameInput', 'reversi', 'reversi_mini', 'sonar',
                     'spritesAndSounds', 'tictactoe'):
    ORIG[pythonScript] = getAspects(os.path.join('..', 'src', pythonScript + '.py'))




class TestSpanish(unittest.TestCase):
    def _compareTwoPrograms(self, origProgram, lang, translatedProgram):
        translatedAspects = getAspects(os.path.join(lang, 'src', translatedProgram + '.py'))
        for line in ORIG[origProgram].keys():
            stamp = (translatedProgram, line)
            self.assertEqual((stamp, ORIG[origProgram][line]['blank']), (stamp, translatedAspects[line]['blank']))
            self.assertEqual((stamp, ORIG[origProgram][line]['whole']), (stamp, translatedAspects[line]['whole']))
            self.assertEqual((stamp, ORIG[origProgram][line]['function']), (stamp, translatedAspects[line]['function']))
            self.assertEqual((stamp, ORIG[origProgram][line]['any']), (stamp, translatedAspects[line]['any']))


    def test_programs(self):
        LANG = 'es'
        programs = {'hello': 'hola',
                    'guess': 'adivinaElNúmero',
                    'dragon': 'dragón',
                    'hangman': 'verdugo',
                    'hangman2': 'verdugo2',}

        for original, translated in programs.items():
            self._compareTwoPrograms(original, LANG, translated)


if __name__ == '__main__':
    unittest.main()
