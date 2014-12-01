import random
def generate_suggestion():
    doctor=['doctor','doc','physician','medic','specialist','MD','DO']
    doctor=random.choice(doctor)
    research=['research','look into','investigate','inquire about','think about']
    research=random.choice(research)
    support=['help','assistance','support','advice']
    support=random.choice(support)
    visit=['visit','go see','consult','ask']
    visit=random.choice(visit)
    better=['Better','Should','Could', 'Go']
    better=random.choice(better)
    ls=[visit+' a '+doctor+'.','Time to '+visit+' the '+doctor+'.',better+' get some '+support+'.','Might want to '+research+' that.',]
    a=random.choice(ls)
    return a,len(a)




much = ['much', 'a lot', 'alot', 'often', 'recently', 'lately', 'frequently','constantly' ]
its = ["It's", "That's", "I think it's", "I think that's" ]
obviously = ['obviously', 'probably', 'undoubtedly', 'possibly', 'plausibly', 'perhaps', 'likely', 'conceivably', 'maybe', 'perchance', 'imaginably' ]

abdomin=['Gassy', 'Tummy hurts', 'Stomach hurts', 'Feeling fat', 'Belly hurts']
abdominprobs=['ebola','tetanus','prego','pancreatitis','Q fever',  'gastroenteritis','fasciolosis','lassa fever', 'giardiasis','pregnant', 'obesity', 'stomach cancer', 'appendicitis', 'constipation', 'stomach flu']
abdominbp=['liver', 'esophagus', 'stomach', 'belly', 'diaphragm', 'cardial notch', 'pylorus','fundus', 'duodenum']
coughing = ['Coughing','Hacking', 'Wheezing', 'Sick', 'Gasping', 'Hissing', 'Rasping','Panting', 'Snoring', 'Hemming', 'Cold', 'Aheming', 'Crouping' ]
coughprobs = ['apnea','lung cancer','valley fever','nocardiosis','mono', 'histoplasmosis','legionnaires','influenza','flu','hookworm', 'pertussis', 'pneumonia', 'myositis', 'bronchitis', 'asthma', 'SARS' ]
coughbp=['lung', 'throat', 'windpipe','trachea', 'cardiac notch' , 'bronchi']
diarrhea =['Shitting', 'Liquid shit', 'Liquid wiping', 'Diarrhea', 'Bowls of brown'  ]
diarrheaprobs=['ebola', 'rotavirus','polio','irritable bowel syndrome', 'lassa fever', 'isosporiasis','hookworm','giardiasis', 'stomach flu','appendicitis', 'cholera' ]
diarrheabp=['ass', 'asshole',  'anus', 'rectum','butt','butthole','backdoor']

earache=['Problems hearing', 'Eardrum hurting', 'Ear pains', 'Ear hurts']
earacheprobs=['mumps','mucormycosis', 'zygomycosis','phycomycosis', 'ear cancer']
earachebp=['ear', 'earlobe', 'eardrum', 'cochlea', 'hearing', 'sense of sound']
eye=['Eye problems', 'Eyesight issues', 'Vision troubles', 'Eye troubles' ]
eyeprobs=['keratitis', 'cerebral malaria', 'leprosy', 'trachoma','zygomycosis']
eyebp=['eye', 'pupil', 'eyeball','eyelid', 'eyesight', 'vision']
fever=['Feverish', 'Sweating', 'Feeling hot', 'Hot flashes','Burning up']
feverprobs=['ebola','valley fever','tetanus','shingles','sepsis ','rift valley fever', 'rubella','rotavirus','polio', 'encephalitis','Q fever','legionnaires','mumps','malaria', 'septicemia','gastroenteritis','nocardiosis' ]
feverbp=['brain', 'head', 'forehead','temple', 'brow','frons','skull','cranium','noggin','dome']
headache=['Headaches', 'Achy head', 'Pounding forehead','Pain in the head']
headacheprobs=['ebola','valley fever','shingles','rift valley fever','polio','encephalitis','Q fever','dengue fever','mumps','malaria','septicemia','gastroenteritis','nocardiosis']
headachebp=['brain', 'head', 'forehead','temple','brow','frons','skull','cranium','noggin','dome']
joint=['Joint pains', 'Muscle pains', 'Stressing bones']
jointprobs=['ebola', 'valley fever','tetanus','rift valley fever','rubella','polio','dengue fever', 'malaria','septicemia','gastroenteritis','Q fever']
jointbp=['bones', 'muscle', 'tendon','tissue','cartilage','bone marrow']
nasal=['Breathing troubles', 'Trouble breathing', 'Problems breathing', 'Breathing problems']
nasalprobs=['sepsis','trachoma','zygomycosis','mucormycosis','phycomycosis' ]
nasalbp=['nose', 'sense of smell', 'smeller' ,'snout']
nausea=['Feeling nauseous', 'Upset stomach', 'Vomiting', 'Tossing','Sick','Throwing up','Queasy' ]
nauseaprobs=['hookworm','influenza', 'lassa fever','pancreatitis','Q fever' ]
nauseabp=['liver', 'esophagus', 'stomach', 'belly', 'diaphragm', 'cardial notch', 'pylorus','fundus', 'duodenum']
skin=['Rashy skin', 'Red skin', 'Irritated skin','Itchy skin'  ]
skinprobs=['poison oak', 'poison ivy', 'syphilis','smallpox','zygomycosis','mucormycosis','phycomycosis', 'shingles', 'scabies', 'rubella','chickenpox','mumps', 'leprosy','dengue fever', 'measles', 'morbilliform' , 'kawasaki disease']
skinbp=['skin', 'hair', 'sense of touch', 'touch sense' ]
sore=['Sore throat', 'Trouble swallowing', 'Throat hurting' , 'Hurts to swallow']
soreprobs=['ebola','flu', 'influenza', 'lung cancer', 'throat cancer', 'pertussis', 'pneumonia']
sorebp=['lung', 'throat', 'windpipe','trachea', 'cardiac notch' , 'bronchi','bronchitis','mono']
urin=['Trouble peeing', 'Problem pissing', 'Peeing', 'Pissing' ]
urinprobs=['rotavirus','malaria','septicemia','gastroenteritis','tetanus','bladder cancer', 'liver cancer']
urinbp=['penis', 'vagina', 'urinary tract', 'pisser','liver','bladder','vesicle']


biglist = [[abdomin,abdominprobs,abdominbp], [coughing,coughprobs,coughbp], [diarrhea,diarrheaprobs,diarrheabp],[earache,earacheprobs, earachebp],[eye,eyeprobs,eyebp], [fever,feverprobs,feverbp], [headache,headacheprobs,headachebp],[joint,jointprobs,jointbp],[nasal,nasalprobs,nasalbp],[nausea,nauseaprobs,nauseabp],[skin,skinprobs,skinbp],[sore,soreprobs,sorebp],[urin, urinprobs,urinbp]]



def generate_ending(i):    #
    may_list = ['That may','That might','That will','That can', 'That could','Def will','Prob will']
    may_list=random.choice(may_list)
    
    curse_word = ['wreck','lose','damage','destroy','ruin','annihilate','finish off','eradicate']
    curse_word=random.choice(curse_word)
    
    time=['decades','years','life','ever','a long time','a minute']
    time=random.choice(time)
    
    ls1=[may_list+' '+curse_word+' '+'the'+' '+random.choice(biglist[i][2])+' '+'for'+' '+time]
    a1=random.choice(ls1)
    return a1,len(a1) 

    
def generate_restate(i):
    ls =   random.choice(biglist[i][0]) + ' ' + random.choice(much) + '? ' + random.choice(its) + ' ' + random.choice(obviously) + ' ' + random.choice(biglist[i][1])+ '!' 
    return ls, len(ls)
    
def tweets_respond(j): # j is the index which will indicate which symptoms we are looking at....
    temp = generate_restate(j)[0], generate_suggestion()[0],generate_ending(j)[0], generate_restate(j)[1] + generate_suggestion()[1] + generate_ending(j)[1]
    respond = temp[0]+' '+temp[1]+' '+temp[2]
    #print respond, temp[3]
    if temp[3] < 122:
        return respond
    else:
        #print "blah blah"
        return tweets_respond(j)