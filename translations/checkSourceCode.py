#! python3
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
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    DEBUG = True
    del sys.argv[1]
else:
    DEBUG = False

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

    fo = open(filename, encoding='utf-8')
    lineNum = 1
    for line in fo.read().split('\n'):
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




class TestPrograms(unittest.TestCase):
    def _checkEncoding(self, lang, translatedProgram):
        try:
            fo = open(os.path.join(lang, 'src', translatedProgram + '.py'), encoding='utf-8')
            fo.read()
            fo.close()
        except:
            print('Error with encoding of ' + translatedProgram + '.py')
            raise

    def _compareTwoPrograms(self, lang, origProgram, translatedProgram):
        if DEBUG: print(origProgram, translatedProgram)
        translatedAspects = getAspects(os.path.join(lang, 'src', translatedProgram + '.py'))
        for line in ORIG[origProgram].keys():
            stamp = (translatedProgram, line)
            if DEBUG: print(lang, translatedProgram, line)
            self.assertEqual((stamp, ORIG[origProgram][line]['blank']), (stamp, translatedAspects[line]['blank']))
            self.assertEqual((stamp, ORIG[origProgram][line]['whole']), (stamp, translatedAspects[line]['whole']))
            self.assertEqual((stamp, ORIG[origProgram][line]['function']), (stamp, translatedAspects[line]['function']))
            self.assertEqual((stamp, ORIG[origProgram][line]['any']), (stamp, translatedAspects[line]['any']))

    def _check(self, lang, origProgram, translatedProgram):
        self._checkEncoding(lang, translatedProgram)
        self._compareTwoPrograms(lang, origProgram, translatedProgram)

    def test_es_programs(self):
        self._check('es', 'hello', 'hola')
        self._check('es', 'guess', 'adivinaElNúmero')
        self._check('es', 'dragon', 'dragón')
        self._check('es', 'hangman', 'ahorcado')
        self._check('es', 'hangman2', 'ahorcado2')
        self._check('es', 'AISim2', 'es_AISim2')
        self._check('es', 'AISim3', 'es_AISim3')
        self._check('es', 'jokes', 'chistes')
        self._check('es', 'animation', 'animacion')
        self._check('es', 'cipher', 'cifrado')
        self._check('es', 'dodger', 'evasor')
        self._check('es', 'bagels', 'panecillos')
        self._check('es', 'tictactoe', 'tateti')
        self._check('es', 'pygameHelloWorld', 'pygameHolaMundo')
        self._check('es', 'collisionDetection', 'deteccionColision')
        self._check('es', 'pygameInput', 'pygameEntrada')
        self._check('es', 'spritesAndSounds', 'spritesYsonidos')

    def test_sv_programs(self):
        self._check('sv', 'hello', 'hello')
        self._check('sv', 'sonar', 'sonar')
        self._check('sv', 'coinFlips', 'coinFlips')
        self._check('sv', 'guess', 'guess')
        self._check('sv', 'reversi', 'reversi')
        self._check('sv', 'AISim3', 'AISim3')
        self._check('sv', 'buggy', 'buggy')
        self._check('sv', 'bagels', 'bagels')
        self._check('sv', 'AISim2', 'AISim2')
        self._check('sv', 'dragon', 'dragon')
        self._check('sv', 'AISim1', 'AISim1')
        self._check('sv', 'hangman', 'hangman')
        self._check('sv', 'tictactoe', 'tictactoe')
        self._check('sv', 'jokes', 'jokes')
        self._check('sv', 'reversi_mini', 'reversi_mini')


    def test_id_programs(self):
        self._check('id', 'guess', 'tebak')
        self._check('id', 'hangman', 'hangman')
        self._check('id', 'hello', 'halo')
        self._check('id', 'buggy', 'ngebug')
        self._check('id', 'coinFlips', 'lemparKoin')
        self._check('id', 'dragon', 'naga')


    def test_fr_programs(self):
        self._check('fr', 'hello', 'bonjour')


if __name__ == '__main__':
    unittest.main()
