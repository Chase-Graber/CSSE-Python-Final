import random, os, time

# Dictionary of all verbs and their conjugations
"""
Verbs are presented in the following form:
list_item | [0]
---------------------
      ich | [1]
       du | [2]
er/sie/es | [3]
      wir | [4]
      ihr | [5]
  Sie/sie | [6]

"""
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

def main_menu_state():
    os.system('cls')
    print('█▄▀ █▀█ █▄░█ ░░█ █░█ █▀▀ ▄▀█ ▀█▀\n█░█ █▄█ █░▀█ █▄█ █▄█ █▄█ █▀█ ░█░\n\n█▀█ █▀▄ █▀▀ █▀█\n█▄█ █▄▀ ██▄ █▀▄\n\n█▀ ▀█▀ █▀▀ █▀█ █▄▄ █▀▀ █▄░█\n▄█ ░█░ ██▄ █▀▄ █▄█ ██▄ █░▀█')
    print('\n')
    time.sleep(0.05)
    print('1) How to play')
    time.sleep(0.05)
    print('2) List of all verbs')
    time.sleep(0.05)
    print('3) Play game')
    time.sleep(0.05)
    print('4) Exit game\n')
    time.sleep(0.05)
    ans = int(input('>> '))
    while ans not in [1, 2, 3, 4]:
        os.system('cls')
        print('█▄▀ █▀█ █▄░█ ░░█ █░█ █▀▀ ▄▀█ ▀█▀\n█░█ █▄█ █░▀█ █▄█ █▄█ █▄█ █▀█ ░█░\n\n█▀█ █▀▄ █▀▀ █▀█\n█▄█ █▄▀ ██▄ █▀▄\n\n█▀ ▀█▀ █▀▀ █▀█ █▄▄ █▀▀ █▄░█\n▄█ ░█░ ██▄ █▀▄ █▄█ ██▄ █░▀█')
        print('\n')
        time.sleep(0.05)
        print('1) How to play')
        time.sleep(0.05)
        print('2) List of all verbs')
        time.sleep(0.05)
        print('3) Play game')
        time.sleep(0.05)
        print('4) Exit game\n')
        time.sleep(0.05)
        ans = int(input('>> '))
    
    if ans == 1:
        pass
    elif ans == 2:
        pass
    elif ans == 3:
        play_state()
    else:
        os.system('cls')
        print('coward')

def play_state():
    os.system('cls')
    randverb = verb, vals = random.choice(list(verbs.items()))
    print('Your verb is...')
    time.sleep(1.5)
    print(randverb[0] + '   ', end='|')
    print('   ' + randverb[1][0])



if __name__ == '__main__':
    main_menu_state()

exit()
