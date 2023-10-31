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

# Main menu function
def main_menu_state():
    title = Label(root, text=' \u263a Konjugat oder sterben \u2694 ', font=('Sans-Serif', 20)).grid()
    
    spacer1 = Label(root, text='').grid()

    buttons = LabelFrame(root, text='Menu').grid()
    start = Button(buttons, text='Play Game', width=20, command=play_state).grid()
    how2play = Button(buttons, text='How to Play', width=20, command=how_play_state).grid()
    settings = Button(buttons, text='Game Settings', width=20, command=settings_state).grid()

    spacer2 = Label(root, text='').grid()
    
    root.mainloop()

# How to play screen
def how_play_state():
    how_play = Toplevel(root)
    how_play.title('How to Play')

    how = Label(how_play, text='How to Play\n', font=('Sans-Serif', 20)).grid()

    rules = Label(how_play, text='You must correctly conjugate the verbs given to you.\nFor conjugations containing the letter \u00e4, type it as "ae".\nFor the letter \u00f6, type as "oe".\nFor the letter \u00fc, type as "ue".\nAnd for the letter \u00df, type it as "ss".\n\nYou can change most aspects of the game in the settings.\n').grid()

    move_on = Label(how_play, text='Close this window to return to the main menu.').grid()

# Settings screen
def settings_state():
    settings = Toplevel(root)
    settings.title('Game Settings')

    title = Label(settings, text='Game Settings', font=('Sans-Serif', 20)).grid()

# Line 67 to line 131: All game functions
def lose_state():
    lose = Toplevel(root)
    lose.title('Die')

    death = Label(lose, text='You have died. \u2694', font=('Sans-Serif', 20)).grid()
    move_on = Label(lose, text='Close this window to return to the main menu.').grid()

def win_state():
    win = Toplevel(root)
    win.title('Conjugate')

    yay = Label(win, text='You have conjugated! \u263a', font=('Sans-Serif', 20)).grid()
    move_on = Label(win, text='Close this window to return to the main menu.').grid()

def check_answers(answers, conjugations):
    for i in range(6):
        if not answers[i] == conjugations[1][i+1]:
            lose_state()
            return
    win_state()

def get_answers():
    i = ich.get()
    d = du.get()
    ese = ersiees.get()
    w = wir.get()
    ih = ihr.get()
    ss = siesie.get()

    return [i, d, ese, w, ih, ss]

def play_state():
    game = Toplevel(root)

    randverb = verb, vals = random.choice(list(verbs.items()))
    game.title(randverb[0])

    v = Label(game, text=randverb[0], width=10).grid(row=0, column=0)
    i = Label(game, text=pronouns[0], width=10).grid(row=1, column=0)
    d = Label(game, text=pronouns[1], width=10).grid(row=2, column=0)
    ese = Label(game, text=pronouns[2], width=10).grid(row=3, column=0)
    w = Label(game, text=pronouns[3], width=10).grid(row=4, column=0)
    ih = Label(game, text=pronouns[4], width=10).grid(row=5, column=0)
    ss = Label(game, text=pronouns[5], width=10).grid(row=6, column=0)

    meaning = Label(game, text=randverb[1][0], width=10).grid(row=0, column=1)

    global ich, du, ersiees, wir, ihr, siesie

    ich = Entry(game, width=10)
    ich.grid(row=1, column=1)
    du = Entry(game, width=10)
    du.grid(row=2, column=1)
    ersiees = Entry(game, width=10)
    ersiees.grid(row=3, column=1)
    wir = Entry(game, width=10)
    wir.grid(row=4, column=1)
    ihr = Entry(game, width=10)
    ihr.grid(row=5, column=1)
    siesie = Entry(game, width=10)
    siesie.grid(row=6, column=1)

    submit = Button(game, text='Submit', command=lambda:[check_answers(get_answers(), randverb), game.destroy()]).grid(row=3, column=2)

if __name__ == '__main__':
    main_menu_state()

exit()
