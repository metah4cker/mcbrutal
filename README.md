# MCBrutal

[![telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&amp;logo=Telegram&amp;logoColor=white)](https://t.me/metah4cker)
[![python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&amp;logo=Python&amp;logoColor=white)](#)

### -> 🇺🇦 Текущий язык: Русский (Current language: Russian)

### -> 🇬🇧 [English language](README_EN.md)

## Контент

- 📓 [Установка](#установка)
- ❓ [Использование](#использование)
- 🛡 [Как предотвратить подобную атаку?](#как-предотвратить-подобную-атаку)
- 💎 [Meta Hacker](#meta-hacker)

------------------------------------------------------------------------------

PoC-инструмент, показывающий, как хакеры могут использовать технику Bruteforce
для взлома ваших серверов майнкрафт через RCON.

Инструмент работает подобным образом:
- Вы задаёте IP адрес вашего сервера, и если у вас RCON находится на другом
порте, отличном от 25575, вы можете его задать вручную.
- Вы задаёте путь к списку перебираемых паролей
- После запуска инструмента, вам приходится немного подождать, пока тот
пробует каждый пароль в списке.
- В случае успеха вы получите ответ о том, что ваш сервер был взломан подобным
образом.

## Установка

Вам понадобится Python (Версии 3.8+ желательно) и GIT установленный на вашем
устройстве.

Выполните эти три команды:

```shell
git clone https://github.com/metah4cker/mcbrutal.git
cd mcbrutal
pip3 install -r requirements.txt
```

Установка завершена!

## Использование

```shell
usage: mcbrutal.py [-h] [-p PORT] [-w WORDLIST] host

positional arguments:
  host                  ip-address of server

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  rcon service port (default -> 25575)
  -w WORDLIST, --wordlist WORDLIST
                        path to the wordlist (file with passwords) (default -> passwords.txt)
```

Пример:

```shell
python3 mcbrutal.py localhost -w rockyou.txt
```

## Как предотвратить подобную атаку?

Первая рекомендация: не использовать RCON. Данная технология имеет слабую защиту
и может быть взломан хакерами подобным образом (с использованием брутфорса) или
используя перехват трафика с помощью условного Wireshark (при условии, если RCON
не использует TLS).

Вторая рекомендация - использовать SSH для удалённого доступа к серверу. Это
позволит уникнуть проблем с RCON и затруднит тот же взлом с использованием
брутфорса.

<img align="left" width="180" src="https://images.weserv.nl/?url=https://github.com/metah4cker/metah4cker/raw/main/logo.jpg&fit=cover&mask=circle&maxage=7d" />
<h1><strong>META HACKER</strong></h1>

Написано специально для телеграм канала по кибербезопасности **Meta Hacker**
Подписывайся и изучай кибербезопасность вместе с нами!

-> https://t.me/metah4cker
