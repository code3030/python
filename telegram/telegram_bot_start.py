import telegram

bot = telegram.Bot(token='1838041440:AAFMy1aV3t3EDal_ePV0qxrltCKC9xshZcE')

chat_id_list = []
for i in bot.getUpdates():
    chat_id = i.message.chat.id
    if chat_id not in chat_id_list:
        bot.send_message(chat_id=chat_id, text='두번째 메세지')
        chat_id_list.append(chat_id)
        
# bot.send_message(chat_id='1843587384', text='안녕하세요~')


