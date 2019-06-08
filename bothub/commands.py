
import urllib.request
import simplejson as json

from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Find github users with /user username")

def user(update, context):
    req = urllib.request.urlopen("https://api.github.com/users/{}".format(context.args[0]))
    req = json.loads(req.read())
    context.bot.send_message(chat_id=update.message.chat_id, text=req['html_url'])

def inline_user(update, context):
    query = update.inline_query.query
    getString = "https://api.github.com/users/{}".format(query)
    print(getString)
    req = urllib.request.urlopen(getString)
    req = json.loads(req.read())

    results = list()
    results.append(
        InlineQueryResultArticle(
            id=req['id'],
            title=req['login'],
            input_message_content=InputTextMessageContent(req['html_url'])
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

HANDLERS = [
    CommandHandler('start', start),
    CommandHandler('user', user),
    InlineQueryHandler(inline_user)
]