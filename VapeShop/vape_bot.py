import telebot
from db.store import name_all, name_single, name_liquid, name_stock_all
from db.sql_files import sql_name_single, sql_name_liquid, sql_name_stock_all
from keyboard import markup_start, markup_menu, markup_applic, markup_rem, markup_catalog, markup_catalog_1, markup_catalog_2, markup_catalog_3, markup_stocks, markup_continue, markup_basket
#from user_file_id import users_file, users_input_consol, users_id_all
from buy import store_buy, applic, product_save
from background import keep_alive
import time
import datetime
from week import day_week, dostavka

# Бот телеграмма
bot = telebot.TeleBot("TOKEN")

print("Я работаю!")
# Приветсвие
seconds = time.time()
result = time.localtime(seconds)
date = datetime.datetime(result.tm_year, result.tm_mon, result.tm_mday)
basket_store = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, "Добро пожаловать в вейп шоп Wisspp!\n Это магазин, который продает одноразки, жижи и т.д.\n Пользуйся нашим магазином! Мы всегда тебе рады!", reply_markup=markup_start)

# Количество пользователей, которые зашли сегодня


#@bot.message_handler(commands=['users'])
#def users_sum(message):
#    admin = [678570906, 1387002896]
#    if message.chat.id not in admin:
#        bot.send_message(message.chat.id, 'Ваши права ограничены!')
#    else:
#        bot.send_message(
#            message.chat.id, f'Сегодня зашло {len(1)} людей')

# Перемещение по боту

@bot.message_handler(content_types=['text'])
def shop(message):
    global spisok, basket_store, charhe
    # Главная страница
    if message.text == "Каталог":
        bot.send_message(message.chat.id, "Каталог товаров:")
        bot.send_message(message.chat.id, "Чего желаете? \n Одноразовые ЭС \n Жидкости для вейпа \n Товары по акции", reply_markup=markup_catalog)
    elif message.text == "Акция":
        bot.send_message(message.chat.id, "Акции проходят каждые две недели на определенные товары")
        bot.send_message(message.chat.id, "Посмотреть товары по акции?",reply_markup= markup_stocks)
    elif message.text == "Мои товары":
        if len(basket_store) == 0:
            bot.send_message(message.chat.id, "Ваша корзина пуста")
        else:
            bot.send_message(message.chat.id, "Ваши товары")
            charhe = 0
            for i in range(len(basket_store)):
                charhe = charhe + basket_store[i][1]
                bot.send_message(message.chat.id, f"{i+1}.{basket_store[i][0]}\n", reply_markup=markup_rem)
            bot.send_message(message.chat.id, f"Сумма покупки: {charhe}", reply_markup= markup_basket)
    elif message.text == "Убрать товары":
        basket_store = []
        bot.send_message(message.chat.id, "Ваша корзина пуста", reply_markup= markup_menu)
    elif message.text == "Баллы":
        bot.send_message(message.chat.id, "Ещё нет")
    elif message.text == "Доставка":
        bot.send_message(
            message.chat.id, "Доставку осуществялем по Пушкину и Колпино")
    elif message.text == "Поддержать":
        file_qr = open("db\\photo_file\\qrcode.jpg", "rb")
        bot.send_message(
            message.chat.id, "Для продвижения магазина будем рады любой копейке. Спасибо)")
        bot.send_photo(message.chat.id, file_qr)
    # Вернуться на главную страницу или каталог
    elif message.text == "Обратно в каталог":
        spisok = 0
        bot.send_message(message.chat.id, "Каталог товаров:")
        bot.send_message(message.chat.id, "Чего желаете? \n Одноразовые ЭС \n Жидкости для вейпа \n Товары по акции", reply_markup=markup_catalog)
    elif (message.text == "Назад") or (message.text == "Начать"):
        bot.send_message(message.chat.id, "Главная страница магазина")
        bot.send_message(message.chat.id, "Чего желаете?",
                         reply_markup=markup_menu)
    # Каталог товаров
    elif message.text == "Одноразовые ЭС":
        bot.send_message(message.chat.id, text='Все товары "Одноразовые ЭС"', reply_markup=markup_catalog_1)
        for i in range(1, len(name_single)+1):
            file_one_es = open(name_single[i][3], "rb")
            bot.send_photo(message.chat.id, file_one_es, f"{name_single[i][0]}.\n В наличии {name_single[i][2]}\n Цена: {name_single[i][1]}", reply_markup=store_buy(name_single, i))
            time.sleep(0.7)
    elif message.text == "Жидкости":
        bot.send_message(message.chat.id, text='Все товары "Жидкоски"', reply_markup=markup_catalog_2)
        for i in range(1, len(name_liquid)+1):
            file_liquids = open(name_liquid[i][3], "rb")
            bot.send_photo(message.chat.id, file_liquids, f"{name_liquid[i][0]}.\n В наличии {name_liquid[i][2]}\n Цена: {name_liquid[i][1]}", reply_markup=store_buy(name_liquid, i))
            time.sleep(0.7)
    elif message.text == "Товары по акции":
        bot.send_message(message.chat.id, text='Все товары "Товары по акции"', reply_markup=markup_catalog_3)
        for i in range(1, len(name_stock_all)+1):
            file_stocks = open(name_stock_all[i][5], "rb")
            bot.send_photo(message.chat.id, file_stocks, f"{name_stock_all[i][0]}.\n" 
                                            f"В наличии {name_stock_all[i][2]}\n"
                                            f"Старая цена: "
                                            f"{str(name_stock_all[i][1])}\n" 
                                            f"Новая цена: {name_stock_all[i][3]}", reply_markup=store_buy(name_stock_all, i))
            time.sleep(0.7)
    # Отправить заявку на покупку товара
    elif message.text == "Заполнить заявку":
        bot.register_next_step_handler(message, sent_form)
        bot.send_message(message.chat.id, "Продолжить покупку товара?", reply_markup = markup_continue)
        
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю!")

spisok = 0

@bot.callback_query_handler(func=lambda callback: True)
def send_random_value(callback):
    global spisok, basket_store
    for i in name_single:
        if callback.data == f"next{name_single[i][4]}":
            file_one_es = open(name_single[i][3], "rb")
            spisok = sql_name_single(name_single[i][4])
            bot.send_photo(callback.message.chat.id, file_one_es, f"Заполните заявку на товар {name_single[i][0]}\n Цена: {name_single[i][1]}", reply_markup=markup_applic)
        elif callback.data == f"basket_next{name_single[i][4]}":
            basket_store.append(sql_name_single(name_single[i][4]))
            bot.send_message(callback.message.chat.id, "Хороший выбор", reply_markup=markup_catalog)
    for j in name_liquid:
        if callback.data == f"next{name_liquid[j][4]}":
            file_liquids = open(name_liquid[j][3], "rb")
            spisok = sql_name_liquid(name_liquid[j][4])
            bot.send_photo(callback.message.chat.id, file_liquids, f"Заполните заявку на товар {name_liquid[j][0]}\n Цена: {name_liquid[j][1]}", reply_markup=markup_applic)
        elif callback.data == f"basket_next{name_liquid[j][4]}":
            basket_store.append(sql_name_liquid(name_liquid[j][4]))
            bot.send_message(callback.message.chat.id, "Хороший выбор", reply_markup=markup_catalog)
    for k in name_stock_all:
        if callback.data == f"next{name_stock_all[k][4]}":
            file_stocks = open(name_stock_all[k][5], "rb")
            spisok = sql_name_stock_all(name_stock_all[k][4])
            bot.send_photo(callback.message.chat.id, file_stocks, f"Заполните заявку на товар {name_stock_all[k][0]}\n Цена: {name_stock_all[k][1]}", reply_markup=markup_applic)
        elif callback.data == f"basket_next{name_stock_all[k][4]}":
            basket_store.append(sql_name_stock_all(name_stock_all[k][4]))
            bot.send_message(callback.message.chat.id, "Хороший выбор", reply_markup=markup_catalog)
# Функция которая создает заявку пользователь

def sent_form(message):
    global spisok, basket_store, charhe
    print(spisok)
    print(basket_store)
    chat_id = message.chat.id
    admin_id_andry = 678570906
    admin_id_alex = 1387002896

    app_fio = []
    app_bond = []
    app_map = []
    app_com = []
    app_items = []
    app_price = []
    app_first_name = []
    app_user_name = []

    def fio(message):
        text_username = message.text
        app_fio.append(text_username)
        bot.register_next_step_handler(message, bond)
        bot.send_message(message.chat.id, f"Ваша почта или номер телефон:\n")

    def bond(message):
        text_bond = message.text
        app_bond.append(text_bond)
        bot.register_next_step_handler(message, adres)
        bot.send_message(message.chat.id, f"Адрес куда доставить:\n")

    def adres(message):
        text_map = message.text
        app_map.append(text_map)
        bot.register_next_step_handler(message, send_data)
        bot.send_message(message.chat.id, f"Комментарий к товару:\n")

    def send_data(message):
        global spisok, basket_store, charhe
        text_com = message.text
        app_com.append(text_com)
        bot.send_message(admin_id_andry,f"Пришла заявка от пользователя:\n" 
                                        f"{day_week(date.weekday())}. Дата: {result.tm_mday}.{result.tm_mon}.{result.tm_year} Время: {result.tm_hour}:{result.tm_min}:{result.tm_sec} \n"
                                        f"Товар клиента: {[(i+1, app_items[i]) for i in range(len(app_items))]} На сумму {app_price}\n"
                                        f"ФИО: {app_fio} \n"
                                        f"Телеграмм: \n Имя - {app_first_name}.\n Его ссылка - {app_user_name} \n id клиента - {message.chat.id} \n"
                                        f"Связаться с клиентом: {app_bond} \n"
                                        f"Адрес: {app_map} \n"
                                        f"Комментарий: {app_com} \n",
                                        reply_markup=markup_menu)
        bot.send_message(admin_id_alex, f"Пришла заявка от пользователя:\n" 
                                        f"{day_week(date.weekday())}. Дата: {result.tm_mday}.{result.tm_mon}.{result.tm_year} Время: {result.tm_hour}:{result.tm_min}:{result.tm_sec} \n"
                                        f"Товар клиента: {[(i+1, app_items[i]) for i in range(len(app_items))]} \n На сумму {app_price} руб\n"
                                        f"ФИО: {app_fio} \n"
                                        f"Телеграмм: \n Имя - {app_first_name}.\n Его ссылка - {app_user_name} \n id клиента - {message.chat.id} \n"
                                        f"Связаться с клиентом: {app_bond} \n"
                                        f"Адрес: {app_map} \n"
                                        f"Комментарий: {app_com} \n",
                                        reply_markup=markup_menu)
        bot.send_message(chat_id, f"Заявка отправлена! С вами свяжуться в ближайшее время.\n"
                                    f"Приблизительное время доставки:\n В {dostavka(result.tm_hour, result.tm_min)}")

        app_items.clear()
        app_fio.clear()
        app_first_name.clear()
        app_user_name.clear()
        app_bond.clear()
        app_map.clear()
        app_com.clear()
        app_price.clear()
        spisok = 0
        basket_store = []
        charhe = []
        return

    first_name = message.chat.first_name
    user_name = message.chat.username
    app_first_name.append(str(first_name))
    app_user_name.append("@" + str(user_name))

    if spisok == 0:
        for i in basket_store:
            app_items.append(i[0])
        app_price.append(charhe)
    else:
        app_items.append(spisok[0])
        app_price.append(spisok[1])
    bot.register_next_step_handler(message, fio)
    bot.send_message(message.chat.id, f"Ваше ФИО:\n", reply_markup=markup_rem)

keep_alive()
bot.infinity_polling()
