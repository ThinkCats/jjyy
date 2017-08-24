TelegramBot = require 'node-telegram-bot-api'

token = '415743257:AAGGsScMruUFIabgtBV6AXFYRPOIJCQ_2Is'

bot = new TelegramBot(token,
    polling: true
)

bot.on 'message', (msg) ->
    console.log msg
