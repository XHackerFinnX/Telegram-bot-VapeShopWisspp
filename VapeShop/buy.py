from telebot import types

def store_buy(product_name, item_number):
    markup_buy = types.InlineKeyboardMarkup()
    buy_store = types.InlineKeyboardButton("Купить в 1 клик!", callback_data = f"next{str(product_name[item_number][4])}")
    basket_store = types.InlineKeyboardButton("Добавить в корзину", callback_data = f"basket_next{str(product_name[item_number][4])}")
    markup_buy.add(buy_store, basket_store)
    return markup_buy

def applic(product_name, item_number):
    markup_applic = types.ReplyKeyboardMarkup(resize_keyboard=True)
    application = types.KeyboardButton('Заполнить заявку')
    back = types.KeyboardButton('Обратно в каталог')
    markup_applic.add(application, back)
    return markup_applic

def product_save(product_name, item_number):
    return product_name, item_number