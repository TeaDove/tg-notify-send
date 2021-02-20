# tg_notify_send
## Telegram command line notifications sender.
tg_notify_send allow you to send messages via telegram bot api.<br>
i.e. you have launched time-consuming script and want to be notified after complition of this scripts. In terminal:<br>
`<you-script>; tg_notify_send "Work completed!"`
## Manual
```
usage: tg_notify_send [-h] [-q] [-n NUMBER] [-c CHAT_ID] [-t TOKEN] [--set_default_chat_id SET_DEFAULT_CHAT_ID] [--set_default_token SET_DEFAULT_TOKEN] [--set_preamble SET_PREAMBLE]
                      [--show_configs]
                      [message [message ...]]

positional arguments:<br>
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
  --set_default_chat_id SET_DEFAULT_CHAT_ID
                        set chat id for sending a message as default and exit
  --set_default_token SET_DEFAULT_TOKEN
                        set telegram bot api token as default and exit
  --set_preamble SET_PREAMBLE
                        set text that will be added before text, space for no preamle and exit
  --show_configs        show current configuration and exit.
```
## Instalation
### Install from source
```
git clone https://gitlab.com/TeaDove/tg_notify_send
cd tg_notify_send
pip install .
```
## Todo
- settings for parse_mode
- badges
- tests
