#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

from audiobridge.config.bot import cfg as bot_cfg


class UserRequest(Enum):
    WAIT_FOR_PLAYLIST    = "Пожалуйста, дождитесь окончания загрузки плейлиста"
    EXCEED_REQUEST_LIMIT = f"Кол-во ваших запросов в общей очереди не может превышать {bot_cfg.settings.max_requests_queue}"
    BAD_REQUEST_FORMAT   = "Неверный формат запроса. Узнать правильный вы можете в инструкции (закреплённый пост в группе)"
    CANT_HANDLE_ATTACH   = "Невозможно обработать прикреплённое видео. Пришлите ссылку"
    NO_URL               = "Не обнаружена ссылка для скачивания"
    DYNAMIC_LINK         = "Ссылка является динамической. Скопируйте ссылку на данную песню по-другому"
    BUSY_PLAYLIST_QUEUE  = "Для загрузки плейлиста очередь запросов должна быть пустой"
    BAD_PLAYLIST_REQUEST = "Слишком много параметров для загрузки плейлиста"
    PRIVATE_ATTACH       = "Невозможно обработать прикреплённое видео, т.к. оно скрыто настройками приватности автора. Попробуйте авторизоваться в боте"
    BAD_RENAME_FORMAT    = "Неправильный запрос на переименовывание песни. Узнать правильный вы можете в инструкции (закреплённый пост в группе)"
    CANT_RENAME_AUDIO    = "Невозможно переименовать песню. Попробуйте позже или обратитесь к разработчикам"


    def __new__(cls, description: str):
        obj             = object.__new__(cls)
        obj._value_     = len(cls.__members__) + 1000
        obj.description = description
        return obj
