

const TelegramBot = require('node-telegram-bot-api'); // подключаем node-telegram-bot-api

const token = '5215392084:AAHchct0SuP7c9dgSoPB8wV_3KEsYg1LpA8'; // тут токен кторый мы получили от botFather

// включаем самого обота
const bot = new TelegramBot(token, {polling: true});

// обработчик события присылания нам любого сообщения
bot.on('message', (msg) => {
  const chatId = msg.chat.id; //получаем идентификатор диалога, чтобы отвечать именно тому пользователю, который нам что-то прислал

  // отправляем сообщение
  //bot.sendMessage(chatId, 'Привет, Друг! чего хочешь?'
  bot.sendMessage(chatId, 'Test');
});

function sendMsg(msg)
{
  bot.sendMessage(chatId, msg);
}

