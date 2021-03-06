import random
import copy
is_first = True


def noun_ending_location(case, num):
    """
    Tells you what the index of the noun ending is.

    Parameters
    ----------
    case : string
        what case is the noun in, "nom", "voc", "gen", "dat", "acc", "abl".
    num : String
        Is the given noun singular or plural "sg", "pl".

    Returns
    -------
    int
        The index of the noun ending.

    """
    return ["sg", "pl"].index(num)*6+["nom", "voc", "gen", "dat", "acc", "abl"].index(case)


def setup(is_first):
    tense = random.randint(1, 3)
    # 1 is presnt 2 is future 3 is past imperfect
    ### VERBS INIT ###
    unusnauta_us_ending1 = ['a', 'īus', 'ī', 'am', 'ā', 'ae', 'ārum', 'īs', 'ās', 'īs']
    unusnauta_us_ending2 = ['us', 'īus', 'ī', 'um', 'ō', 'ī', 'ōrum', 'īs', 'ōs', 'īs']
    unusnauta_us_ending3 = ['um', 'īus', 'ī', 'um', 'ō', 'a', 'ōrum', 'īs', 'a', 'īs']
    hicend1 = ['aec', 'aec', 'uius', 'uic', 'anc', 'āc', 'ae', "ae", 'ārum', 'īs', 'ās', 'īs']
    hicend2 = ['ic', 'ic', 'uius', 'uic', 'onc', 'ōc', 'ī', 'ī', 'ōrum', 'īs', 'ōs', 'īs']
    hicend3 = ['oc', 'oc', 'uius', 'uic', 'oc', 'ōc', "aec", 'aec', 'ōrum', 'īs', 'aec', 'īs']
    if tense == 1:
        verbendings1 = ["ō", "as", "at", "amus", "atis", "ant", "a", "āte", "āre"]
        verbendings2 = ["eō", "es", "et", "emus", "etis", "ent", "e", "ēte", "ēre"]
        verbendings3 = ["ō", "is", "it", "imus", "itis", "unt", "e", "ite", "ēre"]
        verbendingsspecial = ["sum", "es", "est", "sumus", "estis", "sunt", "es", "este"]
        verbs = []
        f = open("verbs.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                verbs.append(line[:-1].split())
        f.close()

        ### ADJECTIVES INIT ###
        adjectives = []
        f = open("adjectives.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                adjectives.append(line.strip().split(" "))
        f.close()

    elif tense == 2:
        verbendings1 = ["bō", "bis", "bit", "bimus", "bitis", "bunt", 'te', 're']
        verbendings2 = ["bō", "bis", "bit", "bimus", "bitis", "bunt", 'te', 're']
        verbendings3 = ["am", "ēs", "et", "ēmus", "ētis", "ent", "ite", "ēre"]
        verbendingsspecial = ["ō", "is", "it", "imus", "itis", "unt"]
        verbs = []
        f = open("verbs2.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                verbs.append(line[:-1].split())
        f.close()
        adjectives = []
        f = open("adjectives2.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                adjectives.append(line.strip().split(" "))
        f.close()
    else:
        verbendings1 = ["bām", "bās", "bāt", "bāmus", "bātis", "bānt", 'te', 're']
        verbendings2 = ["bām", "bās", "bāt", "bāmus", "bātis", "bānt", 'te', 're']
        verbendings3 = ["ēbām", "ēbās", "ēbāt", "ēbāmus", "ēbātis", "ēbānt", 'te', 're']
        verbendingsspecial = ['am', 'ās', 'at', 'āmus', 'ātis', 'ant']
        verbs = []
        f = open("verbs2.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                verbs.append(line[:-1].split())

        f.close()
        adjectives = []
        f = open("adjectives2.txt", "rt", encoding="utf-8")
        for line in f:
            if line[0] != "#":
                adjectives.append(line.strip().split(" "))
        f.close()

    ### ADVERBS INIT ###
    adverbs = []
    f = open("adverbs.txt", "rt", encoding="utf-8")
    for line in f:
        if line[0] != "#":
            adverbs.append(line[:-1].split())
    f.close()
    ### CONJUNCTIONS INIT ###
    conjunctions = []
    f = open("adverbs.txt", "rt", encoding="utf-8")
    for line in f:
        if line[0] != "#":
            conjunctions.append(line[:-1].split())
    f.close()
    ### PREPOSITIONS INIT ###
    prepositions = []
    f = open("prepositions.txt", "rt", encoding="utf-8")
    for line in f:
        if line[0] != "#":
            prepositions.append(line[:-1].split())
    f.close()
    ### PRONOUNS INIT ###
    pronouns = []
    f = open("pronouns.txt", "rt", encoding="utf-8")
    for line in f:
        if line[0] != "#":
            pronouns.append(line[:-1].split())
    f.close()
    ### NOUNS INIT ###
    nounendings1 = ["a", "a", "ae", "ae", "am", "ā", "ae", "ae", "ārum", "īs", "ās", "īs"]
    nounendings2 = ["us", "e", "ī", "ō", "um", "ō", "ī", "ī", "ōrum", "īs", "ōs", "īs"]
    nounendings2er = ["er", "er", "rī", "rō", "rum", "rō", "rī", "rī", "rōrum", "rīs", "rōs", "rīs"]
    nounendings3 = ["um", "um", "ī", "ō", "um", "ō", "a", "a", "ōrum", "īs", "as", "īs"]

    nouns = []
    f = open("nouns.txt", "rt", encoding="utf-8")
    for line in f:
        if line[0] != "#" and line[0] != '~':
            nouns.append(line.strip().split(" "))
        if line[0] != '#' and "~" in line:
            specialnoun = line.strip().split(" ")[1:]

            nombase = specialnoun[1]

            thirddec = [specialnoun[1]]

            thirddec.append(nombase)
            if specialnoun[2] == 'm' or specialnoun[2] == 'f':
                [thirddec.append(i) for i in [specialnoun[0]+'is', specialnoun[0]+"ī", specialnoun[0]+"em", specialnoun[0]+"e", specialnoun[0]+"ēs", specialnoun[0]+"ēs", specialnoun[0]+"um", specialnoun[0]+"ibus", specialnoun[0]+"ēs", specialnoun[0]+"ibus"]]
            elif specialnoun[2] == 'n':
                [thirddec.append(i) for i in [specialnoun[0]+'is', specialnoun[0]+"ī", nombase, specialnoun[0]+"e", specialnoun[0]+"a", specialnoun[0]+"a", specialnoun[0]+"um", specialnoun[0]+"ibus", specialnoun[0]+"a", specialnoun[0]+"ibus"]]
            else:
                pass
            specialnoun[1] = thirddec[:]
            specialnoun[0] = "​"

            nouns.append(specialnoun)

    f.close()

    if is_first:
        is_first = False
    return unusnauta_us_ending1, unusnauta_us_ending2, unusnauta_us_ending3, hicend1, hicend2, hicend3, verbendings1, verbendings2, verbendings3, verbs, verbendingsspecial, adjectives, adverbs, conjunctions, prepositions, pronouns, nounendings1, nounendings2, nounendings2er, nounendings3, nouns
### GENERATE A NOUN PHRASE ###
# I should make -are things appear here... later


maxnounrecursiondeapth = 3


def nounphrase(case, num=random.choice(["sg", "pl"]), nounrecursiondeapth=0):
    setup_variables = setup(is_first)
    nouns = setup_variables[20]
    pronouns = setup_variables[15]
    adjectives = setup_variables[11]
    nounendings1 = setup_variables[16]
    nounendings2 = setup_variables[17]
    nounendings2er = setup_variables[18]
    nounendings3 = setup_variables[19]
    hicend1 = setup_variables[3]
    hicend2 = setup_variables[4]
    hicend3 = setup_variables[5]
    if num == "pl":
        if random.randint(0, 1) == 1 and nounrecursiondeapth < maxnounrecursiondeapth:
            return nounphrase(case, num="sg", nounrecursiondeapth=nounrecursiondeapth+1)+" et "+nounphrase(case, num="sg", nounrecursiondeapth=nounrecursiondeapth+1)
    localnouns = copy.copy(nouns)
    for pronoun in pronouns:
        scope = locals()
        if case in eval("pronoun[1]", scope) and num in eval("pronoun[2]", scope):
            localnouns.append(pronoun)
    chosennoun = random.choice(localnouns)
    if chosennoun in pronouns:
        return chosennoun[0]

    else:

        if chosennoun[0] == "?":
            scope = locals()
            phrase = str(eval('eval("chosennoun[1]")', scope)[noun_ending_location(case, num)])

        else:
            try:
                if len(chosennoun[0]) == 1:  # if there is an invisible character here
                    scope = locals()
                    phrase = eval("chosennoun[1]", scope)[noun_ending_location(case, num)]
                else:
                    scope = locals()
                    phrase = chosennoun[0]+eval('globals()[eval("chosennoun[1]")]', scope)[noun_ending_location(case, num)]

            except KeyError:
                scope = locals()
                phrase = chosennoun[0]+eval("chosennoun[1]", scope)[noun_ending_location(case, num)]

        if random.randint(0, 1) == 1:
            if random.randint(0, 3) != 0:

                phrase += " "+random.choice(adjectives)[0]+{"f": nounendings1, "m": nounendings2, "n": nounendings3}[chosennoun[2]][noun_ending_location(case, num)]
            else:

                if chosennoun[2] == "f":
                    phrase += " h"+hicend1[noun_ending_location(case, num)]
                elif chosennoun[2] == "m":
                    phrase += " h"+hicend2[noun_ending_location(case, num)]
                elif chosennoun[2] == "n":
                    phrase += " h"+hicend3[noun_ending_location(case, num)]

        if random.randint(0, 1) == 1 and nounrecursiondeapth < maxnounrecursiondeapth:
            phrase += " "+nounphrase("gen", nounrecursiondeapth=nounrecursiondeapth+1)

    return phrase


def sentance(si=False):  # si is there so that there aren't nested ifs or multiple addresses
    setup_variables = setup(is_first)
    nounendings3 = setup_variables[19]
    verbs = setup_variables[9]
    prepositions = setup_variables[14]
    adverbs = setup_variables[12]
    verbendings1 = setup_variables[6]
    verbendings2 = setup_variables[7]
    verbendings3 = setup_variables[8]
    verbendingsspecial = setup_variables[10]

    locals().update({'nounendings3': nounendings3})

    verb = random.choice(verbs)
    ending = random.randint(0, 7)

    phrase = []
    if ending == 2:
        phrase.append([nounphrase("nom", num="sg"), 3])
    if ending == 5:
        phrase.append([nounphrase("nom", num="pl"), 3])

    if verb[2] == "link":
        # let this also be an adjective also
        if ending in [0, 1, 2, 6]:
            num = "sg"
        else:
            num = "pl"
        phrase.append([nounphrase("nom", num=num), 10])
    if verb[2] == "t":
        phrase.append([nounphrase("acc"), 5])
    if verb[3] == 'v':
        scope = locals()
        phrase.append([verb[0]+eval('globals()[eval("verb[1]")]', scope)[ending], 8])
        debug = [tempverb for tempverb in verbs if tempverb[2] == verb[2] and tempverb != verb and tempverb[3] != 'v']
        otherverb = random.choice(debug)
        scope = locals()
        phrase.append([otherverb[0]+eval('globals()[eval("otherverb[1]")]', scope)[ending], 8])
    if verb[0] in ["d", "serv"] and random.randint(0, 1) == 1:
        phrase.append([nounphrase("dat"), 4])
    if random.randint(0, 1) == 1:
        prep = random.choice(prepositions)
        phrase.append([prep[0]+" "+nounphrase(prep[1]), 2])
    if not si and random.randint(0, 1) == 1:
        phrase.append(["? "+nounphrase("voc")+",", 0])
    if random.randint(0, 1) == 1:
        phrase.append([nounphrase("abl"), 6])
    if random.randint(0, 1) == 1:
        phrase.append([random.choice(adverbs)[0], 7])
    if random.randint(0, 1) == 1 and verb[2] != 'link':

        debug = [tempverb for tempverb in verbs if tempverb[2] == verb[2] and tempverb != verb and tempverb[3] != 'v']

        otherverb = random.choice(debug)
        scope = locals()
        phrase.append(["et "+verb[0]+eval('globals()[eval("verb[1]")]', scope)[ending], 9])
        scope = locals()
        phrase.append([otherverb[0]+eval('globals()[eval("otherverb[1]")]', scope)[ending], 9])
    if random.randint(0, 1) == 1 and not si:
        phrase.append(["si "+sentance(si=True)+",", 1])

    phrase.sort(key=lambda x: x[1])

    return " ".join([subphrase[0] for subphrase in phrase])


j = 0


while j < 1000:
    try:
        z = sentance()
        if 'si et' not in z and z != '':
            print(z)
            print("------")
            j += 1

    except IndexError:
        pass
