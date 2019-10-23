import random
import copy

### VERBS INIT ###
verbendings1 = ["bō","bis","bit","bimus","bitis","bunt"]
verbendings2 = ["bō","bis","bit","bimus","bitis","bunt"]
verbs = []
f=open("verbs2.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        verbs.append(line[:-1].split())
f.close()
### ADVERBS INIT ###
adverbs = []
f=open("adverbs.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        adverbs.append(line[:-1].split())
f.close()
### CONJUNCTIONS INIT ###
conjunctions = []
f=open("adverbs.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        conjunctions.append(line[:-1].split())
f.close()
### PREPOSITIONS INIT ###
prepositions = []
f=open("prepositions.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        prepositions.append(line[:-1].split())
f.close()
### PRONOUNS INIT ###
pronouns = []
f=open("pronouns.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        pronouns.append(line[:-1].split())
f.close()
### NOUNS INIT ###
nounendings1 = ["a","a","ae","ae","am","ā","ae","ae","ārum","īs","ās","īs"]
nounendings2 = ["us","e","ī","ō","um","ō","ī","ī","ōrum","īs","ōs","īs"]
nounendings2er = ["er","er","erī","erō","erum","erō","erī","erī","erōrum","erīs","erōs","erīs"]
nounendings3 = ["um","um","ī","ō","um","ō","a","a","ōrum","īs","as","īs"]
nounendinglocation = lambda case,num:["sg","pl"].index(num)*6+["nom","voc","gen","dat","acc","abl"].index(case)
nouns = []
f=open("nouns.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        nouns.append(line.strip().split(" "))
f.close()
### ADJECTIVES INIT ###
adjectives = []
f=open("adjectives2.txt","rt", encoding="utf-8")
for line in f:
    if line[0]!="#":
        adjectives.append(line.strip().split(" "))
f.close()

### GENERATE A NOUN PHRASE ###
# I should make -are things appear here... later
maxnounrecursiondeapth=3
def nounphrase(case,num=random.choice(["sg","pl"]),nounrecursiondeapth=0):
    if num == "pl":
        if random.randint(0,1)==1 and nounrecursiondeapth<maxnounrecursiondeapth:
            return nounphrase(case,num="sg",nounrecursiondeapth = nounrecursiondeapth+1)+" et "+nounphrase(case,num="sg",nounrecursiondeapth=nounrecursiondeapth+1)

    localnouns = copy.copy(nouns)
    for pronoun in pronouns:
        if case in eval(pronoun[1]) and num in eval(pronoun[2]):
            localnouns.append(pronoun)
    chosennoun = random.choice(localnouns)
    if chosennoun in pronouns:
        return chosennoun[0]
    else:
        phrase = chosennoun[0]+eval(chosennoun[1])[nounendinglocation(case,num)]
        if random.randint(0,1)==1:
            phrase += " "+random.choice(adjectives)[0]+{"f":nounendings1,"m":nounendings2,"n":nounendings3}[chosennoun[2]][nounendinglocation(case,num)]
        if random.randint(0,1)==1 and nounrecursiondeapth<maxnounrecursiondeapth:
            phrase += " "+nounphrase("gen",nounrecursiondeapth = nounrecursiondeapth+1)

    return phrase

###sentance order
#0 address
#1 if
#2 preposition
#3 subject
#4 indirect object
#5 direct object
#6 ablative instrument
#7 adverbs
#8 verb
#9 compound predicate
#10 linkednominative
def sentance(si=False): #si is there so that there aren't nested ifs or multiple addresses
    verb = random.choice(verbs)
    ending = random.randint(0,5)
    phrase = [[verb[0]+eval(verb[1])[ending],8]]
    if ending == 2:
        phrase.append([nounphrase("nom",num="sg"),3])
    if ending == 5:
        phrase.append([nounphrase("nom",num="pl"),3])
    if verb[2] == "link":
        #let this also be an adjective also
        if ending in [0,1,2,6]:
            num = "sg"
        else:
            num = "pl"
        phrase.append([nounphrase("nom",num=num),10])
    if verb[2] == "t":
        phrase.append([nounphrase("acc"),5])
    if verb[0] in ["d","serv","dēbe"] and random.randint(0,1)==1:
        phrase.append([nounphrase("dat"),4])
    if random.randint(0,1)==1:
        prep = random.choice(prepositions)
        phrase.append([prep[0]+" "+nounphrase(prep[1]),2])
    if not si and random.randint(0,1)==1:
        phrase.append(["ō "+nounphrase("voc")+",",0])
    if random.randint(0,1)==1:
        phrase.append([nounphrase("abl"),6])
    if random.randint(0,1)==1:
        phrase.append([random.choice(adverbs)[0],7])
    if random.randint(0,1)==1:
        otherverb = random.choice([tempverb for tempverb in verbs if tempverb[2] == verb[2] and tempverb != verb])
        phrase.append(["et "+otherverb[0]+eval(otherverb[1])[ending],9])
    if random.randint(0,1)==1 and not si:
        phrase.append(["si "+sentance(si=True)+",",1])

    phrase.sort(key=lambda x:x[1])
    return " ".join([subphrase[0] for subphrase in phrase])
j=0
while j<100:
    try:
        print(sentance())
        print("------")
        j+=1
    except:
        pass
XX=True
##
##while XX:
##    try:
##        yy=sentance()
##        if len(yy.split())>=500:
##            print(yy)
##            XX=False
##        
##    except:
##        pass
