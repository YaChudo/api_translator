import requests
import config

URL_AUTH = config.URL_AUTH
URL_TRANSLATE = config.URL_TRANSLATE
KEY1 = config.KEY1

headers_auth = {'Authorization': 'Basic ' + KEY1}
auth = requests.post(URL_AUTH, headers=headers_auth)

x = input('Привет! Я переводчик, выбери цифру, как тебе необходимо перевести слова - '
          '\n с русского на английский - 1,'
          '\n с английского на русский - 2, '
          '\nс немецкого на русский - 3,'
          '\n с русского на немецкий - 4?'
          '\n')

if x == str(1) or x == int(1):
    dstLang = '1033'
    srcLang = '1049'
elif x == str(2) or x == int(2):
    dstLang = '1049'
    srcLang = '1033'
elif x == str(3) or x == int(3):
    dstLang = '1049'
    srcLang = '1031'
elif x == str(4) or x == int(4):
    dstLang = '1031'
    srcLang = '1049'
else:
    exit('Не верно выбран перевод! Необходимо прописать цифру от 1 до 4')
if auth.status_code == 200:
    token = auth.text
    while True:
        word = input('введите слово для перевода...  '
                     '\n Для выхода из программы - прописать "!выйти" или "!break" ')

        if word == '!break' or word == '!выйти':
            break

        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': srcLang,
                'dstLang': dstLang
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найден перевод')

else:
    print('Error!')
