import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped, HighQualityAudio
from pyrogram.types import Message

# --- CONFIG ---
API_ID = 33603336  # Apna API ID dalo
API_HASH = "c9683a8ec3b886c18219f650fc8ed429" # Apna API Hash dalo
SESSION = "BQE-4i0ASxu8TXk4s870tFMn-D2Ijs-7DaTep8qcmRnZuowGYTiKDzzy9fKRT3pCc7aFI9oql0Rp5k1FkymDhRbewYPN11p5G7exMCs-z2bdMPuRoJCF60r7p_xq0TBjtLw5P1f-pXHHRxeXSAq0nKyNglv2pZ-GVCbYL4J-OwIkfck4wZyfiU0H58LZla5Il4VmVww-ewK3roa4mVjIxGKYoFva7LqYEf9Iti77jLz7HW7gCfuNessLDXqH1se4DuOSmoJzbacJxofENDQJChGjP4K7gbkMQQKwjCQfndvTmHLyDnc5jDqwfngZK1ogepmyiXZhhzHVebIieznK4DXTM1Q7pAAAAAHKarFXAA"
# --- Random image links ---" # Assistant ka String Session

app = Client("UkhiBot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
call = PyTgCalls(app)

# Default Power Level
UKHI_LEVEL = 10 

@app.on_message(filters.command("level"))
async def set_level(_, msg: Message):
    global UKHI_LEVEL
    if len(msg.command) < 2:
        return await msg.reply("❌ **Level do (1-20)!** Example: `/level 15`")
    
    UKHI_LEVEL = int(msg.command[1])
    await msg.reply(f"🔥 **Ukhi Power Set to:** `{UKHI_LEVEL}`")

@app.on_message(filters.command("boost_on"))
async def boost_on(_, msg: Message):
    chat_id = msg.chat.id
    
    # Ye hai asali Speaker-Crushing Filter 💀
    # bass=g={UKHI_LEVEL*2} -> Bhari Bass
    # volume={UKHI_LEVEL} -> Loudness
    # aecho -> Wo 'Goonjti' hui ukhi awaz
    filt = f"bass=g={UKHI_LEVEL*2},volume={UKHI_LEVEL},aecho=0.8:0.8:40:0.5"

    try:
        await call.join_group_call(
            chat_id,
            AudioPiped(
                "pulse", # VPS ka virtual sound driver
                HighQualityAudio(),
                options=f"-af {filt}" # Latest version logic
            )
        )
        await msg.reply(f"🎤 **UKHI BOOST ON!**\nLevel: `{UKHI_LEVEL}`\n*Assistant is now roaring...*")
    except Exception as e:
        await msg.reply(f"❌ **Error:** `{e}`\n*(Check if PulseAudio is running)*")

@app.on_message(filters.command("boost_off"))
async def boost_off(_, msg: Message):
    try:
        await call.leave_group_call(msg.chat.id)
        await msg.reply("🔇 **Boost OFF!** Assistant is quiet now.")
    except:
        pass

# Start the bot
print("🚀 UKHI BASS BOOST BOT IS ALIVE!")
app.start()
call.start()
import asyncio
asyncio.get_event_loop().run_forever()
