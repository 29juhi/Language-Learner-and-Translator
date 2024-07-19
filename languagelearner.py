import pickle
import googletrans
import random
import os

detail = []

def login():
    name = input('ENTER USERNAME: ')
    passwd = input('ENTER PASSWORD: ')
    print()

    if not os.path.exists('profiles.dat'):
        print("No profiles found. Please register first.")
        return

    try:
        with open('profiles.dat', 'rb') as f:
            profiles = []
            while True:
                try:
                    profiles.append(pickle.load(f))
                except EOFError:
                    break
    except Exception as e:
        print(f"Error reading profiles: {e}")
        return

    login_success = False
    for i, profile in enumerate(profiles):
        if profile[0] == name and profile[1] == passwd:
            print(f'LOGGED IN AS {name}')
            global detail
            detail = profile
            req_ind = i
            login_success = True
            break

    if not login_success:
        print('Incorrect username or password')
        return

    print()

    def details():
        lang_tested = ', '.join(detail[-1]) if detail[-1] else 'none'
        print('username: ', detail[0])
        print('points: ', detail[2])
        print('languages tested: ', lang_tested)

    def test():
        with open('words.txt', 'w') as f:
            l_of_words = [
                'Earth\n', 'planet\n', 'hosts\n', 'inhabited\n', 'humans\n', 'other\n', 'living\n', 'beings\n',
                'rocks\n', 'metals\n', 'gases\n', 'solar\n', 'system\n', 'sustain\n', 'Mother\n', 'billion\n',
                'people\n', 'natural\n', 'resources\n', 'healthier\n', 'lives\n', 'provides\n', 'water\n',
                'shelter\n', 'Writing\n', 'essay\n', 'helps\n', 'children\n', 'importance\n', 'protecting\n',
                'vital\n', 'resource\n', 'depend\n', 'plants\n', 'trees\n', 'destroy\n', 'start\n', 'things\n',
                'environment\n', 'health\n', 'survive\n', 'protect\n'
            ]
            f.writelines(l_of_words)
        
        points = 0

        available_languages = [
            '1. ARABIC', '2. SPANISH', '3. FRENCH', '4. GERMAN', '5. GREEK', '6. HINDI', '7. ITALIAN', '8. JAPANESE',
            '9. KOREAN', '10. LATIN'
        ]

        for language in available_languages:
            print(language)

        ch = int(input('PLEASE ENTER YOUR SL.NO OF CHOICE OF YOUR DESIRED LANGUAGE FROM THE LIST GIVEN ABOVE: '))
        print('INSTRUCTIONS:')
        print('There will be 10 questions in the test.')
        print('The questions will be displayed in English and you have to enter the translation of each question.')
        print()

        for language in available_languages:
            if int(language.split('.')[0]) == ch:
                lang = language.split('. ')[1]
                print(f'Your chosen language is {lang}')
                print()

        translator = googletrans.Translator()
        languages_dict = googletrans.LANGUAGES

        language_code = None
        for code, language in languages_dict.items():
            if language.lower() == lang.lower():
                language_code = code
                break

        if not language_code:
            print("Selected language is not supported.")
            return

        with open('words.txt', 'r') as f:
            l_used = []
            l_words = f.readlines()
            i = 1
            while len(l_used) < 10:
                ind = random.randint(0, len(l_words) - 1)
                word = l_words[ind].strip()
                if word not in l_used:
                    l_used.append(word)
                    print(f'Q{i}: {word}')
                    ans = input('Enter translation: ').strip()
                    translated = translator.translate(word, src='en', dest=language_code)
                    translated_word = translated.text.strip()
                    if translated_word.lower() == ans.lower():
                        print('Correct')
                        points += 1
                    else:
                        print(f'Incorrect. Correct answer is {translated_word}')
                    print()
                    i += 1
        
        acc = points * 10
        print(f'points: {points}')
        print(f'your accuracy = {acc}%')

        detail[-1].append(lang)
        detail[2] += points
        profiles[req_ind] = detail

        with open('profiles.dat', 'wb') as f:
            for profile in profiles:
                pickle.dump(profile, f)

    def translate():
        word = input('Enter sentence/word to translate: ').strip()
        d_languages = googletrans.LANGUAGES
        ind = 1
        l = []
        for i in d_languages:
            print(f'{ind}. {d_languages.get(i)}')
            ind += 1
            l.append(d_languages.get(i))
        ch = int(input('Enter sl.no of your desired language: '))
        d_list = list(d_languages.keys())
        language_chosen = d_list[ch - 1]
        translator = googletrans.Translator()
        translated = translator.translate(word, src='en', dest=language_chosen)
        translated_word = translated.text.strip()
        print(f'Translating "{word}" from English to {l[ch - 1]}:')
        print(translated_word)

    print('YOUR OPTIONS:')
    print('1. DETAILS')
    print('2. TRANSLATE')
    print('3. TEST')
    ch = int(input('Enter your desired option (SL.NO): '))
    print()

    if ch == 1:
        details()
    elif ch == 2:
        translate()
    elif ch == 3:
        test()
    else:
        print('Invalid choice')

def create_profile():
    print('TO CREATE A PROFILE PLEASE ENTER THE FOLLOWING DETAILS')
    if not os.path.exists('profiles.dat'):
        profiles = []
    else:
        try:
            with open('profiles.dat', 'rb') as f:
                profiles = []
                while True:
                    try:
                        profiles.append(pickle.load(f))
                    except EOFError:
                        break
        except Exception as e:
            print(f"Error reading profiles: {e}")
            return

    name = input('ENTER USERNAME: ').strip()
    if any(profile[0] == name for profile in profiles):
        print('Username already taken')
        return

    passwd = input('CREATE PASSWORD: ').strip()
    new_profile = [name, passwd, 0, []]

    try:
        with open('profiles.dat', 'ab') as f:
            pickle.dump(new_profile, f)
    except Exception as e:
        print(f"Error saving profile: {e}")
        return

    print(f'Profile for {name} created successfully.')

if __name__ == "__main__":
    print('---------MENU----------')
    print('1. LOG IN TO YOUR PROFILE')
    print('2. CREATE A PROFILE')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        login()
    elif ch == 2:
        create_profile()
    else:
        print('Enter a valid choice')
