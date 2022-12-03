import telebot
from Tasks.Kirutsin.additional.script_src import select_user, create_user, login_validation, select_shoplist, \
    add_product, delete_product

# connect bot
TOKEN = "5631651495:AAG-fKHualc1SfKqrL17dl9Imj6bbkWrXXI"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# config db
path_db = 'test_bd'

# tables
table_name_db_users = 'users'
table_name_db_shop_info = 'shop_info'

# tables parameters
headers_users_login = 'login'
headers_users_password = 'password'

headers_shop_info_user = 'user'
headers_shop_info_product = 'product'
headers_shop_info_currency = 'currency'
headers_shop_info_price = 'price'


# secure info must be encoded
key = b'4234gfbvfgbf5t45t6'

# secret_hash = hmac.new(key=b'4234gfbvfgbf5t45t6', msg=b'231231', digestmod=hashlib.sha256, ).hexdigest()

# hello user
@bot.message_handler(commands=['start'])
def user_autorisation(message):
    bot.reply_to(message, "Hello!\nI'm a fin bot, type /login. For authorization. Or /register for new account")


# register
@bot.message_handler(commands=['register'])
def handle_register_help(message):
    bot.reply_to(message, "Provide your login and password. Example\nNew login:example, New password:example,")

    @bot.message_handler(regexp='New login')
    def register(message):
        # parse response
        login_user = message.text[message.text.find(":") + 1:message.text.find(",")]

        password_user = message.text[message.text.rfind(":") + 1:message.text.rfind(",")]

        check_login_history = select_user(path_db, headers_users_login, table_name_db_users, login_user)

        if not check_login_history:
            create_user(path_db, table_name_db_users, login_user, password_user, key)
            bot.reply_to(message, "Yours account, has been successfully created. Use /login")
        else:
            bot.reply_to(message, "I see this user, please use /login")


@bot.message_handler(commands=['login'])
def handle_login_help(message):
    bot.reply_to(message, "Provide your login and password. Example\nLogin:example, Password:example,")

    @bot.message_handler(regexp='Login')
    def login(message):
        # parse response
        login_user = message.text[message.text.find(":") + 1:message.text.find(",")]
        password_user = message.text[message.text.rfind(":") + 1:message.text.rfind(",")]

        login_result = login_validation(path_db, headers_users_password, table_name_db_users,
                                        headers_users_login, login_user, password_user, key)

        if login_result:
            bot.reply_to(message, f"Hello {login_user}! Available commands:\n"
                                  f"/shop_list == view you shop list\n"
                                  f"/add_product == add product(Example:/add_product|product|price|currency)\n"
                                  f"/delete_product == delete product(Example:/delete_product|id)")

            @bot.message_handler(regexp='/shop_list')
            def shop_list(message):
                bot.reply_to(message, select_shoplist(path_db, login_user))

            @bot.message_handler(regexp='/add_product')
            def shop_list(message):
                add_product(path_db, table_name_db_shop_info, message.text, login_user)
                bot.reply_to(message, "Done! Please check")

            @bot.message_handler(regexp='/delete_product')
            def shop_list(message):
                delete_product(path_db, table_name_db_shop_info, message.text)
                bot.reply_to(message, "Done! Please check")

        else:
            return bot.reply_to(message, "Check you login or password")


bot.infinity_polling()
