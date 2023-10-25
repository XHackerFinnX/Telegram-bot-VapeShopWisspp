from telebot import types

markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_store = types.KeyboardButton('Начать')
markup_start.add(start_store)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
catalog = types.KeyboardButton('Каталог')
stock = types.KeyboardButton('Акция')
scores = types.KeyboardButton('Баллы')
maps = types.KeyboardButton('Доставка')
support_store = types.KeyboardButton('Поддержать')
basket = types.KeyboardButton('Мои товары')
markup_menu.add(catalog, stock, basket, scores, maps, support_store)

markup_applic = types.ReplyKeyboardMarkup(resize_keyboard=True)
application = types.KeyboardButton('Заполнить заявку')
back = types.KeyboardButton('Обратно в каталог')
markup_applic.add(application, back)

markup_basket = types.ReplyKeyboardMarkup(resize_keyboard=True)
application = types.KeyboardButton('Заполнить заявку')
back = types.KeyboardButton('Обратно в каталог')
clear = types.KeyboardButton('Убрать товары')
markup_basket.add(application, clear, back)

markup_rem = types.ReplyKeyboardRemove()

markup_continue = types.ReplyKeyboardMarkup(resize_keyboard=True)
mar_con = types.KeyboardButton('Продолжить')
markup_continue.add(mar_con)

markup_catalog = types.ReplyKeyboardMarkup(resize_keyboard=True)
single = types.KeyboardButton('Одноразовые ЭС')
liquid = types.KeyboardButton('Жидкости')
name_stock = types.KeyboardButton('Товары по акции')
back = types.KeyboardButton('Назад')
markup_catalog.add(single, liquid, name_stock, back)

markup_catalog_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
liquid = types.KeyboardButton('Жидкости')
name_stock = types.KeyboardButton('Товары по акции')
back = types.KeyboardButton('Назад')
markup_catalog_1.add(liquid, name_stock, back)

markup_catalog_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
single = types.KeyboardButton('Одноразовые ЭС')
name_stock = types.KeyboardButton('Товары по акции')
back = types.KeyboardButton('Назад')
markup_catalog_2.add(single, name_stock, back)

markup_catalog_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
single = types.KeyboardButton('Одноразовые ЭС')
liquid = types.KeyboardButton('Жидкости')
back = types.KeyboardButton('Назад')
markup_catalog_3.add(single, liquid, back)

markup_stocks = types.ReplyKeyboardMarkup(resize_keyboard=True)
name_stock = types.KeyboardButton('Товары по акции')
back = types.KeyboardButton('Назад')
markup_stocks.add(name_stock, back)
