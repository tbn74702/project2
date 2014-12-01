import pymongo
import re
import time
import bson
import os

def lastid_read(txtfile):
    file=open(txtfile,'r')
    ls=file.read()
    file.close()
    return ls

def lastid_write(txtfile,string):
    os.remove(txtfile)
    file=open(txtfile,'w')
    #ls=file.read()
    #ls.replace(r'.*','')
    file.write(string)
    #ls=file.read()
    file.close()
    
def mongo_search(pattern,lastid):
    id_list=[]
    #tweet_list=[]
    blastid=bson.ObjectId(lastid)
    conn=pymongo.MongoClient()
    cn=conn['twitter']
    tweet=cn['lines']
    query={'text':{'$regex':pattern},'_id' : {'$gt':blastid}}
    a=list(tweet.find(query).limit(1))
    for i in range(len(a)):
        id_list.append(str(a[i]['id_str']))
        #tweet_list.append(str(a[i]['text']))
    if len(id_list) == 0:   #Deals with possible indexing errors when no tweets are found
        bson_id=blastid
    else:
        bson_id=a[0]['_id']
    return id_list,bson_id

def getall_tweet(allregex,lastid):  #runs every regex through mongodb (allregex=mark)
    allid_list=[]
    bson_ids=[]
    #alltweet_list=[]
    for i in range(len(allregex)):
        ms=[]
        ms=mongo_search(allregex[i],lastid)
        allid_list.append(ms[0])
        bson_ids.append(ms[1])
        print 'Found '+str(len(ms[0])) + ' tweets for pattern '+str(i)
    dt_ids=[]
    for i in range(len(bson_ids)):
        dt_ids.append(bson_ids[i].generation_time)
    max_time=max(dt_ids)
    for j in range(len(dt_ids)):
        if dt_ids[j]==max_time:
            max_id=bson_ids[j]
    return allid_list,str(max_id)

def list_create(txtfile):
    file=open(txtfile,'r')
    ls=file.readlines()
    for i in range(len(ls)):
        ls[i]=ls[i].replace('\n','')
    file.close()
    return ls

def regex_generate(symptoms_txt,synonyms_txt): #Compressing the regex work below into a function
    symptoms=list_create(symptoms_txt)
    synonyms=[]
    for i in range(len(symptoms)):
        synonyms.append(list_create(synonyms_txt)[i].split())
    tl=[]
    for j in range(len(symptoms)):
        tl.append('(?=.*(\s+'+symptoms[j] + '\s*|\s+')
        for i in range(len(synonyms[j])):
            if i<(len(synonyms[j])-1):
                tl[j]=tl[j]+synonyms[j][i]+'\s*|\s+'
            else:
                tl[j]=tl[j]+synonyms[j][i]+'))'
    #helplist ='(\s+help\s*|\s+assist\s*|\s+aid\s*|\s+ease\s*|\s+alleviat\s*|\s+sooth\s*|\s+relie\s*|\s+lessen\s*)'            
    hurtlist ='(\s+hurt\s*|\s+painful\s*|\s+pains\s*|\s+pain\s+|\s+injur\s*|\s+cut\s+|\s+wound\s*|\s+damage\s*|\s+suffering\s*|\s+trauma\s*|\s+agony\s*|\s+torment\s*|\s+discomfort\s*|\s+distress\s*)'
    mark=[]
    for i in range(len(tl)):
        mark.append(re.compile(tl[i]+'(?=.*'+hurtlist+ ')', flags=re.IGNORECASE))
    return mark