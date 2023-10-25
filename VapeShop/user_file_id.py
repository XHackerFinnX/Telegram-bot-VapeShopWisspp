def users_id_all():
    global users_id
    return users_id


def users_input_consol():
    global users_id
    users_id = []
    file_id = open("id-клиетов.txt", "r", encoding="utf-8")
    for i in file_id.readlines():
        users_id.append(int(i.replace("\n", "")))
    file_id.close()
    temp = []
    for x in users_id:
        if x not in temp:
            temp.append(x)
    users_id, temp = temp, users_id
    temp.clear()
    print("На текущий момент сегодня", len(users_id), "клиент")
    print(users_id)
    return


def users_file(message):
    global users_id
    file_id = open("id-клиетов.txt", "r", encoding="utf-8")
    for i in file_id.readlines():
        users_id.append(int(i.replace("\n", "")))
    file_id.close()
    temp = []
    for x in users_id:
        if x not in temp:
            temp.append(x)
    users_id, temp = temp, users_id
    temp.clear()
    if message.chat.id in users_id:
        print('ok')
        return
    else:
        file_id = open("id-клиетов.txt", "a+", encoding="utf-8")
        file_id.writelines(f"{str(message.chat.id)}\n")
        file_id.close()
        file_users = open("Клиенты.txt", "a+", encoding="utf-8")
        file_users.writelines(
            f"Клиент {str(len(users_id)+1)}. {str(message.chat.id)}\n")
        file_users.close()
        users_id.append(message.chat.id)
        print('Ещё один клиент!')
    return
