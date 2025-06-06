import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from assistant_task2 import Assistant

TOKEN = "7510157585:AAFTzQfmtmCcF8fhwsqW-Lu-PqfQn8RKe_4"
assistant = Assistant()

class Form(StatesGroup):
    adding = State()
    searching = State()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привіт! Команди: /add /list /search")

@dp.message(F.text == "/add")
async def add_note(message: Message, state: FSMContext):
    await state.set_state(Form.adding)
    await message.answer("Введи нотатку:")

@dp.message(F.text == "/search")
async def search_note(message: Message, state: FSMContext):
    await state.set_state(Form.searching)
    await message.answer("Введи ключове слово:")

@dp.message(F.text == "/list")
async def list_notes(message: Message):
    notes = assistant.list_notes()
    await message.answer("\n".join(notes) if notes else "Нотаток немає.")

@dp.message(Form.adding)
async def process_add_note(message: Message, state: FSMContext):
    assistant.add_note(message.text)
    await message.answer("Нотатку додано.")
    await state.clear()

@dp.message(Form.searching)
async def process_search(message: Message, state: FSMContext):
    results = assistant.search_notes(message.text)
    await message.answer("\n".join(results) if results else "Збігів немає.")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
