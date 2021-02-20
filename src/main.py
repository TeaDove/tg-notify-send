#!/usr/bin/python3 
import argparse
import requests
import os
import configparser
import sys
import logging
import time
import pathlib

BASE_FOLDER = pathlib.Path(__file__).parent.absolute()
BASE_URL = "http://api.telegram.org"


def check_and_generate_config():
    if "config.ini" not in os.listdir(BASE_FOLDER):
        with open(f"{BASE_FOLDER}/config.ini", "w") as f:
            f.write('[credentials]\ntoken = \nchat_id = \npreamble = ')


def rewrite_config(config):
    with open(f"{BASE_FOLDER}/config.ini", "w") as f:
        config.write(f)
    # print("Done!")


def token_ok(token: int) -> bool:
    res = requests.get(f"{BASE_URL}/bot{token}/getMe")
    res_json = res.json()
    return res_json['ok']


def send_message(chat_id: int, text: str, token: int, quiet: bool = False, messages_amount: int = 1) -> bool:
    while messages_amount > 0:
        res = requests.get(f"{BASE_URL}/bot{token}/sendMessage", params = {'text': text, 'chat_id': chat_id, 
                                                                            "disable_notification": quiet, 'parse_mode': 'html'})
        res_json = res.json()
        if res_json['ok']:
            pass
        else:
            print(res_json)
            if res_json['description'].split(':')[0] == 'Too Many Requests':
                sleep_time = res_json['parameters']['retry_after']
                print(f"Sleeping for {sleep_time}s")
                time.sleep(sleep_time)
            else:
                sys.exit("Error sending message")
        messages_amount-=1


def dialog(token: str, chat_id: int):
    cur_id = -1
    res = requests.get(f"{BASE_URL}/bot{token}/getUpdates", params={'offset': cur_id, 'allowed_updates': ['message']})
    res_json = res.json()
    print(res_json)
    while True:
        try:
            if res_json['result']:
                if 'text' in res_json['result'][0]['message']:
                    print(res_json['result'][0]['message']['text'])
                cur_id = res_json['result'][0]['update_id'] + 1
            res = requests.get(f"{BASE_URL}/bot{token}/getUpdates", params={'offset': cur_id, 'allowed_updates': ['message']})
            res_json = res.json()
            time.sleep(0.2)
        except (KeyboardInterrupt, EOFError):
            print('\nBye!')
            return 

def main():
    parser = argparse.ArgumentParser(description='Send messages from your bot to user in TG via terminal command')
    parser.add_argument('message', action="store", type=str, help='text of message, that you want to send', nargs='*')
    parser.add_argument('-q', '--quiet', action="store_true", help='disable notifications for this message')
    parser.add_argument('-n', '--number', action="store", type=int, help="send same message n times, WARNING, it's stricly recomended not to send more than 30 message in row because of telegram spam control")
    parser.add_argument('-c', '--chat_id', action="store", type=int, help='use chat id for sending a message')
    parser.add_argument('-t', '--token', action="store", type=str, help='use telegram bot api token')
    parser.add_argument('--set_default_chat_id', action="store", type=str, help='set chat id for sending a message as default and exit')
    parser.add_argument('--set_default_token', action="store", type=str, help='set telegram bot api token as default and exit')
    parser.add_argument('--set_preamble', action="store", type=str, help='set text that will be added before text, space for no preamle and exit')
    parser.add_argument('--show_configs', action="store_true", help='show current configuration and exit')
    parser.add_argument('--dialog', action="store_true", help='listen for only text messages from particular chat and write them')
    args = parser.parse_args()
    check_and_generate_config()
    config = configparser.ConfigParser()
    config.read(f'{BASE_FOLDER}/config.ini')
    token = config['credentials']['token'] if args.token is None else args.token
    chat_id = config['credentials']['chat_id'] if args.chat_id is None else args.chat_id
    preamble = config['credentials']['preamble'] 
    messages_amount = 1 if args.number is None else args.number
    should_send_message = True
    if args.set_default_chat_id:
        config['credentials']['chat_id'] = args.set_default_chat_id
        rewrite_config(config)
        should_send_message = False
        print('Default chat id updated')
    if args.set_default_token:
        config['credentials']['token'] = args.set_default_token
        rewrite_config(config)
        should_send_message = False
        print('Default token updated')
    if args.set_preamble:
        config['credentials']['preamble'] = args.set_preamble if args.set_preamble else None 
        rewrite_config(config)
        should_send_message = False
        print('Preamble updated')
    if args.show_configs:
        with open(f'{BASE_FOLDER}/config.ini', 'r') as f:
            to_send = f.read()
        print(to_send)
        should_send_message = False
    if should_send_message:
        if (not token) or (not chat_id): # No tokens or chats id
            sys.exit("Token and/or chat_id is not specified!, use -c, -t or --set_default_token, --set_default_chat_id")
        elif args.dialog:
            print("Start dialog mode, Ctrl+C to exit")
            dialog(token, chat_id)
        elif not args.message: # No message
            sys.exit("No message specified")
        elif token_ok(token): # Normal mod
            send_message(chat_id, f"{preamble}{' '.join(args.message)}", token, args.quiet, messages_amount)
            print(f"{messages_amount} message(s) sent!")
        else: # Bad token 
            sys.exit(f"Bad token: {token}")


if __name__ == "__main__":
    main()
