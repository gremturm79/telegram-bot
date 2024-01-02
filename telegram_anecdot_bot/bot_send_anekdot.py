from aiogram import Dispatcher, Bot, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
import logging
from LibeAnekdot import anecdot

TOKEN = '6110512466:AAGLXM2-C4XNzMu-VcDOPwmqYoX0DMGq_zE'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

id_list = set()


@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    id_list.add(user_id)
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {message.from_user.full_name}, анекдоты для вас')


async def send_message_time(bot: Bot):
    mix = anecdot.Anecdote.anec_mixed()
    sundry = anecdot.Anecdote.anec_sundry()
    nation = anecdot.Anecdote.anec_national()
    time.sleep(5)
    for i in id_list:
        await bot.send_message(i, f"\N{fire}\n{mix}")
        await bot.send_message(i, f"\N{fire}\n{sundry}")
        await bot.send_message(i, f"\N{fire}\n{nation}")


scheduler = AsyncIOScheduler(timezone='Europe/Kaliningrad')
scheduler.add_job(send_message_time, 'interval', hours=6, kwargs={'bot': bot})

scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
