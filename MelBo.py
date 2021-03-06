import chatbot
import birthcongr
import reposter
import statuser
import botmemory
import simplevk
import getpass
import threading


app_id = botmemory.app_id
my_id = botmemory.my_id
access_token = botmemory.access_token
v = botmemory.api_version

chatting = botmemory.chatting
reposting = botmemory.reposting


vk = simplevk.vk()
vk.access_token = access_token
vk.v = v
vk.app_id = app_id
while('vk'):
    if access_token!="ad96fe5b51f6d9c0bd241bc4cb01afc7af0e507be9eb7e2b0995a71aa35bd2fc263537ac736d8e41fd35b":
        try:
            vk.user_id = vk.request('users.get')['response'][0]['id']
            print("Успешная авторизация")
            break
        except KeyError:
            print("Возникла ошибка, нужна авторизация")
    try:
        login = input('    Login: ')
        password = getpass.getpass('    Password: ')
        vk.authorize(botmemory.app_id, login, password, 'messages+offline+wall+friends', botmemory.api_version)
    except simplevk.AuthorizationError as autherr:
        print(autherr)
        continue
    if input('    Save password? [y/n]')=="y":
            botmemory.save_token(vk.access_token)
    print('Успешная авторизация')
    break

try:
    if chatting:
        threading.Thread(target=chatbot.start, args=(vk,)).start()
    if reposting:
        threading.Thread(target=reposter.start, args=(vk,)).start()
except Exception as e:
    print("Error: "+str(e))
#chatbot.start(vk)
#reposter.start(vk)
#birthcongr.start()
