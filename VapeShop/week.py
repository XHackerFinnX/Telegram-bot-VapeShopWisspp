def day_week(num):
    if num == 0:
        return "Понедельник"
    elif num == 1:
        return "Вторник"
    elif num == 2:
        return "Среда"
    elif num == 3:
        return "Четверг"
    elif num == 4:
        return "Пятница"
    elif num == 5:
        return "Суббота"
    elif num == 6:
        return "Воскресенье"
    
def dostavka(h, m):
    m = m + 50
    if m // 60 == 1:
        h = h + 1
        m = m - 60
        return f"{h} часов {m} минут"
    else:
        return f"{h} часов {m} минут"