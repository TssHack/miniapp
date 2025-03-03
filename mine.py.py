import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import F
import asyncio

# توکن ربات و آیدی ادمین
TOKEN = '7187032756:AAFB05e5mez9oz2UbAssDN6mC6ZPj2UM3UU'
ADMIN_ID = '1848591768'  # آیدی ادمین خود را اینجا وارد کنید

# لینک مینی اپ (لینک صفحه HTML مینی اپ)
WEB_APP_URL = 'https://miniapp-olive.vercel.app'

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

# ساخت ربات و دیسپچر
bot = Bot(token=TOKEN)
dp = Dispatcher()

# هنگام شروع ربات، پیام خوشامدگویی به همراه مشخصات کاربر به ادمین ارسال می‌شود
@dp.message(F.command("start"))
async def send_welcome(message: types.Message):
    # ارسال مشخصات کاربر به ادمین
    user_info = f"""
    📢 **کاربر جدید وارد ربات شد:**
    - نام: {message.from_user.full_name}
    - شناسه کاربری: @{message.from_user.username if message.from_user.username else "N/A"}
    - آیدی کاربر: {message.from_user.id}
    - زبان: {message.from_user.language_code}
    """
    await bot.send_message(ADMIN_ID, user_info)

    # ساخت دکمه "مشاهده اطلاعات من"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔹 مشاهده اطلاعات من", web_app=WebAppInfo(url=WEB_APP_URL))
    )

    # ارسال پیام خوشامدگویی همراه با دکمه
    await message.answer(
        "👋 سلام! خوش آمدید.\nبرای مشاهده اطلاعات من روی دکمه زیر کلیک کنید:",
        reply_markup=keyboard
    )

# دستور help
@dp.message(F.command("help"))
async def send_help(message: types.Message):
    help_text = """
    📝 **راهنمای ربات:**
    1. برای مشاهده اطلاعات من روی دکمه "مشاهده اطلاعات من" کلیک کنید.

    اگر سوالی دارید، همینجا بپرسید!
    """
    await message.answer(help_text)

# شروع به کار ربات
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
