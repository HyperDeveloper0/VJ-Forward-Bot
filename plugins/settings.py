# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio 
from database import Db, db
from script import Script
from pyrogram import Client, filters
from .test import get_configs, update_configs, CLIENT, parse_buttons
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .db import connect_user_db

CLIENT = CLIENT()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

@Client.on_message(filters.command('settings'))
async def settings(client, message):
   await message.reply_text(
     "<b>Hᴇʀᴇ Is Tʜᴇ Sᴇᴛᴛɪɴɢs Pᴀɴᴇʟ⚙\n\nᴄʜᴀɴɢᴇ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ 👇</b>",
     reply_markup=main_buttons()
     )

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

@Client.on_callback_query(filters.regex(r'^settings'))
async def settings_query(bot, query):
  user_id = query.from_user.id
  i, type = query.data.split("#")
  buttons = [[InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data="settings#main")]]
  if type=="main":
     await query.message.edit_text(
       "<b>Hᴇʀᴇ Is Tʜᴇ Sᴇᴛᴛɪɴɢs Pᴀɴᴇʟ⚙\n\nᴄʜᴀɴɢᴇ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ 👇</b>",
       reply_markup=main_buttons())
  elif type=="extra":
       await query.message.edit_text(
         "<b>Hᴇʀᴇ Is Tʜᴇ Exᴛʀᴀ Sᴇᴛᴛɪɴɢs Pᴀɴᴇʟ⚙</b>",
         reply_markup=extra_buttons())
  elif type=="bots":
     buttons = [] 
     _bot = await db.get_bot(user_id)
     usr_bot = await db.get_userbot(user_id)
     if _bot is not None:
        buttons.append([InlineKeyboardButton(_bot['name'],
                         callback_data=f"settings#editbot")])
     else:
        buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ʙᴏᴛ ✚', 
                         callback_data="settings#addbot")])
     if usr_bot is not None:
        buttons.append([InlineKeyboardButton(usr_bot['name'],
                         callback_data=f"settings#edituserbot")])
     else:
        buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ᴜsᴇʀ ʙᴏᴛ ✚', 
                         callback_data="settings#adduserbot")])
     buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#main")])
     await query.message.edit_text(
       "<b><u>My Bots</b></u>\n\n<b>ʏᴏᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʙᴏᴛs ɪɴ ʜᴇʀᴇ</b>",
       reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addbot":
     await query.message.delete()
     bot = await CLIENT.add_bot(bot, query)
     if bot != True: return
     await query.message.reply_text(
        "<b>bot token successfully added to db</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="adduserbot":
     await query.message.delete()
     user = await CLIENT.add_session(bot, query)
     if user != True: return
     await query.message.reply_text(
        "<b>session successfully added to db</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="channels":
     buttons = []
     channels = await db.get_user_channels(user_id)
     for channel in channels:
        buttons.append([InlineKeyboardButton(f"{channel['title']}",
                         callback_data=f"settings#editchannels_{channel['chat_id']}")])
     buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ᴄʜᴀɴɴᴇʟ ✚', 
                      callback_data="settings#addchannel")])
     buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#main")])
     await query.message.edit_text( 
       "<b><u>Mʏ Cʜᴀɴɴᴇʟs</b></u>\n\n<b>ʏᴏᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛꜱ ɪɴ ʜᴇʀᴇ</b>",
       reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addchannel":  
     await query.message.delete()
     chat_ids = await bot.ask(chat_id=query.from_user.id, text="<b>❪ SET TARGET CHAT ❫\n\nꜰᴏʀᴡᴀʀᴅ ᴀ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ\n/cancel - cancel this process</b>")
     if chat_ids.text=="/cancel":
        return await chat_ids.reply_text(
                  "<b>process canceled</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
     elif not chat_ids.forward_date:
        return await chat_ids.reply("**Tʜɪs ɪs ɴᴏᴛ ᴀ ꜰᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ⚠️**")
     else:
        chat_id = chat_ids.forward_from_chat.id
        title = chat_ids.forward_from_chat.title
        username = chat_ids.forward_from_chat.username
        username = "@" + username if username else "private"
     chat = await db.add_channel(user_id, chat_id, title, username)
     await query.message.reply_text(
        "<b>Successfully updated</b>" if chat else "<b>Tʜɪs ᴄʜᴀɴɴᴇʟ ᴀʟʀᴇᴀᴅʏ ᴀᴅᴅᴇᴅ</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="editbot": 
     bot = await db.get_bot(user_id)
     TEXT = Script.BOT_DETAILS if bot['is_bot'] else Script.USER_DETAILS
     buttons = [[InlineKeyboardButton('❌ ʀᴇᴍᴏᴠᴇ ❌', callback_data=f"settings#removebot")
               ],
               [InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data="settings#bots")]]
     await query.message.edit_text(
        TEXT.format(bot['name'], bot['id'], bot['username']),
        reply_markup=InlineKeyboardMarkup(buttons))
     
  elif type=="edituserbot": 
     bot = await db.get_userbot(user_id)
     TEXT = Script.USER_DETAILS
     buttons = [[InlineKeyboardButton('❌ ʀᴇᴍᴏᴠᴇ ❌', callback_data=f"settings#removeuserbot")
               ],
               [InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data="settings#bots")]]
     await query.message.edit_text(
        TEXT.format(bot['name'], bot['id'], bot['username']),
        reply_markup=InlineKeyboardMarkup(buttons))
     
  elif type=="removebot":
     await db.remove_bot(user_id)
     await query.message.edit_text(
        "<b>successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))
     
  elif type=="removeuserbot":
     await db.remove_userbot(user_id)
     await query.message.edit_text(
        "<b>successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))
     
  elif type.startswith("editchannels"): 
     chat_id = type.split('_')[1]
     chat = await db.get_channel_details(user_id, chat_id)
     buttons = [[InlineKeyboardButton('❌ ʀᴇᴍᴏᴠᴇ ❌', callback_data=f"settings#removechannel_{chat_id}")
               ],
               [InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data="settings#channels")]]
     await query.message.edit_text(
        f"<b><u>📄 Cʜᴀɴɴᴇʟ Dᴇᴛᴀɪʟs</b></u>\n\n<b>- Tɪᴛʟᴇ:</b> <code>{chat['title']}</code>\n<b>- Cʜᴀɴɴᴇʟ ID: </b> <code>{chat['chat_id']}</code>\n<b>- Usᴇʀɴᴀᴍᴇ :</b> {chat['username']}",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type.startswith("removechannel"):
     chat_id = type.split('_')[1]
     await db.remove_channel(user_id, chat_id)
     await query.message.edit_text(
        "<b>successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="caption":
     buttons = []
     data = await get_configs(user_id)
     caption = data['caption']
     if caption is None:
        buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ᴄᴀᴘᴛɪᴏɴ ✚', 
                      callback_data="settings#addcaption")])
     else:
        buttons.append([InlineKeyboardButton('👀 sᴇᴇ ᴄᴀᴘᴛɪᴏɴ 👀', 
                      callback_data="settings#seecaption")])
        buttons[-1].append(InlineKeyboardButton('🗑️ ᴅᴇʟᴇᴛᴇ ᴄᴀᴘᴛɪᴏɴ 🗑️', 
                      callback_data="settings#deletecaption"))
     buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#main")])
     await query.message.edit_text(
        "<b><u>Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</b></u>\n\n<b>ʏᴏᴜ ᴄᴀɴ sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴠɪᴅᴇᴏꜱ ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛs. ɴᴏʀᴍᴀʟʟʏ ᴜꜱᴇ ɪᴛꜱ ᴅᴇꜰᴀᴜʟᴛ ᴄᴀᴘᴛɪᴏɴ.</b>\n\n<b><u>Aᴠᴀɪʟᴀʙʟᴇ Fɪʟʟɪɴɢs:</b></u>\n- <code>{filename}</code> : Fɪʟᴇ ɴᴀᴍᴇ \n- <code>{size}</code> : Fɪʟᴇ sɪᴢᴇ\n- <code>{caption}</code> : Dᴇꜰᴀᴜʟᴛ ᴄᴀᴘᴛɪᴏɴ",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="seecaption":   
     data = await get_configs(user_id)
     buttons = [[InlineKeyboardButton('🖋️ Eᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ', 
                  callback_data="settings#addcaption")
               ],[
               InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                 callback_data="settings#caption")]]
     await query.message.edit_text(
        f"<b><u>Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</b></u>\n\n<code>{data['caption']}</code>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="deletecaption":
     await update_configs(user_id, 'caption', None)
     await query.message.edit_text(
        "<b>successfully updated</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addcaption":
     await query.message.delete()
     caption = await bot.ask(query.message.chat.id, "sᴇɴᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ\n/cancel - <code>ᴄᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</code>")
     if caption.text=="/cancel":
        return await caption.reply_text(
                  "<b>process canceled !</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
     try:
         caption.text.format(filename='', size='', caption='')
     except KeyError as e:
         return await caption.reply_text(
            f"<b>ᴡʀᴏɴɢ ꜰɪʟʟɪɴɢ {e} ᴜsᴇᴅ ɪɴ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ. ᴄʜᴀɴɢᴇ ɪᴛ</b>",
            reply_markup=InlineKeyboardMarkup(buttons))
     await update_configs(user_id, 'caption', caption.text)
     await caption.reply_text(
        "<b>sᴜᴄᴄᴇsꜰᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ✅</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="button":
     buttons = []
     button = (await get_configs(user_id))['button']
     if button is None:
        buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ʙᴜᴛᴛᴏɴ ✚', 
                      callback_data="settings#addbutton")])
     else:
        buttons.append([InlineKeyboardButton('👀 sᴇᴇ ʙᴜᴛᴛᴏɴ 👀', 
                      callback_data="settings#seebutton")])
        buttons[-1].append(InlineKeyboardButton('🗑️ ʀᴇᴍᴏᴠᴇ ʙᴜᴛᴛᴏɴ 🗑️', 
                      callback_data="settings#deletebutton"))
     buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#main")])
     await query.message.edit_text(
        "<b><u>CUSTOM BUTTON</b></u>\n\n<b>ʏᴏᴜ ᴄᴀɴ sᴇᴛ ᴀɴ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇꜱ.</b>\n\n<b><u>FORMAT:</b></u>\n`[Forward bot][buttonurl:https://t.me/mychannelurl]`\n",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addbutton":
     await query.message.delete()
     ask = await bot.ask(user_id, text="**Sᴇɴᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ʙᴜᴛᴛᴏɴ.\n\nFORMAT:**\n`[forward bot][buttonurl:https://t.me/url]`\n")
     button = parse_buttons(ask.text.html)
     if not button:
        return await ask.reply("**INVALID BUTTON**")
     await update_configs(user_id, 'button', ask.text.html)
     await ask.reply("**sᴜᴄᴄᴇssғʟꜰᴜʟʟʏ ʙᴜᴛᴛᴏɴ ᴀᴅᴅᴇᴅ ✅**",
             reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="seebutton":
      button = (await get_configs(user_id))['button']
      button = parse_buttons(button, markup=False)
      button.append([InlineKeyboardButton("• ʙᴀᴄᴋ •", "settings#button")])
      await query.message.edit_text(
         "**Yᴏᴜʀ Cᴜsᴛᴏᴍ Bᴜᴛᴛᴏɴ**",
         reply_markup=InlineKeyboardMarkup(button))

  elif type=="deletebutton":
     await update_configs(user_id, 'button', None)
     await query.message.edit_text(
        "**sᴜᴄᴄᴇssꜰᴜʟʟʏ ʙᴜᴛᴛᴏɴ ᴅᴇʟᴇᴛᴇᴅ ✅**",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="database":
     buttons = []
     db_uri = (await get_configs(user_id))['db_uri']
     if db_uri is None:
        buttons.append([InlineKeyboardButton('✚ ᴀᴅᴅ ᴍᴏɴɢᴏ ᴅʙ ᴜʀʟ ✚', 
                      callback_data="settings#addurl")])
     else:
        buttons.append([InlineKeyboardButton('👀 sᴇᴇ ᴜʀʟ', 
                      callback_data="settings#seeurl")])
        buttons[-1].append(InlineKeyboardButton('❌ ʀᴇᴍᴏᴠᴇ ᴜʀʟ ❌', 
                      callback_data="settings#deleteurl"))
     buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#main")])
     await query.message.edit_text(
        "<b><u>Dᴀᴛᴀʙsᴇ</u>\n\nᴅᴀᴛᴀʙᴀꜱᴇ ɪꜱ ʀᴇǫᴜɪʀᴇᴅ ꜰᴏʀ ꜱᴛᴏʀɪɴɢ ʏᴏᴜʀ ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ. ᴏᴛʜᴇʀᴡɪꜱᴇ, ꜱᴛᴏʀᴇᴅ ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇᴅɪᴀ ᴍᴀʏ ᴅɪꜱᴀᴘᴘᴇᴀʀ ᴀꜰᴛᴇʀ ᴀ ʙᴏᴛ ʀᴇꜱᴛᴀʀᴛ.</b>",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="addurl":
     await query.message.delete()
     uri = await bot.ask(user_id, "<b>ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴍᴏɴɢᴏ ᴅʙ ᴜʀʟ.</b>\n\n<i>ɢᴇᴛ ʏᴏᴜʀ ᴜʀʟ ꜰʀᴏᴍ MangoDb](https://mongodb.com)</i>", disable_web_page_preview=True)
     if uri.text=="/cancel":
        return await uri.reply_text(
                  "<b>process canceled !</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
     if not uri.text.startswith("mongodb+srv://") and not uri.text.endswith("majority"):
        return await uri.reply("<b>⚠️ Iɴᴠᴀʟɪᴅ MᴏɴɢᴏDB Uʀʟ ⚠️</b>",
                   reply_markup=InlineKeyboardMarkup(buttons))
     connect, udb = await connect_user_db(user_id, uri.text, "test")
     if connect:
        await udb.drop_all()
        await udb.close()
     else:
        return await uri.reply("<b>⚠️ Iɴᴠᴀʟɪᴅ MᴏɴɢᴏDB ᴜʀʟ, ᴄᴀɴ'ᴛ ᴄᴏɴɴᴇᴄᴛ ᴡɪᴛʜ ᴛʜɪs ᴜʀʟ ⚠️</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
     await update_configs(user_id, 'db_uri', uri.text)
     await uri.reply("**sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴅᴀᴛᴀʙᴀsᴇ ᴜʀʟ ᴀᴅᴅᴇᴅ ✅**",
             reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="seeurl":
     db_uri = (await get_configs(user_id))['db_uri']
     await query.answer(f"DATABASE URL: {db_uri}", show_alert=True)

  elif type=="deleteurl":
     await update_configs(user_id, 'db_uri', None)
     await query.message.edit_text(
        "**sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴅᴀᴛᴀʙᴀsᴇ ᴜʀʟ ᴅᴇʟᴇᴛᴇᴅ ✅**",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type=="filters":
     await query.message.edit_text(
        "<b><u>💠 Cᴜsᴛᴏᴍ Fɪʟᴛᴇʀs 💠</b></u>\n\n**ᴄᴏɴꜰɪɢᴜʀᴇ ᴛʜᴇ ᴛʏᴘᴇ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ**",
        reply_markup=await filters_buttons(user_id))

  elif type=="nextfilters":
     await query.edit_message_reply_markup( 
        reply_markup=await next_filters_buttons(user_id))

  elif type.startswith("updatefilter"):
     i, key, value = type.split('-')
     if value=="True":
        await update_configs(user_id, key, False)
     else:
        await update_configs(user_id, key, True)
     if key in ['poll', 'protect', 'voice', 'animation', 'sticker', 'duplicate']:
        return await query.edit_message_reply_markup(
           reply_markup=await next_filters_buttons(user_id)) 
     await query.edit_message_reply_markup(
        reply_markup=await filters_buttons(user_id))

  elif type.startswith("file_size"):
    settings = await get_configs(user_id)
    size = settings.get('min_size', 0)
    await query.message.edit_text(
       f'<b><u>SIZE LIMIT</b></u><b>\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ꜰɪʟᴇ ᴍᴀxɪᴍᴜᴍ sɪᴢᴇ ʟɪᴍɪᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ\n\nꜰɪʟᴇs ᴡɪᴛʜ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ `{size} MB` will forward</b>',
       reply_markup=size_button(size))
     
  elif type.startswith("maxfile_size"):
    settings = await get_configs(user_id)
    size = settings.get('max_size', 0)
    await query.message.edit_text(
       f'<b><u>Max SIZE LIMIT</b></u><b>\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ꜰɪʟᴇ ᴍᴀxɪᴍᴜᴍ sɪᴢᴇ ʟɪᴍɪᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ\n\nꜰɪʟᴇꜱ ᴡɪᴛʜ ʟᴇss ᴛʜᴀɴ `{size} MB` will forward</b>',
       reply_markup=maxsize_button(size))

  elif type.startswith("update_size"):
    size = int(query.data.split('-')[1])
    if 0 < size > 4000:
      return await query.answer("size limit exceeded", show_alert=True)
    await update_configs(user_id, 'min_size', size)
    i, limit = size_limit((await get_configs(user_id))['size_limit'])
    await query.message.edit_text(
       f'<b><u>SIZE LIMIT</b></u><b>\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ꜰɪʟᴇ ᴍᴀxɪᴍᴜᴍ sɪᴢᴇ ʟɪᴍɪᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ\n\nꜰɪʟᴇs ᴡɪᴛʜ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ {size} MB` will forward</b>',
       reply_markup=size_button(size))
     
  elif type.startswith("maxupdate_size"):
    size = int(query.data.split('-')[1])
    if 0 < size > 4000:
      return await query.answer("size limit exceeded", show_alert=True)
    await update_configs(user_id, 'max_size', size)
    i, limit = size_limit((await get_configs(user_id))['size_limit'])
    await query.message.edit_text(
       f'<b><u>Max SIZE LIMIT</b></u><b>\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ꜰɪʟᴇ ᴍᴀxɪᴍᴜᴍ sɪᴢᴇ ʟɪᴍɪᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ\n\nꜰɪʟᴇꜱ ᴡɪᴛʜ ʟᴇss ᴛʜᴀɴ `{size} MB` will forward</b>',
       reply_markup=maxsize_button(size))

  elif type.startswith('update_limit'):
    i, limit, size = type.split('-')
    limit, sts = size_limit(limit)
    await update_configs(user_id, 'size_limit', limit) 
    await query.message.edit_text(
       f'<b><u>SIZE LIMIT</b></u><b>\n\nʏᴏᴜ ᴄᴀɴ sᴇᴛ ғɪʟᴇ sɪᴢᴇ ʟɪᴍɪᴛ ᴛᴏ ꜰᴏʀᴡᴀʀᴅ\n\nSᴛᴀᴛᴜs: files with {sts} `{size} MB` will forward</b>',
       reply_markup=size_button(int(size)))

  elif type == "add_extension":
    await query.message.delete() 
    ext = await bot.ask(user_id, text="**ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴇxᴛᴇɴsɪᴏɴs (seperete by space)**")
    if ext.text == '/cancel':
       return await ext.reply_text(
                  "<b>process canceled</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
    extensions = ext.text.split(" ")
    extension = (await get_configs(user_id))['extension']
    if extension:
        for extn in extensions:
            extension.append(extn)
    else:
        extension = extensions
    await update_configs(user_id, 'extension', extension)
    buttons = []
    buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#get_extension")])
    await ext.reply_text(
        f"**successfully updated**",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type == "get_extension":
    extensions = (await get_configs(user_id))['extension']
    btn = []
    text = ""
    if extensions:
       text += "**🕹 Exᴛᴇɴsɪᴏɴs**"
       for ext in extensions:
          text += f"\n<code>-{ext}</code>"
    else:
       text += "**Nᴏ Exᴛᴇɴsɪᴏɴs Hᴇʀᴇ**"
    btn.append([InlineKeyboardButton('✚ ᴀᴅᴅ ✚', 'settings#add_extension')])
    btn.append([InlineKeyboardButton('🗑️ ʀᴇᴍᴏᴠᴇ ᴀʟʟ 🗑️', 'settings#rmve_all_extension')])
    btn.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 'settings#extra')])
    await query.message.edit_text(
        text=f"<b><u>ᴇ Exᴛᴇɴsɪᴏɴs</u></b>\n\n**ꜰɪʟᴇꜱ ᴡɪᴛʜ ᴛʜᴇꜱᴇ ᴇxᴛᴇɴꜱɪᴏɴꜱ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ꜰᴏʀᴡᴀʀᴅᴇᴅ.**\n\n{text}",
        reply_markup=InlineKeyboardMarkup(btn))

  elif type == "rmve_all_extension":
    await update_configs(user_id, 'extension', None)
    buttons = []
    buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#get_extension")])
    await query.message.edit_text(text="**sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ✅**",
                                   reply_markup=InlineKeyboardMarkup(buttons))
  elif type == "add_keyword":
    await query.message.delete()
    ask = await bot.ask(user_id, text="**ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ᴋᴇʏᴡᴏʀᴅs ʟɪᴋᴇ :- (English 1080p Hdrip)**")
    if ask.text == '/cancel':
       return await ask.reply_text(
                  "<b>process canceled</b>",
                  reply_markup=InlineKeyboardMarkup(buttons))
    keywords = ask.text.split(" ")
    keyword = (await get_configs(user_id))['keywords']
    if keyword:
        for word in keywords:
            keyword.append(word)
    else:
        keyword = keywords
    await update_configs(user_id, 'keywords', keyword)
    buttons = []
    buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#get_keyword")])
    await ask.reply_text(
        f"**successfully updated**",
        reply_markup=InlineKeyboardMarkup(buttons))

  elif type == "get_keyword":
    keywords = (await get_configs(user_id))['keywords']
    btn = []
    text = ""
    if keywords:
       text += "**🔖 Kᴇʏᴡᴏʀᴅs:**"
       for key in keywords:
          text += f"\n<code>-{key}</code>"
    else:
       text += "**ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴀᴅᴅ ᴀɴʏ ᴋᴇʏᴡᴏʀᴅꜱ.**"
    btn.append([InlineKeyboardButton('✚ ᴀᴅᴅ ✚', 'settings#add_keyword')])
    btn.append([InlineKeyboardButton('🗑️ ʀᴇᴍᴏᴠᴇ ᴀʟʟ 🗑️', 'settings#rmve_all_keyword')])
    btn.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 'settings#extra')])
    await query.message.edit_text(
        text=f"<b><u>Kᴇʏᴡᴏʀᴅs</u></b>ꜰɪʟᴇꜱ ᴡɪᴛʜ ᴛʜᴇsᴇ ᴋᴇʏᴡᴏʀᴅs ɪɴ ꜰɪʟᴇ ɴᴀᴍᴇ ᴏɴʟʏ ᴛᴏ ᴍᴇ ᴀʀᴇ ꜰᴏʀᴡᴀʀᴅᴇᴅ**\n\n{text}",
        reply_markup=InlineKeyboardMarkup(btn))

  elif type == "rmve_all_keyword":
    await update_configs(user_id, 'keywords', None)
    buttons = []
    buttons.append([InlineKeyboardButton('• ʙᴀᴄᴋ •', 
                      callback_data="settings#get_keyword")])
    await query.message.edit_text(text="**sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ᴋᴇʏᴡᴏʀᴅs ✅**",
                                   reply_markup=InlineKeyboardMarkup(buttons))
  elif type.startswith("alert"):
    alert = type.split('_')[1]
    await query.answer(alert, show_alert=True)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def extra_buttons():
   buttons = [[
       InlineKeyboardButton('💾 Mɪɴ Sɪᴢᴇ Lɪᴍɪᴛ',
                    callback_data=f'settings#file_size')
       ],[
       InlineKeyboardButton('💾 Mᴀx Sɪᴢᴇ Lɪᴍɪᴛ',
                    callback_data=f'settings#maxfile_size ')
       ],[
       InlineKeyboardButton('🚥 Kᴇʏᴡᴏʀᴅs',
                    callback_data=f'settings#get_keyword'),
       InlineKeyboardButton('🕹 Exᴛᴇɴsɪᴏɴs',
                    callback_data=f'settings#get_extension')
       ],[
       InlineKeyboardButton('⫷ Bᴀᴄᴋ',
                    callback_data=f'settings#main')
       ]]
   return InlineKeyboardMarkup(buttons)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def main_buttons():
  buttons = [[
       InlineKeyboardButton('🤖 Bᴏᴛs',
                    callback_data=f'settings#bots'),
       InlineKeyboardButton('🏷 Cʜᴀɴɴᴇʟs',
                    callback_data=f'settings#channels')
       ],[
       InlineKeyboardButton('🖋️ Cᴀᴘᴛɪᴏɴ',
                    callback_data=f'settings#caption'),
       InlineKeyboardButton('⏹ Bᴜᴛᴛᴏɴ',
                    callback_data=f'settings#button')
       ],[
       InlineKeyboardButton('🕵‍♀ Fɪʟᴛᴇʀs 🕵‍♀',
                    callback_data=f'settings#filters'),
       InlineKeyboardButton('🗃 MᴏɴɢᴏDB',
                    callback_data=f'settings#database')
       ],[
       InlineKeyboardButton('Exᴛʀᴀ Sᴇᴛᴛɪɴɢs 🧪',
                    callback_data=f'settings#extra')
       ],[
       InlineKeyboardButton('⫷ Bᴀᴄᴋ',
                    callback_data=f'help')
       ]]
  return InlineKeyboardMarkup(buttons)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def size_limit(limit):
   if str(limit) == "None":
      return None, ""
   elif str(limit) == "True":
      return True, "more than"
   else:
      return False, "less than"

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def extract_btn(datas):
    i = 0
    btn = []
    if datas:
       for data in datas:
         if i >= 3:
            i = 0
         if i == 0:
            btn.append([InlineKeyboardButton(data, f'settings#alert_{data}')])
            i += 1
            continue
         elif i > 0:
            btn[-1].append(InlineKeyboardButton(data, f'settings#alert_{data}'))
            i += 1
    return btn 

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def maxsize_button(size):
  buttons = [[
       InlineKeyboardButton('💾 Max Size Limit',
                    callback_data=f'noth')
       ],[
       InlineKeyboardButton('+1',
                    callback_data=f'settings#maxupdate_size-{size + 1}'),
       InlineKeyboardButton('-1',
                    callback_data=f'settings#maxupdate_size_-{size - 1}')
       ],[
       InlineKeyboardButton('+5',
                    callback_data=f'settings#maxupdate_size-{size + 5}'),
       InlineKeyboardButton('-5',
                    callback_data=f'settings#maxupdate_size_-{size - 5}')
       ],[
       InlineKeyboardButton('+10',
                    callback_data=f'settings#maxupdate_size-{size + 10}'),
       InlineKeyboardButton('-10',
                    callback_data=f'settings#maxupdate_size_-{size - 10}')
       ],[
       InlineKeyboardButton('+50',
                    callback_data=f'settings#maxupdate_size-{size + 50}'),
       InlineKeyboardButton('-50',
                    callback_data=f'settings#maxupdate_size_-{size - 50}')
       ],[
       InlineKeyboardButton('+100',
                    callback_data=f'settings#maxupdate_size-{size + 100}'),
       InlineKeyboardButton('-100',
                    callback_data=f'settings#maxupdate_size_-{size - 100}')
       ],[
       InlineKeyboardButton('• ʙᴀᴄᴋ •',
                    callback_data="settings#extra")
     ]]
  return InlineKeyboardMarkup(buttons)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

def size_button(size):
  buttons = [[
       InlineKeyboardButton('💾 Min Size Limit',
                    callback_data=f'noth')
       ],[
       InlineKeyboardButton('+1',
                    callback_data=f'settings#update_size-{size + 1}'),
       InlineKeyboardButton('-1',
                    callback_data=f'settings#update_size_-{size - 1}')
       ],[
       InlineKeyboardButton('+5',
                    callback_data=f'settings#update_size-{size + 5}'),
       InlineKeyboardButton('-5',
                    callback_data=f'settings#update_size_-{size - 5}')
       ],[
       InlineKeyboardButton('+10',
                    callback_data=f'settings#update_size-{size + 10}'),
       InlineKeyboardButton('-10',
                    callback_data=f'settings#update_size_-{size - 10}')
       ],[
       InlineKeyboardButton('+50',
                    callback_data=f'settings#update_size-{size + 50}'),
       InlineKeyboardButton('-50',
                    callback_data=f'settings#update_size_-{size - 50}')
       ],[
       InlineKeyboardButton('+100',
                    callback_data=f'settings#update_size-{size + 100}'),
       InlineKeyboardButton('-100',
                    callback_data=f'settings#update_size_-{size - 100}')
       ],[
       InlineKeyboardButton('• ʙᴀᴄᴋ •',
                    callback_data="settings#extra")
     ]]
  return InlineKeyboardMarkup(buttons)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

async def filters_buttons(user_id):
  filter = await get_configs(user_id)
  filters = filter['filters']
  buttons = [[
       InlineKeyboardButton('🏷️ Fᴏʀᴡᴀʀᴅ ᴛᴀɢ',
                    callback_data=f'settings_#updatefilter-forward_tag-{filter["forward_tag"]}'),
       InlineKeyboardButton('✅' if filter['forward_tag'] else '❌',
                    callback_data=f'settings#updatefilter-forward_tag-{filter["forward_tag"]}')
       ],[
       InlineKeyboardButton('🖍️ Tᴇxᴛs',
                    callback_data=f'settings_#updatefilter-text-{filters["text"]}'),
       InlineKeyboardButton('✅' if filters['text'] else '❌',
                    callback_data=f'settings#updatefilter-text-{filters["text"]}')
       ],[
       InlineKeyboardButton('📁 Dᴏᴄᴜᴍᴇɴᴛs',
                    callback_data=f'settings_#updatefilter-document-{filters["document"]}'),
       InlineKeyboardButton('✅' if filters['document'] else '❌',
                    callback_data=f'settings#updatefilter-document-{filters["document"]}')
       ],[
       InlineKeyboardButton('🎞️ Vɪᴅᴇᴏs',
                    callback_data=f'settings_#updatefilter-video-{filters["video"]}'),
       InlineKeyboardButton('✅' if filters['video'] else '❌',
                    callback_data=f'settings#updatefilter-video-{filters["video"]}')
       ],[
       InlineKeyboardButton('📷 Pʜᴏᴛᴏs',
                    callback_data=f'settings_#updatefilter-photo-{filters["photo"]}'),
       InlineKeyboardButton('✅' if filters['photo'] else '❌',
                    callback_data=f'settings#updatefilter-photo-{filters["photo"]}')
       ],[
       InlineKeyboardButton('🎧 Aᴜᴅɪᴏs',
                    callback_data=f'settings_#updatefilter-audio-{filters["audio"]}'),
       InlineKeyboardButton('✅' if filters['audio'] else '❌',
                    callback_data=f'settings#updatefilter-audio-{filters["audio"]}')
       ],[
       InlineKeyboardButton('⫷ ʙᴀᴄᴋ',
                    callback_data="settings#main"),
       InlineKeyboardButton('ɴᴇxᴛ ⫸',
                    callback_data="settings#nextfilters")
       ]]
  return InlineKeyboardMarkup(buttons) 

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

async def next_filters_buttons(user_id):
  filter = await get_configs(user_id)
  filters = filter['filters']
  buttons = [[
       ],[
       InlineKeyboardButton('🎤 Vᴏɪᴄᴇs',
                    callback_data=f'settings_#updatefilter-voice-{filters["voice"]}'),
       InlineKeyboardButton('✅' if filters['voice'] else '❌',
                    callback_data=f'settings#updatefilter-voice-{filters["voice"]}')
       ],[
       InlineKeyboardButton('🎭 Aɴɪᴍᴀᴛɪᴏɴs',
                    callback_data=f'settings_#updatefilter-animation-{filters["animation"]}'),
       InlineKeyboardButton('✅' if filters['animation'] else '❌',
                    callback_data=f'settings#updatefilter-animation-{filters["animation"]}')
       ],[
       InlineKeyboardButton('🃏 Sᴛɪᴄᴋᴇʀs',
                    callback_data=f'settings_#updatefilter-sticker-{filters["sticker"]}'),
       InlineKeyboardButton('✅' if filters['sticker'] else '❌',
                    callback_data=f'settings#updatefilter-sticker-{filters["sticker"]}')
       ],[
       InlineKeyboardButton('▶️ Sᴋɪᴘ ᴅᴜᴘʟɪᴄᴀᴛᴇ',
                    callback_data=f'settings_#updatefilter-duplicate-{filter["duplicate"]}'),
       InlineKeyboardButton('✅' if filter['duplicate'] else '❌',
                    callback_data=f'settings#updatefilter-duplicate-{filter["duplicate"]}')
       ],[
       InlineKeyboardButton('📊 Pᴏʟʟ',
                    callback_data=f'settings_#updatefilter-poll-{filters["poll"]}'),
       InlineKeyboardButton('✅' if filters['poll'] else '❌',
                    callback_data=f'settings#updatefilter-poll-{filters["poll"]}')
       ],[
       InlineKeyboardButton('🔒 Sᴇᴄᴜʀᴇ ᴍᴇssᴀɢᴇ',
                    callback_data=f'settings_#updatefilter-protect-{filter["protect"]}'),
       InlineKeyboardButton('✅' if filter['protect'] else '❌',
                    callback_data=f'settings#updatefilter-protect-{filter["protect"]}')
       ],[
       InlineKeyboardButton('⫷ ʙᴀᴄᴋ', 
                    callback_data="settings#filters"),
       InlineKeyboardButton('ʜᴏᴍᴇ 🏠',
                    callback_data="settings#main")
       ]]
  return InlineKeyboardMarkup(buttons) 

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
