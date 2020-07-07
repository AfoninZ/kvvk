# -*- coding: utf-8 -*-
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import sys
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from db import Database, User, Group

token = '310c422c4c0efa5c7cb7de424733155e583617ccf0140d5a529572cd1f08ed5553b765fa3a5e82dc0af70'
vk_session = vk_api.VkApi(token=token, api_version='5.89')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
DB = Database()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
        user = DB.get_user(uid=int(event.user_id))
        print(user.location)
        if user.role == 'teacher':
            pass
        elif user.role == 'student':
            pass
        elif user.role == 'parent':
            pass
        elif user.role == 'admin':
            if user.location == 'homepage':
                if event.text == 'Учебные группы':
                    user.location = 'stud_groups'
                    DB.update_user(user)
                    keyboard = VkKeyboard(one_time=True)
                    kvantums = [i[0] for i in DB.cursor.execute("SELECT name FROM kvantums").fetchall()]
                    print(kvantums)
                    for i in range(len(kvantums)):
                        if i % 2 == 0:
                            keyboard.add_button(kvantums[i], color=VkKeyboardColor.PRIMARY)
                        else:
                            keyboard.add_button(kvantums[i], color=VkKeyboardColor.PRIMARY)
                            keyboard.add_line()
                    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Выберете квантум',
                        keyboard=keyboard.get_keyboard())
                elif event.text == 'Учителя':
                    user.location = 'teachers_group'
                    DB.update_user(user)
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Раздел УЧИТЕЛЯ',
                        keyboard=keyboard.get_keyboard())
                elif event.text == 'Банлист':
                    user.location = 'banlist'
                    DB.update_user(user)
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Раздел БАНЛИСТ',
                        keyboard=keyboard.get_keyboard())
                else:

                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button('Учебные группы', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button('Учителя', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Банлист', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Неизвестная команда',
                        keyboard=keyboard.get_keyboard())
            elif user.location == 'stud_groups':
                kvantums = [i[0] for i in DB.cursor.execute("SELECT name FROM kvantums").fetchall()]
                if event.text == 'Назад':
                    user.location = 'homepage'
                    DB.update_user(user)
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button('Учебные группы', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button('Учителя', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Банлист', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Возврат',
                        keyboard=keyboard.get_keyboard())
                else:
                    keyboard = VkKeyboard(one_time=True)

                    for i in range(len(kvantums)):
                        if i % 2 == 0:
                            keyboard.add_button(kvantums[i], color=VkKeyboardColor.PRIMARY)
                        else:
                            keyboard.add_button(kvantums[i], color=VkKeyboardColor.PRIMARY)
                            keyboard.add_line()
                    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Неизвестная команда',
                        keyboard=keyboard.get_keyboard())
