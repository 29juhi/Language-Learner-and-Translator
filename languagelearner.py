import pickle
import os
#logging in
detail=[]
def login():    #function to login to a profile
    
    name=input('ENTER USERNAME: ')     #input username n password
    passwd=input('ENTER PASSWORD: ')
    print()  #leave a line
    
    f=open('profiles.dat','rb')   #a file where all profiles and resp data is saved
    #data is stored in form [username,password,points,languages chosen]
    l=[]    #to load profiles into the list l
    
    try:
        while True:
            x=pickle.load(f)  #loadgetting data from file
            l.append(x)
    
    except:
       
        pass
    
    login=0
    
    for i in l:
        
        if i[0]==name:
        
            if i[1]==passwd:   #checking password
                
                print('LOGGED IN AS',name)
                login+=1
                
                global detail    #so that we can used vatiable detail wherever in the code
                detail=i   #these are details of user
                req_ind=l.index(i)
                
            else:
                
                pass
        
        else:
            pass
    
    if login!=1:      #when there is no match
        print('incorrect username or password')
    
    elif login==1:  #username and password match
        print()
    
    f.close()
    #----- VIEW PROFILE
    
    def details():  #to show details of user
        lang_tested=''
        lang_tested_lst=detail[-1::]  #languages tested
        
        if len(lang_tested_lst)==0:  #no language tested yet
            lang_tested='none'
        
        else:
            for i in lang_tested_lst:
                if lang_tested_lst.index(i)==len(lang_tested_lst)-1: #if it is last element of list
                    lang_tested+=str(i)
                else:
                    lang_tested+=i #to display words seperated by commas
                    lang_tested+=','
        print('username: ',detail[0])
        print('points: ',detail[2])
        print('languages tested: ',lang_tested)
    #---- TAKE TEST
    def test():      #function for test
        f=open('words.txt','w')  #a file where all words are saved 
        l_of_words=['Earth\n', 'planet\n', 'hosts\n', 'inhabited\n', 'humans\n', 'other\n', 'living\n', 'beings\n', 'rocks\n', 'metals\n', 'gases\n', 'solar\n', 'system\n', 'sustain\n', 'Mother\n', 'billion\n', 'people\n', 'natural\n', 'resources\n', 'healthier\n', 'lives\n', 'provides\n', 'water\n', 'shelter\n', 'Writing\n', 'essay\n', 'helps\n', 'children\n', 'importance\n', 'protecting\n', 'vital\n', 'resource\n', 'depend\n', 'plants\n', 'trees\n', 'destroy\n', 'start\n', 'things\n', 'environment\n', 'health\n', 'survive\n', 'protect\n', 'planting\n', 'adopting\n', 'sustainable\n', 'lifestyle\n', 'amazing\n', 'various\n', 'landscapes\n', 'ecosystems\n', 'essential\n', 'preserve\n', 'ensure\n', 'future\n', 'generations\n', 'enjoy\n', 'unique\n', 'beauty\n', 'crucial\n', 'conservation\n', 'programmes\n', 'across\n', 'world\n', 'Environmental\n', 'organisations\n', 'around\n', 'decades\n', 'trying\n', 'biodiversity\n', 'promote\n', 'awareness\n', 'defined\n', 'government\n', 'Democracy\n', 'which\n', 'governed\n', 'elected\n', 'representatives\n', 'guarantees\n', 'basic\n', 'rights\n', 'freedom\n', 'individuals\n', 'voters\n', 'known\n','fundamental\n', 'population\n', 'union\n', 'states\n', 'sovereign\n', 'socialist\n', 'secular\n', 'democratic\n', 'republic\n', 'parliamentary\n', 'terms\n', 'theÂ\xa0Constitution\n', 'adopted\n', 'force\n', 'possible\n', 'country\n', 'participate\n', 'exercise\n', 'franchise\n', 'elect\n', 'regular\n', 'intervals\n', 'parliament\n', 'legislate\n', 'responsible\n', 'became\n', 'infused\n', 'spirit\n', 'justice\n', 'liberty\n', 'equality\n', 'fraternity\n', 'State\n', 'policy\n', 'reflect\n', 'Indian\n', 'ideology\n', 'caste\n', 'creed\n', 'religion\n', 'property\n', 'right\n', 'After\n', 'election\n', 'majority\n', 'party\n', 'coalition\n', 'forms\n', 'leader\n', 'become\n', 'wellness\n', 'healthy\n', 'considered\n', 'methods\n', 'preventive\n', 'healthcare\n', 'globally\n', 'demand\n', 'effective\n', 'products\n', 'enhance\n', 'quality\n', 'increased\n', 'manifold\n', 'years\n', 'ethical\n', 'direct\n', 'selling\n', 'company\n', 'brings\n', 'range\n', 'solutions\n', 'peopleâ€™s\n', 'empowers\n', 'political\n', 'control\n', 'limits\n', 'power\n', 'separation\n', 'between\n', 'governmental\n', 'entities\n', 'ensures\n', 'protection\n', 'civil\n', 'liberties\n', 'practice\n', 'takes\n', 'different\n', 'Along\n', 'common\n', 'types\n', 'representative\n', 'participatory\n', 'liberal\n', 'pluralist\n', 'constitutional\n', 'democracies\n', 'found\n', 'today\n', 'organisation\n', 'spreading\n', 'holistic\n', 'throughout\n', 'personal\n', 'cosmetics\n', 'categories\n', 'manufactured\n', 'manufacturing\n', 'facilities\n', 'these\n', 'superior\n', 'exalt\n', 'consumer\n', 'experience\n', 'responsive\n', 'extremely\n', 'focus\n', 'providing\n', 'excellent\n', 'support\n', 'service\n', 'every\n', 'celebrate\n', 'everyone\n', 'society\n', 'variants']
        f.writelines(l_of_words)  
        f.close()
        points=0  #given on each correct answer
    
        import googletrans, random  #modules used
        l=['1. ARABIC','2. SPANISH','3. FRENCH','4. GERMAN','5. GREEK','6. HINDI','7. ITALIAN','8. JAPANESE','9. KOREAN','10. LATIN']
        #these are languages available
        
        for i in l:
            print(i)
        
        ch=int(input('PLEASE ENTER YOUR SL.NO OF CHOICE OF YOUR DESIRED LANGUAGE FROM THE LIST GIVEN ABOVE: '))
        #language to take test
        print('INSTRUCTIONS:')
        print('There will be 10 questions in the test.')
        print('The questions will be displayed in english and you have to enter the translation of each question.')
        print()
        
        for i in l:
            if int(i[0])==ch:
                lang=i[3::] #it is in format '1. language' slicing to take only language
        
        print('Your chosen language is',lang)  
        print()      
        d_languages=googletrans.LANGUAGES #dict of languages googletrans has
        '''
        {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 
         'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
         'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
         'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 
         'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish
         ', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek',
         'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew',
         'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 
         'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 
         'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin',
         'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 
         'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
         'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian',
         'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 
         'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 
         'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 
         'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 
         'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 
         'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        '''
        for i in d_languages:
            if d_languages.get(i)==lang.lower():
                language_chosen=i
                
        f=open('words.txt','r')
        l_used=[]  # further few lines of code are to not repeat any word in test
        l_words=f.readlines()
        i=1
        quest=len(l_used)+10
        
        while len(l_used)<quest:
            ind=random.randint(0,len(l_words)-1)  #to get any random word
            word=l_words[ind]
            
            if word not in l_used:  #only if word has not been given previously
                l_used.append(word)
                print('Q'+str(i)+':',word)
                ans=input('Enter translation:')  #inputting answer
                translator=googletrans.Translator()
                translated=translator.translate(word,src='en',dest=language_chosen)
                x=(str(translated)[10::])  #slicing to get required word
                x=(x.split(', '))
                translated_word=x[2][5::]
                
                if translated_word.lower()==ans.lower():  #checking answer
                    print('correct')
                    print()
                    
                    points+=1
    
                else:
                    print('incorrect')
                    print('correct answer is',translated_word)  #displaying correct ans
                    print()
                i+=1
            
            else:
                pass
        
        acc=points*10  #results
        print('points:',points)
        print('your accuracy=',acc,'%')
        lang_new=detail[-1]
        points_new=detail[-2]+points#updating profile
        lang_new.append(lang)
        det_new=[detail[0],detail[1],points_new,lang_new]
        l.pop(req_ind)
        l.insert(req_ind,det_new)
        f=open('profiles.dat','wb')
        
        for i in l:
            pickle.dump(i,f)
        f.close()
    #------translate
    
    def translate():  #to translate a text from english to other language
        import googletrans
        word=input('Enter sentence/word to translate: ')
        d_languages=googletrans.LANGUAGES
        ind=1
        
        l=[]
        
        for i in d_languages:
            print(str(ind)+'.'+d_languages.get(i))
            ind+=1
            l.append(d_languages.get(i))
        ch=int(input('enter sl.no of your desired language: '))
        d_list=list(d_languages) #to get only the keys
        language_chosen=(d_list[ch-1])
        translator=googletrans.Translator()
        translated=translator.translate(word,src='en',dest=language_chosen)

        #Translated(src=en, dest=it, text=vive, pronunciation=lives, extra_data="{'translat...")
        #this is how it appears so to slice required string

        x=(str(translated)[10::]) #slicing resquired result
        x=(x.split(', '))
        translated_word=x[2][5::]
        print('Translating',word,'from English to',l[ch-1])
        print(translated_word)
        
        
    #----MENU2
    if login==1:  #only if login successful
        print('--MENU--')
        print('1. VIEW PROFILE')
        print('2. TAKE TEST')
        print('3. TRANSLATE')
        
        ch=int(input('enter choice: '))
        
        if ch==1:
            details()
        
        elif ch==2:
            test()
        
        elif ch==3:
            translate()
            
        else:
            print('enter valid choice')
        
        
#----------------
def create_profile():
    print('TO CREATE A PROFILE PLEASE ENTER THE FOLLOWING DETAILS')

    # Check if the file exists
    if os.path.exists('profiles.dat'):
        f = open('profiles.dat', 'rb')
        l = []
        try:
            while True:
                x = pickle.load(f)
                l.append(x)
        except EOFError:  # Handle the end of file error
            pass
        f.close()
    else:
        l = []  # Initialize an empty list if the file doesn't exist

    name = input('ENTER USERNAME: ')
    n = 0
    
    for i in l: 
        if i[0] == name:  # If username already exists
            n += 1
        else:
            pass

    if n == 0:
        passwd = input('CREATE PASSWORD: ')
        f = open('profiles.dat', 'ab')  # Open file in append mode to add new profile
        j = [name, passwd, 0, []]  # New profile details
        pickle.dump(j, f)
        f.close()
    else:
        print('Username already taken')

#-------------------------------------MENU MAIN

print('---------MENU----------')

print('1. LOG IN TO YOUR PROFILE')

print('2. CREATE A PROFILE')

ch=int(input('enter your choice: '))

if ch==1:
    login()

elif ch==2:
    create_profile()
else:
    print('enter valid choice')

