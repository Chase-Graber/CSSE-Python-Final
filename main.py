import random
from tkinter import *

# Dictionary of all verbs and their conjugations
"""
Verbs are presented in the following form:
     verb | [0]
---------------------
      ich | [1]
       du | [2]
er/sie/es | [3]
      wir | [4]
      ihr | [5]
  Sie/sie | [6]
"""

pronouns = ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'Sie/sie']

verbs = {
    'sein' : ['to be', 'bin', 'bist', 'ist', 'sind', 'seid', 'sind'],
    'hei\u00dfen' : ['to be called', 'heisse', 'heisst', 'heisst', 'heissen', 'heisst', 'heissen'],
    'kommen' : ['to come', 'komme', 'kommst', 'kommt', 'kommen', 'kommt', 'kommen'],
    'spielen' : ['to play', 'spiele', 'spielst', 'spielt', 'spielen', 'spielt', 'spielen'],
    'machen' : ['to do', 'mache', 'machst', 'macht', 'machen', 'macht', 'machen'],
    'sammeln' : ['to collect', 'sammle', 'sammlst', 'sammlt', 'sammlen', 'sammlt', 'sammlen'],
    'zeichnen' : ['to draw', 'zeichne', 'zeichnest', 'zeichnet', 'zeichnen', 'zeichnet', 'zeichnen'],
    'h\u00f6ren' : ['to listen', 'hoere', 'hoerst', 'hoert', 'hoeren', 'hoert', 'hoeren'],
    'basteln' : ['to craft', 'bastele', 'bastelst', 'bastelt', 'basteln', 'bastelt', 'basteln'],
    'besuchen' : ['to visit', 'besuche', 'besuchest', 'besuchet', 'besuchen', 'besuchet', 'besuchen'],
    'schauen' : ['to view', 'schaue', 'schauest', 'schauet', 'schauen', 'schauet', 'schauen'],
    'schwimmen' : ['to swim', 'schwimme', 'scwimmst', 'scwimmt', 'schwimmen', 'scwimmt', 'schwimmen'],
    'tanzen' : ['to dance', 'tanze', 'tanzst', 'tanzt', 'tanzen', 'tanzt', 'tanzen'],
    'wandern' : ['to hike', 'wande', 'wanderst', 'wandert', 'wandern', 'wandert', 'wandern'],
    'lesen' : ['to read', 'lese', 'liest', 'liest', 'lesen', 'lest', 'lesen'],
    'laufen' : ['to run', 'laufe', 'laeufst', 'laeuft', 'laufen', 'lauft', 'laufen'],
    'malen' : ['to paint', 'male', 'malst', 'malt', 'malen', 'malt', 'malen'],
    'kochen' : ['to cook', 'koche', 'kochest', 'kochet', 'kochen', 'kochet', 'kochen'],
    'schreiben' : ['to write', 'schreibe', 'schreibest', 'schreibet', 'schreiben', 'schreibet', 'schreiben'],
    'joggen' : ['to jog', 'jogge', 'joggst', 'joggt', 'joggen', 'joggt', 'joggen'],
    'segeln' : ['to sail', 'segele', 'segelst', 'segelt', 'segeln', 'segelt', 'segeln'],
    'fahren' : ['to drive', 'fahre', 'faehrst', 'faehrt', 'fahren', 'fahrt', 'fahren'],
    'reiten' : ['to ride', 'reite', 'reitest', 'reitet', 'reiten', 'reitet', 'reiten'],
    'fragen' : ['to ask', 'frage', 'fragst', 'fragt', 'fragen', 'fragt', 'fragen'],
    'sehen' : ['to see', 'sehe', 'sehest', 'sehe', 'sehen', 'sehet', 'sehen'],
    'gewinnen' : ['to win', 'gewinne', 'gewinnest', 'gewinnet', 'gewinnen', 'gewinnet', 'gewinnen'],
    'm\u00f6geln' : ['to cheat', 'mag', 'magst', 'mag', 'moegen', 'moegt', 'moegen'],
    'verlieren' : ['to lose', 'verliere', 'verlierest', 'verliere', 'verlieren', 'verlieret', 'verlieren'],
    'haben' : ['to have', 'habe', 'hast', 'hat', 'haben', 'habt', 'haben'],
    'wissen' : ['to know a fact', 'weiss', 'weisst', 'weiss', 'wissen', 'wisst', 'wissen'],
    'essen' : ['to eat', 'esse', 'isst', 'isst', 'essen', 'esst', 'essen']
    }

root = Tk()
root.title('Conjugate or Die')

def main_menu_state():
    title = Label(root, text='Konjugat oder sterben', font=('Sans-Serif', 20)).grid()

    buttons = LabelFrame(root, text='Menu').grid()
    start = Button(buttons, text='Play Game', width=20, command=play_state).grid()
    how2play = Button(buttons, text='How to Play', width=20).grid()
    settings = Button(buttons, text='Game Settings', width=20).grid()
    
    root.mainloop()

def play_state():
    game = Toplevel(root)
    game.title('Conjugate or Die')

    randverb = verb, vals = random.choice(list(verbs.items()))

    v = Label(game, text=randverb[0], width=10).grid(row=0, column=0)
    i = Label(game, text=pronouns[0], width=10).grid(row=1, column=0)
    d = Label(game, text=pronouns[1], width=10).grid(row=2, column=0)
    ese = Label(game, text=pronouns[2], width=10).grid(row=3, column=0)
    w = Label(game, text=pronouns[3], width=10).grid(row=4, column=0)
    ih = Label(game, text=pronouns[4], width=10).grid(row=5, column=0)
    ss = Label(game, text=pronouns[5], width=10).grid(row=6, column=0)

    meaning = Label(game, text=randverb[1][0], width=10).grid(row=0, column=1)
    ich = Entry(game, width=10).grid(row=1, column=1)
    du = Entry(game, width=10).grid(row=2, column=1)
    ersiees = Entry(game, width=10).grid(row=3, column=1)
    wir = Entry(game, width=10).grid(row=4, column=1)
    ihr = Entry(game, width=10).grid(row=5, column=1)
    siesie = Entry(game, width=10).grid(row=6, column=1)

    submit = Button(game, text='Submit').grid(row=3, column=2)

    game.mainloop()

if __name__ == '__main__':
    main_menu_state()

exit()
