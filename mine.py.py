#import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

# توکن ربات را اینجا جایگذاری کنید
TOKEN = "7187032756:AAFB05e5mez9oz2UbAssDN6mC6ZPj2UM3UU"
ADMIN_ID = "1848591768"  # آیدی ادمین خود را اینجا وارد کنید

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# لینک مینی اپ (لینک صفحه HTML مینی اپ)
WEB_APP_URL = "https://miniapp-olive.vercel.app"

# راه‌اندازی logging
#logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
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

    # فقط دکمه "مشاهده اطلاعات من"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔹 مشاهده اطلاعات من", web_app=WebAppInfo(url=WEB_APP_URL))
    )

    # ارسال پیام خوشامدگویی همراه با دکمه
    await message.answer(
        "👋 سلام! خوش آمدید.\nبرای مشاهده اطلاعات من روی دکمه زیر کلیک کنید:",
        reply_markup=keyboard
    )

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    # ارسال دستورالعمل‌ها برای کاربر
    help_text = """
    📝 **راهنمای ربات:**
    1. برای مشاهده اطلاعات من روی دکمه "مشاهده اطلاعات من" کلیک کنید.

    اگر سوالی دارید، همینجا بپرسید!
    """
    await message.answer(help_text)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def handle_location(message: types.Message):
    # پردازش موقعیت مکانی
    location = message.location
    await message.answer(f"📍 موقعیت شما: طول: {location.longitude}, عرض: {location.latitude}")

async def main():
    # شروع به کار ربات
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
