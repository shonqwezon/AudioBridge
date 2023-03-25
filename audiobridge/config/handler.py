#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

import vk_api


@dataclass
class WorkerTask:
    msg_start   : int  # id сообщения с добавлением запроса в очередь пользователя
    user_id     : int  # id пользователя
    msg_reply   : int  # id сообщения запроса пользователя
    url         : str  # Ссылка на песню
    song_name   : str = None  # Название песни
    song_author : str = None  # Автор песни
    interval    : str = None  # Временной интервал
    pl_type     : bool = False # Если True, то запрос является плейлистом
    pl_param    : str = ''  # Параметры для скачивания плейлиста (количество и/или номера песен в плейлисте)
    pl_element  : int = None # Порядковый номер элемента в плейлисте
    pl_size     : int = None  # Размер плейлиста


@dataclass
class Api:
    bot         : vk_api.vk_api.VkApiMethod
    agent       : vk_api.vk_api.VkApiMethod
    agent_upload: vk_api.VkUpload

@dataclass
class Handler:
    api         : Api
    userRequests: dict
    queue       : 'audiobridge.bot.QueueHandler'
    playlist    : 'audiobridge.bot.PlaylistHandler'
    vk          : 'audiobridge.bot.VkBotWorker'
    db          : 'audiobridge.bot.DataBase'


vars = Handler
