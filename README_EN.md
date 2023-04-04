# MCBrutal

[![telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&amp;logo=Telegram&amp;logoColor=white)](https://t.me/metah4cker)
[![python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&amp;logo=Python&amp;logoColor=white)](#)

### -> 🇬🇧 Current language: English

### -> 🇺🇦 [Русский язык (Russian language)](README.md)

## Contents

- 📓 [Installation](#installation)
- ❓ [Usage](#usage)
- 🛡 [How to prevent such an attack?](#how-to-prevent-such-an-attack)
- 💎 [Meta Hacker](#meta-hacker)

--------------------------------------------------------------------------

PoC-tool showing how hackers can use the Bruteforce technique to hack your
minecraft servers through RCON.

The tool works like this:
- You set the IP address of your server, and if you have RCON located on another
port other than 25575, you can set it manually.
- You set the path to the list of passwords (wordlist)
- After starting the tool, you have to wait a little while it tries every password
in the list.
- If successful, you will receive a response that your server has been hacked like
by this method.

## Installation

You will need Python (Version 3.8+ preferred) and GIT installed on your device.

Run these three commands:

```shell
git clone https://github.com/metah4cker/mcbrutal.git
cd mcbrutal
pip3 install -r requirements.txt
```

Installation completed!

## Usage

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

Example:

```shell
python3 mcbrutal.py localhost -w rockyou.txt
```

## How to prevent such an attack?

First recommendation: don't use RCON. This technology is weak and can be hacked by
hackers in a similar way (using brute force) or using conditional Wireshark sniffing
(assuming RCON does not use TLS).

The second recommendation is to use SSH to access the server remotely. This will make
it possible to get rid of problems with RCON and make the same hacking more difficult
using brute force.

<img align="left" width="180" src="https://images.weserv.nl/?url=https://github.com/metah4cker/metah4cker/raw/main/logo.jpg&fit=cover&mask=circle&maxage=7d" />
<h1><strong>META HACKER</strong></h1>

Written specifically for the cybersecurity telegram channel **Meta Hacker**
Subscribe and learn cybersecurity with us!

-> https://t.me/metah4cker
