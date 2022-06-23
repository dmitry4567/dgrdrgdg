from aiogram import Bot, Dispatcher, executor, types
import logic

API_TOKEN = "5377723913:AAEiMadPE1RoWW10wWvr43gKWDXuCTgNWAg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text.startswith('/dl'))
async def editTaskOk(message: types.Message):
    logic.delTaskAll()
    await message.answer("Все задания удалены")

@dp.message_handler(lambda message: message.text.startswith('/del'))
async def delTaskOk(message: types.Message):
    row_id = int(message.text[4:])
    logic.delTask(row_id)
    await message.answer("Задание удалено")


@dp.message_handler(lambda message: message.text.startswith('/edit'))
async def editTaskOk(message: types.Message):
    row_id = int(message.text[5:])
    logic.editTaskOk(row_id)
    await message.answer("Изменил статус")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Бот to do list\n\n"
        "Для того чтобы добавить задание напишите любой текст\n\n"
        )


@dp.message_handler(commands=['tasks'])
async def get_Tasks(message: types.Message):
    tasks = logic.getTasks()
    if not tasks:
        await message.answer("Заданий нет")
        return

    text = []
    for task in tasks:
        if task.ok == 1:
            f = '✅'
        else:
            f = '❌'
        text.append(f"{f} {task.text} /edit{task.id} /del{task.id}")
    answer_message = "Задачи:\n\n" + "\n\n" \
        .join(text)
    await message.answer(answer_message)


@dp.message_handler()
async def add_Task(message: types.Message):
    try:
        logic.add_Task(message.text)
    except:
        pass
    await message.answer("Задача добавлена")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)