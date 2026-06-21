# EM System

## Introduction
Django проект аутентификации(PASETO) и авторизации.  

## Installation
```aiignore
pip install -r requirements/development.txt
```

## Environment
файл настроки окружения .env
```
DJANGO_CONFIGURATION=Development
SECRET_KEY="kh@!()&g7e-7$2u$w*y9lj)dzm-lveuq!0_zhhdze)0du$99np"
```

## Authentication
Для аутентификации будем использовать [PASETO](https://paseto.io/). На данный момент RFC для PASETO не принят и находится в статусе [черновика](https://www.ietf.org/archive/id/draft-paragon-paseto-rfc-01.txt). Реализация основана на [pyseto](https://github.com/dajiaji/pyseto). В проекте по умолчанию используется версия шифрования v4.local. Токен хранится в куки. При выходе из системе(logout) токен удаляется. 

## Authorization
Для авторизация используется - DjangoModelPermissions

"api/v1/users/" - endpoint предназначен для пользователей уровня staff(is_staff). Выводит список пользователей. Для конечного пользователя(api/v1/users/{id}) возможно изменения данных и доступов. 