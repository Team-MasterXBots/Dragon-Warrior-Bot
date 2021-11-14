# Voics Chatbot Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav
# @lyciachatbot support Now
import os

import aiofiles
import aiohttp
from pyrogram import filters

from Natsuki.services.pyrogram import pbot as Natsuki


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_lycia(url):
    ai_name = "DragonWarrior.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@Natsuki.on_message(filters.command("Dragon Warrior"))
async def Lycia(_, message):
    if len(message.command) < 2:
        await message.reply_text("DragonWarrior AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    lycia = text.replace(" ", "%20")
    m = await message.reply_text("DragonWarrior Is Best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=DragonWarrior&ownername=New-Dev3&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "DragonWarrior"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @madepranav...")
    LyciaVoice = await ai_lycia(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=LyciaVoice, title=chatbot, performer=name)
    os.remove(LyciaVoice)
    await m.delete()
