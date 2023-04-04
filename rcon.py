#!/usr/bin/python3

'''
    Специально разработано для канала Meta Hacker.
    Присоиденяйся к нам! -> https://t.me/metah4cker

    Specially developed for the Meta Hacker channel.
    Join us now! -> https://t.me/metah4cker

    ================================================

    MCBrutal
    Copyright (C) 2023  Meta Hacker

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import mcrcon
import time
import sys
import argparse

from colorama import init, just_fix_windows_console, Fore, Style

printi = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.CYAN}i{Fore.RESET}]{Style.RESET_ALL}', *a, **kw)
printe = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTRED_EX}-{Fore.RESET}]', *a, **kw)
prints = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]', *a, **kw)

def rcon(host='localhost', port=25575, password='test'):

    printi(f'RCON | Connection to host: {host} by port: {port}')
    printi('Specially written for the Meta Hacker channel | https://t.me/metah4cker')

    try:
        mr = mcrcon.MCRcon(host, password, port)
        mr.connect()
    except Exception as e:
        printe(f'Cannot connect to the server{Style.RESET_ALL}')
        return

    try:
        while 1: print(mr.command(input('> ')))
    except Exception as e:
        printe('Error occurred while sending command:', e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host',
                        help='IP-address of server')
    parser.add_argument('-P', '--port',
                        type=int,
                        default=25575,
                        help='rcon service port (default -> 25575)')
    parser.add_argument('-p', '--password',
                        default='123456',
                        help='path to the wordlist (file with passwords) (default -> passwords.txt)')

    args = parser.parse_args()

    rcon(args.host, args.port, args.password)
