import telebot
import logging
import os

# ============================================
# ДАННЫЕ ИЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ (на BotHost)
# ============================================
TOKEN = "8667946531:AAFA87hpZiHEXp7z3utaW5JassSd9fpLCUA"          # Токен от BotFather
GAME_URL = os.environ.get('GAME_URL')        # Ссылка на игру (потом вставишь)

# ============================================
# НАСТРОЙКА ЛОГИРОВАНИЯ
# ============================================
logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot(TOKEN)

# ============================================
# ТВОЁ ПРИВЕТСТВИЕ (КОТОРОЕ ТЫ НАПИСАЛ)
# ============================================
WELCOME_TEXT = """
 Приветствую, Леля! С Международным женским днём — 8 марта!

Зима позади, дни длиннее, пуховики в шкафу, холода закончились, тёплые дни впереди. В общем, пришла весна, и ты прекрасна. Неважно, что слякоть и лужи, зато весна!!!

Мне давно хотелось разобраться, как вообще работает телеграм-бот, и попробовать сделать как-нибудь, и решил, что это неординарный способ поздравить.

Это пробный бот в формате викторины, так что, если что-то поломалось, прости, ты — тестировщик.

В общем, с 8 марта! 
"""

# ============================================
# КОМАНДА /start - ГЛАВНЫЙ СТАРТ
# ============================================
@bot.message_handler(commands=['start'])
def start(message):
    # Создаём клавиатуру с одной большой кнопкой "СТАРТ"
    markup = telebot.types.InlineKeyboardMarkup()
    start_button = telebot.types.InlineKeyboardButton(
        text="СТАРТ", 
        callback_data="show_game_button"  # При нажатии покажем кнопку с игрой
    )
    markup.add(start_button)
    
    # Отправляем твоё приветствие
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=markup
    )

# ============================================
# ОБРАБОТЧИК НАЖАТИЯ КНОПКИ "СТАРТ"
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "show_game_button")
def show_game_button(call):
    # Создаём кнопку для открытия игры
    markup = telebot.types.InlineKeyboardMarkup()
    game_button = telebot.types.InlineKeyboardButton(
        text="ЗАПУСТИТЬ ВИКТОРИНУ", 
        web_app=telebot.types.WebAppInfo(GAME_URL)  # Открывает игру
    )
    markup.add(game_button)
    
    # Редактируем предыдущее сообщение (заменяем текст и кнопки)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Отлично! Тогда начнем!\n\nНажми на кнопку, чтобы открыть викторину:",
        reply_markup=markup
    )

# ============================================
# ЗАПУСК БОТА
# ============================================
logging.info("Бот запущен и готов к работе!")

bot.polling(none_stop=True)

