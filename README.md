# tg-notify-send
## Telegram command line notifications sender.
tg-notify-send allow you to send messages via telegram bot api.<br>
i.e. you have launched time-consuming script and want to be notified after complition of this scripts. i.e. terminal:<br>
`seq 99999999 | tqdm --bytes | wc -l && tg-notify-send "Work completed!"          "`
## Manual
```
usage: main.py [-h] [-q] [-n NUMBER] [-c CHAT_ID] [-t TOKEN] [--default_chat_id DEFAULT_CHAT_ID] [--default_token DEFAULT_TOKEN] [--preamble PREAMBLE] [--show_configs] [--dialog] [message [message ...]]

Send messages from your bot to user in TG via terminal command

positional arguments:
  message               text of message, that you want to send

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           disable notifications for this message
  -n NUMBER, --number NUMBER
                        send same message n times, WARNING, it's stricly recomended not to send more than 30 message in row because of telegram spam control
  -c CHAT_ID, --chat_id CHAT_ID
                        use chat id for sending a message
  -t TOKEN, --token TOKEN
                        use telegram bot api token
  --default_chat_id DEFAULT_CHAT_ID
                        set chat id for sending a message as default and exit
  --default_token DEFAULT_TOKEN
                        set telegram bot api token as default and exit
  --preamble PREAMBLE   set text that will be added before text, space for no preamle and exit
  --show_configs        show current configuration and exit
  --dialog              listen for only text messages from particular chat and write them
```
## Instalation
### Install from source
```
git clone https://github.com/TeaDove/tg-notify-send
cd tg-notify-send
pip install .
```
or just
```
pip install git+https://github.com/TeaDove/tg-notify-send
```
## Todo
- settings for parse_mode
- badges
- tests
