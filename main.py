from aiogram import types, Dispatcher, F, filters, Bot
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="7209918809:AAH7l5dregYjP4r8mTDQikb6x9V952cyQro")
dp = Dispatcher(bot=bot)

inline_keyboards = [
    [InlineKeyboardButton(text="Menu", callback_data="menu"),
     InlineKeyboardButton(text="Basket",callback_data="basket"),
     InlineKeyboardButton(text="About us", url="https://evos.uz/")]
]
main_button = InlineKeyboardMarkup(inline_keyboard=inline_keyboards)


products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Lavash", callback_data="lavash"), InlineKeyboardButton(text="Hamburger", callback_data="hamburger"), InlineKeyboardButton(text="Hot-Dog", callback_data="hotdog")]
])

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buy", callback_data="yes"), InlineKeyboardButton(text="Cancel", callback_data="no")]
])

basket=[]

@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer("Xush kelibsiz", reply_markup=main_button)

@dp.callback_query(F.data == "menu")
async def hotdog(call: types.CallbackQuery):
    await call.message.answer("Qaysi birini tanlisiz?", reply_markup=products)

@dp.callback_query(F.data=="lavash")
async def lavash(call: types.CallbackQuery):
    photo = "https://anhor.uz/wp-content/uploads/2023/12/side_view_chicken_roll_grilled_chicken_lettuce_cucumber_tomato_mayo_pita_1200x675.jpg"
    caption = "Lavash 30.000 som"
    await call.message.answer_photo(photo=photo, caption=caption, reply_markup=yes_or_no)

@dp.callback_query(F.data=="hamburger")
async def hamburger(call: types.CallbackQuery):
    photo = "https://media.cnn.com/api/v1/images/stellar/prod/220428140436-04-classic-american-hamburgers.jpg?c=original"
    caption = "Hamburger 35.000 som"
    await call.message.answer_photo(photo=photo, caption=caption, reply_markup=yes_or_no)

@dp.callback_query(F.data=="hotdog")
async def hotdog(call: types.CallbackQuery):
    photo = "https://img.freepik.com/free-photo/classic-hot-dog-with-ketchup-and-mustard-sauce-isolated-on-white-background_123827-29747.jpg"
    caption = "Hot-Dog 35.000 som"
    await call.message.answer_photo(photo=photo, caption=caption, reply_markup=yes_or_no)

@dp.callback_query(F.data=="yes")
async def yes(call:types.CallbackQuery):
    await call.message.answer("We added it to basket")

@dp.callback_query(F.data=="no")
async def no(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer()
async def mainpy():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(mainpy())
