import random

def tones():
    return ['C','^C','D','^D','E','F','^F','G','^G','A','^A','B',
            'c','^c','d','^d','e','f','^f','g','^g','a','^a','b']

def maj(note):
    t = tones()
    return [
        t[note],
        t[note+4],
        t[note+7],
        t[note+11],
    ]

def dorian(note):
    t = tones()
    return [
        t[note],
        t[note+3],
        t[note+7],
        t[note+10]
    ]

def dom(note):
    t = tones()
    return [
        t[note],
        t[note+4],
        t[note+7],
        t[note+10]
    ]

# 0  = C
# 11 = B

progression = [
    dom(0), # C7
    dom(5), # F7
    dom(0), # C7
    dom(0), # C7

    dom(5), # F7
    dom(5), # F7
    dom(0), # C7
    dom(0), # C7

    dorian(2), # Dm
    dom(7), # G7
    dom(0), # C7
    dom(7), # G7
]

#print progression

print 'X:1'
print 'T:180'
print 'M:4/4'
print 'L:1/4'
print 'N: Blues'
print 'K: C bass octave=-2'
print '%%MIDI program 34'

old_note = None

for notes in progression:
    did_remove = False

    if old_note is None:
        note = random.choice(notes)
    else:
        if old_note in notes:
            notes.remove(old_note)
            did_remove = True

        idx_current = tones().index(old_note)
        distances = [abs(tones().index(x) - idx_current) for x in notes]
        min_dist = min(distances)
        dist_list = []
        for x, dist in enumerate(distances):
            if dist == min_dist:
                dist_list.append(x)
        note = notes[random.choice(dist_list)]

    print note,

    if did_remove:
        notes.append(old_note)
    old_note = note
    notes.remove(note)

    idx_current = tones().index(old_note)
    distances = [abs(tones().index(x) - idx_current) for x in notes]
    min_dist = min(distances)
    dist_list = []
    for x, dist in enumerate(distances):
        if dist == min_dist:
            dist_list.append(x)
    note = notes[random.choice(dist_list)]

    print note,
    notes.append(old_note)
    old_note = note
    notes.remove(note)

    idx_current = tones().index(old_note)
    distances = [abs(tones().index(x) - idx_current) for x in notes]
    min_dist = min(distances)
    dist_list = []
    for x, dist in enumerate(distances):
        if dist == min_dist:
            dist_list.append(x)
    note = notes[random.choice(dist_list)]

    print note,
    notes.append(old_note)
    old_note = note
    notes.remove(note)

    idx_current = tones().index(old_note)
    distances = [abs(tones().index(x) - idx_current) for x in notes]
    min_dist = min(distances)
    dist_list = []
    for x, dist in enumerate(distances):
        if dist == min_dist:
            dist_list.append(x)
    note = notes[random.choice(dist_list)]

    print note,
    notes.append(old_note)
    old_note = note
    notes.remove(note)

    print '|'
