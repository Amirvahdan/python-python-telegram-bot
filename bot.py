import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.ext import *
from telegram.update import Update
from telegram.chataction import ChatAction
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton , InlineKeyboardMarkup

buttons = {
    
    'contact us' : 'راه تماس',
    'creator id' : 'آیدی سازنده',
    'text bank' : 'بانک متن ها',
    'search games' : 'جست و جوی بازی',


    
    'hello' : 'سلام',
    'how are you' : 'حالت چطوره؟',
    'back button' : 'بازگشت',
    'bagher_image' : 'دریافت تصویر',
    'links' : 'لینک سایت های دانلود',
    'farsroid' : 'لینک فارسروید'
 
}


token = '6178195928:AAFfOeT_Y4drjE73iVZclbxdtKyeRXvSNQw'
updater = Updater(token)
bot = Bot(token)
commands=['/commandslist','/start','/chatid','/Sum','/gif','/conversation']
FIRST , SECOND = range(2)

def start(update : Update, context= CallbackContext):
    chat_id=update.message.chat_id
    U_name=update.message.from_user.username
    Full_name=update.message.from_user.full_name
    
    if U_name==None:
        bot.send_chat_action(chat_id,ChatAction.TYPING)
        bot.send_message(chat_id,f'سلام {Full_name}\n       به بات تست باقر خوش آمدی!')

    else:
        bot.send_chat_action(chat_id,ChatAction.TYPING)
        bot.send_message(chat_id,f'سلام {Full_name}\n       به بات تست باقر خوش آمدی!\n\nنام کاربری: @{U_name}')
    main_menu(update,context)

def chat_id(update : Update , context=CallbackContext):
    chat_id=update.message.chat_id
    bot.send_chat_action(chat_id,ChatAction.TYPING)
    bot.send_message(chat_id,f'چت آیدی شما: {chat_id}')

def commands_list(update: Update , context= CallbackContext):
    chat_id=update.message.chat_id
    commandsList=['\n'+i for i in commands]
    commandsSTR=''.join(commandsList)
    bot.send_chat_action(chat_id,ChatAction.TYPING)
    bot.send_message(chat_id,f'لیست دستورهای ربات{commandsSTR}')

#calculate the total of numbers given as args
def Sum(update : Update, context: CallbackContext):
    chat_id=update.message.chat_id
    numbers = context.args
    result = sum( int(i) for i in numbers)
    display='+'.join(numbers)
    if len(numbers)==0:
        
        bot.send_chat_action(chat_id,ChatAction.TYPING)
        update.message.reply_text(text='دستور اشتباه است\n\nنمونه: sum 2 3/')
    else:
        bot.send_chat_action(chat_id,ChatAction.TYPING)
        update.message.reply_text(text=f'{display}=\n\n{result}')
def main_menu(update:Update,context:CallbackContext):
    glass=[
        [buttons['search games'],buttons['creator id']],
        [buttons['text bank'],buttons['bagher_image']],
        [buttons['links'],buttons['farsroid']],
        [buttons['contact us']]
    ]
    update.message.reply_text(text='منوی اصلی',reply_markup=ReplyKeyboardMarkup(glass,resize_keyboard=True))

def text_bank(update:Update, context:CallbackContext):
    glass=[
        [buttons['hello'],buttons['how are you']],
        [buttons['back button']]
    ]
    update.message.reply_text(text='بانک متن ها',reply_markup=ReplyKeyboardMarkup(glass,resize_keyboard=True))

def back_btn(update:Update, context:CallbackContext):
    main_menu(update,context)

def creator_id(update:Update, context:CallbackContext):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'آیدی توسعه دهندی:\n\n@ArzemoonShekarchian')

def contact(update:Update, context:CallbackContext):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'راه های تماس\n\nشماره تلفن: +989331921323\nپست الکترونیکی: amirmohammadvahdani@gmail.com')

def hello_response(update:Update, context: CallbackContext):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'سلام')

def greetings_response(update:Update, context: CallbackContext):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'خوبم, توچطوری؟')

def bagher_image(update:Update,context:CallbackContext):
    chat_id = update.message.chat_id
    with open("./Pics/باقر.PNG",'rb') as img:
        bot.send_chat_action(chat_id,ChatAction.UPLOAD_PHOTO)
        bot.sendPhoto(chat_id,img,caption='تصویر ربات باقر')

def link(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    glass_links=[
        [InlineKeyboardButton('SarzaminDownload.cpm','https://www.sarzamindownload.com'),
        InlineKeyboardButton('YasDownload.com','https://www.yasdl.com/')]
    ]
    with open('./Pics/دانلود.png','rb') as dlimg:
        bot.send_chat_action(chat_id,ChatAction.UPLOAD_PHOTO)
        bot.sendPhoto(chat_id,dlimg,caption='جهت ادامه دانلود یک سایت را نتخاب کنید...',reply_markup= InlineKeyboardMarkup(glass_links))
    
def gif(update: Update, context: CallbackContext):
    chat_id= update.message.chat_id
    bot.send_chat_action(chat_id,ChatAction.UPLOAD_VIDEO)
    bot.sendVideo(chat_id,'https://media.emailonacid.com/wp-content/uploads/2019/03/2019-GifsInEmail.gif',caption='گیف')

def farsroid_link(update: Update,context: CallbackContext):
    glass_button=[
        [InlineKeyboardButton('سایت فارسروید',callback_data='farsroid')]
    ]
    update.message.reply_text(text='برای دریافت لینک سایت فارسروید کلیک کنید',reply_markup=InlineKeyboardMarkup(glass_button))

def query_(update: Update, context: CallbackContext):
    query= update.callback_query
    data= query.data
    chat_id= query.message.chat_id
    message_id=query.message.message_id
    if data=='farsroid':
        text= "https://farsroid.com"
    bot.editMessageText(text=text, chat_id=chat_id, message_id=message_id)

def site_conv(update:Update, context:CallbackContext):
    

    button= [
        [
          InlineKeyboardButton('فارسروید',callback_data='fars'),
          InlineKeyboardButton('یاس دانلود',callback_data='yasdl')  
        ]
    ]
    
    update.message.reply_text(text='لطفا یک گزینه را انتخاب نمایید',reply_markup=InlineKeyboardMarkup(button))

    return FIRST

def fars_conv(update: Update, context: CallbackContext):
    query= update.callback_query
    chat_id= query.message.chat_id
    message_id=query.message.message_id

    button=[
        [
            InlineKeyboardButton('دانلود بازی',callback_data='mobile game'),
            InlineKeyboardButton('دانلود برنامه',callback_data='mobile app')
        ],
        [
            InlineKeyboardButton('بازگشت',callback_data='return')
        ]
    ]
    bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=InlineKeyboardMarkup(button))
    
    return SECOND



def yas_conv(update: Update, context: CallbackContext):
    query= update.callback_query
    chat_id= query.message.chat_id
    message_id=query.message.message_id
    button=[
        [
            InlineKeyboardButton('دانلود بازی',callback_data='pc game'),
            InlineKeyboardButton('دانلود برنامه',callback_data='pc app')
        ],
        [
            InlineKeyboardButton('بازگشت',callback_data='return')
        ]
    ]
    bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,reply_markup=InlineKeyboardMarkup(button))
    return SECOND





def give_link(update: Update, context: CallbackContext):
    query= update.callback_query
    chat_id= query.message.chat_id
    message_id=query.message.message_id
    data=query.data
    
    mob_game_link='https://www.farsroid.com/cat/application'
    mob_app_link='https://www.farsroid.com/cat/application'
    pc_game_link='https://www.yasdl.com/category/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d8%a8%d8%a7%d8%b2%db%8c-%da%a9%d8%a7%d9%85%d9%be%db%8c%d9%88%d8%aa%d8%b1-game-pc-2'
    pc_app_link='https://www.yasdl.com/category/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d9%86%d8%b1%d9%85-%d8%a7%d9%81%d8%b2%d8%a7%d8%b1-software-tool'
    
    text=False
    match data:
        case 'mobile game':
            text=mob_game_link
        case 'mobile app':
            text=mob_app_link
        case 'pc game':
            text=pc_game_link
        case 'pc app':
            text=pc_app_link
        case 'return':
            back_query(update, context)
            return FIRST
    if text==False:
        pass
    else:    
        bot.editMessageText(text=text,chat_id=chat_id,message_id=message_id)
    
def back_query(update: Update, context: CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat_id
    message_id=query.message.message_id

    button=button= [
        [
          InlineKeyboardButton('فارسروید',callback_data='fars'),
          InlineKeyboardButton('یاس دانلود',callback_data='yasdl')  
        ]
    ]

    context.bot.edit_message_reply_markup(chat_id=chat_id,message_id=message_id,
    reply_markup=InlineKeyboardMarkup(button))

def games_searcher():
    HTML_text= requests.get('https://www.farsroid.com/?s=%D8%A8%D8%A7%D8%B2%DB%8C').text
    soup= BeautifulSoup(HTML_text, 'lxml')
    result_boxes=soup.find_all('article',class_='post-item-wide')
    desciption=soup.find_all('div',class_='excerpt')
    des_list=[(des.p.text)[:100] for des in desciption]

    final_text=''
    for index,tag in enumerate(result_boxes):
        games_title=tag.h2.a.text
        games_link=tag.h2.a['href']
        final_text=games_title+'\n'+des_list[index]+'\n'+games_link+'\n\n\n\n'
    return final_text

def search_result(update: Update, contex: CallbackContext):
    update.message.reply_text(games_searcher())




def main():
    conv_handler=ConversationHandler(

        entry_points=[CommandHandler('conversation',site_conv)],
        states={
            FIRST :[
                CallbackQueryHandler(fars_conv,pattern='^fars$'),
                CallbackQueryHandler(yas_conv,pattern='^yasdl$')
            ],
            
            SECOND :[
                CallbackQueryHandler(give_link)
            
            ]
            
        },
        fallbacks=[CommandHandler('conversation',site_conv)],
        allow_reentry=True
    )
        
    updater.dispatcher.add_handler(conv_handler)

    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CommandHandler('commandslist',commands_list))
    updater.dispatcher.add_handler(CommandHandler('chatid',chat_id))
    updater.dispatcher.add_handler(CommandHandler('sum',Sum))
    updater.dispatcher.add_handler(CommandHandler('gif',gif))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['text bank']),text_bank))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['back button']),back_btn))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['creator id']),creator_id))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['contact us']),contact))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['hello']),hello_response))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['how are you']),greetings_response))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['bagher_image']),bagher_image))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['links']),link))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['farsroid']),farsroid_link))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(buttons['search games']),search_result))

    updater.dispatcher.add_handler(CallbackQueryHandler(query_))

    updater.start_polling()
    updater.idle()

main()
