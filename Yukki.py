# v3.1.1.11 beta1

import os
import sys
import asyncio
import csv
import random
from asyncio import sleep
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserPrivacyRestrictedError,
    UserNotMutualContactError
)
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO,TMP_DOWNLOAD_DIRECTORY, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10
import asyncio
import telethon.utils
from telethon.tl.types import InputPeerUser, ChatBannedRights
from telethon.tl.functions.channels import (
    InviteToChannelRequest,
    EditBannedRequest,
    GetFullChannelRequest,
    LeaveChannelRequest)
from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from Utils import RAID, RRAID
from Pong import *
import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError

from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)

from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)

from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import time

# TMP_DOWNLOAD_DIRECTORY = "resources/downloads/"



a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk


    print("bot v3.1.1.11 beta1 is starting...")
    print("")
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await idk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await ydk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await wdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await hdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await sdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await adk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await bdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await cdk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await ddk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@CariTemanLink"))
            await edk(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 

loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
# =============[BATAS]=============



@idk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.getmemb"))

# @register(outgoing=True, pattern=r"^\.getmemb$")
async def scrapmem(event):
    if event.sender_id in SMEX_USERS:
        # text = "`Mohon tunggu...`"
        chat = event.chat_id
        y = await event.reply("`Mohon tunggu...`" )
        client = event.client
        members = await client.get_participants(chat, aggressive=True)

        with open("members.csv", "w", encoding="UTF-8") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(["user_id", "hash"])
            for member in members:
                writer.writerow([member.id, member.access_hash])
        await y.edit(f"`Berhasil Mengumpulkan Member..`")




@idk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.addmemb"))
# @register(outgoing=True, pattern=r"^\.addmemb$")

async def admem(event):
    if event.sender_id in SMEX_USERS:
        # text = "`Proses Menambahkan 0 Member...`"
        x = await event.reply("`Proses Menambahkan 0 Member...`")
        chat = await event.get_chat()
        client = event.client
        users = []
        with open("members.csv", encoding="UTF-8") as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {'id': int(row[0]), 'hash': int(row[1])}
                users.append(user)
        n = 0
        for user in users:
            n += 1
            if n % 10 == 0:
                await x.edit(f"`Mencapai 10 anggota, tunggu selama {900/60} menit`")
                await asyncio.sleep(900)
            try:
                userin = InputPeerUser(user['id'], user['hash'])
                await event.client(InviteToChannelRequest(chat, [userin]))
                await asyncio.sleep(random.randrange(5, 7))
                await x.edit(f"`Prosess Menambahkan {n} Member...`")
            except TypeError:
                n -= 1
                continue
            except UserAlreadyParticipantError:
                n -= 1
                continue
            except UserPrivacyRestrictedError:
                n -= 1
                continue
            except UserNotMutualContactError:
                n -= 1
                continue

# =============[BATAS]=============
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.eplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 𝗣𝗼𝗻𝗴!\n`{ms}` 𝗺𝘀")

# ======PONG


# ======PURGEME


@idk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.purgeme"))

async def purgeme(delme):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝙋𝙪𝙧𝙜𝙚𝙢𝙚\n\nCommand:\n\n.purgeme <count> | delete x count of your latest message."
    if delme.sender_id in SMEX_USERS:
        """ For .purgeme, delete x count of your latest message."""
        message = delme.text
        count = int(message[9:])
        i = 1

        async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
            if i > count + 1:
                break
            i = i + 1
            await message.delete()

        smsg = await delme.client.send_message(
            delme.chat_id,
            "`Purge complete!` Purged " + str(count) + " messages.",
        )
        """
        if BOTLOG:
            await delme.client.send_message(
                BOTLOG_CHATID,
                "#PURGEME \nPurge of " + str(count) + " messages done successfully.")
        """
        await sleep(2)
        i = 1
        await smsg.delete()
        

# ====================== CONSTANT ===============================
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "```Profile picture changed successfully.```"
PP_TOO_SMOL = "```This image is too small, use a bigger image.```"
PP_ERROR = "```Failure occured while processing image.```"

BIO_SUCCESS = "```Successfully edited Bio.```"

NAME_OK = "```Your name was succesfully changed.```"
USERNAME_SUCCESS = "```Your username was succesfully changed.```"
USERNAME_TAKEN = "```This username is already taken.```"
# ===============================================================

# ==== SET PHOTO PROFIL

@idk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setpfp$"))

# @bot.on(geezbot_cmd(outgoing=True, pattern="setpfp$"))
async def set_profilepic(propic):
    if propic.sender_id in SMEX_USERS:    
        """ For .profilepic command, change your profile picture in Telegram. """
        replymsg = await propic.get_reply_message()
        photo = None
        if replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await propic.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split('/'):
                photo = await propic.client.download_file(replymsg.media.document)
            else:
                await propic.reply(INVALID_MEDIA)

        if photo:
            try:
                await propic.client(
                    UploadProfilePhotoRequest(await
                                              propic.client.upload_file(photo)))
                os.remove(photo)
                await propic.reply(PP_CHANGED)
            except PhotoCropSizeSmallError:
                await propic.reply(PP_TOO_SMOL)
            except ImageProcessFailedError:
                await propic.reply(PP_ERROR)
            except PhotoExtInvalidError:
                await propic.reply(INVALID_MEDIA)


# ==== DELETE PHOTO PROFIL


@idk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"^\.delpfp ?(.*)"))


# credit to geez, ultroid

# @bot.on(geezbot_cmd(outgoing=True, pattern=r"delpfp"))
async def remove_profilepic(delpfp):
    if delpfp.sender_id in SMEX_USERS:
        """ For .delpfp command, delete your current profile picture in Telegram. """
        ok = await delpfp.reply("...")
        group = delpfp.text[8:]
        if group == 'all':
            lim = 0
        elif group.isdigit():
            lim = int(group)
        else:
            lim = 1

        pfplist = await delpfp.client.get_profile_photos("me", limit=lim)

        await delpfp.client(DeletePhotosRequest(pfplist))
        await ok.edit(
            f"`Successfully deleted {len(pfplist)} profile picture(s).`")



# ==== SET USERNAME

@idk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.username (.*)"))


# @bot.on(geezbot_cmd(outgoing=True, pattern="username (.*)"))
async def update_username(username):
    if username.sender_id in SMEX_USERS:
        """ For .username command, set a new username in Telegram. """
        newusername = username.pattern_match.group(1)
        try:
            await username.client(UpdateUsernameRequest(newusername))
            await username.reply(USERNAME_SUCCESS)
        except UsernameOccupiedError:
            await username.reply(USERNAME_TAKEN)


# ==== COUNT CHATS

# STRINGS
STAT_INDICATION = "`Collecting stats, Please wait....`"

# Functions
def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"

@idk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"^\.stats$"))

# @register(outgoing=True, pattern=r"^\.stats$")
async def stats(event):
    if event.sender_id in SMEX_USERS:
        stat = await event.reply(STAT_INDICATION)
        start_time = time.time()
        private_chats = 0
        bots = 0
        groups = 0
        broadcast_channels = 0
        admin_in_groups = 0
        creator_in_groups = 0
        admin_in_broadcast_channels = 0
        creator_in_channels = 0
        unread_mentions = 0
        unread = 0
        dialog: Dialog
        async for dialog in event.client.iter_dialogs():
            entity = dialog.entity
            if isinstance(entity, Channel) and entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif (
                isinstance(entity, Channel)
                and entity.megagroup
                or not isinstance(entity, Channel)
                and not isinstance(entity, User)
                and isinstance(entity, Chat)
            ):
                groups += 1
                if entity.creator or entity.admin_rights:
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
            elif not isinstance(entity, Channel) and isinstance(entity, User):
                private_chats += 1
                if entity.bot:
                    bots += 1
            unread_mentions += dialog.unread_mentions_count
            unread += dialog.unread_count
        stop_time = time.time() - start_time
        full_name = inline_mention(await event.client.get_me())
        response = f"📊 **Stats for {full_name}** \n\n"
        response += f"**Private Chats:** {private_chats} \n"
        response += f"   • `Users: {private_chats - bots}` \n"
        response += f"   • `Bots: {bots}` \n"
        response += f"**Groups:** {groups} \n"
        response += f"**Channels:** {broadcast_channels} \n"
        response += f"**Admin in Groups:** {admin_in_groups} \n"
        response += f"   • `Creator: {creator_in_groups}` \n"
        response += f"   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n"
        response += f"**Admin in Channels:** {admin_in_broadcast_channels} \n"
        response += f"   • `Creator: {creator_in_channels}` \n"
        response += (
            f"   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n"
        )
        response += f"**Unread:** {unread} \n"
        response += f"**Unread Mentions:** {unread_mentions} \n\n"
        response += f"⏱ __It Took:__ {stop_time:.02f}s \n"
        await stat.edit(response)


########[VAR]########

ALIVE_NAME = "Alpha-XProject"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Alpha-X Userbot"

BIO_MSG = "Alpha-X Userbot | @AlphaXProject"
DEFAULTUSERBIO = str(BIO_MSG) if BIO_MSG else "Alpha-X Userbot | @AlphaXProject"
BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
BOTLOG = False


########[CLONE]########

@idk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.clone ?(.*)"))


# @ultroid_cmd(pattern="clone ?(.*)")
async def _(event):
    if event.sender_id in SMEX_USERS:
        if event.fwd_from:
            return
        reply_message = await event.get_reply_message()
        replied_user, error_i_a = await get_full_user(event)
        if replied_user is None:
            await event.edit(str(error_i_a))
            return False
        user_id = replied_user.user.id
        profile_pic = await event.client.download_profile_photo(
            user_id, Config.TMP_DOWNLOAD_DIRECTORY
        )
        # some people have weird HTML in their names
        first_name = html.escape(replied_user.user.first_name)
        # https://stackoverflow.com/a/5072031/4723940
        # some Deleted Accounts do not have first_name
        if first_name is not None:
            # some weird people (like me) have more than 4096 characters in their names
            first_name = first_name.replace("\u2060", "")
        last_name = replied_user.user.last_name
        # last_name is not Manadatory in @Telegram
        if last_name is not None:
            last_name = html.escape(last_name)
            last_name = last_name.replace("\u2060", "")
        if last_name is None:
            last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
        # inspired by https://telegram.dog/afsaI181
        user_bio = replied_user.about
        if user_bio is not None:
            user_bio = replied_user.about
        await borg(functions.account.UpdateProfileRequest(first_name=first_name))
        await borg(functions.account.UpdateProfileRequest(last_name=last_name))
        await borg(functions.account.UpdateProfileRequest(about=user_bio))
        pfile = await borg.upload_file(profile_pic)  # pylint:disable=E060
        await borg(
            functions.photos.UploadProfilePhotoRequest(pfile)  # pylint:disable=E0602
        )
        await event.delete()
        await borg.send_message(
            event.chat_id, "**Who Are You? .. **", reply_to=reply_message
        )
        """
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#CLONED\nSuccesfulley cloned [{first_name}](tg://user?id={user_id })",
            )
            """


########[REVERT]########

@idk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.revert$"))

# @ultroid_cmd(pattern="revert$")
# @borg.on(admin_cmd(pattern="revert$"))
async def _(event):
    if event.sender_id in SMEX_USERS:
        if event.fwd_from:
            return
        name = f"{DEFAULTUSER}"
        bio = f"{DEFAULTUSERBIO}"
        n = 1
        await borg(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=n)
            )
        )
        await borg(functions.account.UpdateProfileRequest(about=f"{bio}"))
        await borg(functions.account.UpdateProfileRequest(first_name=f"{name}"))
        await event.edit("succesfully reverted to your account back")
        """
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, f"#REVERT\nSuccesfully reverted back to your profile"
            )
        """    


async def get_full_user(event):
    if event.sender_id in SMEX_USERS:
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.forward:
                replied_user = await event.client(
                    GetFullUserRequest(
                        previous_message.forward.sender_id
                        or previous_message.forward.channel_id
                    )
                )
                return replied_user, None
            else:
                replied_user = await event.client(
                    GetFullUserRequest(previous_message.sender_id)
                )
                return replied_user, None
        else:
            input_str = None
            try:
                input_str = event.pattern_match.group(1)
            except IndexError as e:
                return None, e
            if event.message.entities:
                mention_entity = event.message.entities
                probable_user_mention_entity = mention_entity[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                else:
                    try:
                        user_object = await event.client.get_entity(input_str)
                        user_id = user_object.id
                        replied_user = await event.client(GetFullUserRequest(user_id))
                        return replied_user, None
                    except Exception as e:
                        return None, e
            elif event.is_private:
                try:
                    user_id = event.chat_id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
            else:
                try:
                    user_object = await event.client.get_entity(int(input_str))
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e



# ========[name changer]

@idk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.setname ?((.|//)*)"))

# @ultroid_cmd(pattern="setname ?((.|//)*)", fullsudo=True)

async def setname(event):
    if event.sender_id in SMEX_USERS:
        ok = await event.reply("...")
        names = event.pattern_match.group(1)
        first_name = names
        last_name = ""
        if "//" in names:
            first_name, last_name = names.split("//", 1)
        try:
            await event.client(
                UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name,
                ),
            )
            await ok.edit(f"Name changed to `{names}`")
        except Exception as ex:
            await ok.edit("Error occured.\n`{}`".format(str(ex)))



# ===== DM ========

@idk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dm(?: |$)(.*)"))

# @bot.on(geezbot_cmd(outgoing=True, pattern="dm(?: |$)(.*)"))
async def remoteaccess(event):
    if event.sender_id in SMEX_USERS:
        p = event.pattern_match.group(1)
        m = p.split(" ")

        chat_id = m[0]
        try:
            chat_id = int(chat_id)
        except BaseException:

            pass

        msg = ""
        mssg = await event.get_reply_message()
        if event.reply_to_msg_id:
            await event.client.send_message(chat_id, mssg)
            await event.reply("`Success Mengirim Pesan Anda.`")
        for i in m[1:]:
            msg += i + " "
        if msg == "":
            return
        try:
            await event.client.send_message(chat_id, msg)
            await event.reply("`Success Mengirim Pesan Anda.`")
        except BaseException:
            await event.reply("**Terjadi Error. Gagal Mengirim Pesan.**")


# restart         

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
           
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = """🔰 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

🛠 𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:
<code>.ping</code>
<code>.restart</code>

🎛 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:
<code>.bio</code>
<code>.join</code>
<code>.pjoin</code>
<code>.leave</code>
<code>.inviteall</code>

☠️ 𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:
<code>.spam</code>
<code>.delayspam</code>
<code>.bigspam</code>
<code>.raid</code>
<code>.replyraid</code>
<code>.dreplyraid</code>

⚔️ 𝙓𝙩𝙧𝙖 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:
<code>.purgeme</code>
<code>.rabsen</code>
<code>.setname</code>
<code>.getmemb</code>
<code>.addmemb</code>
<code>.dm</code>
<code>.setpfp</code>
<code>.delpfp</code>
<code>.username</code>
<code>.stats</code>

For more help regarding usage of plugins type plugins name

🤖 𝘽𝙤𝙩 𝙑𝙚𝙧𝙨𝙞𝙤𝙣\t: <code>v3.1.1.11 beta1</code>
🤖 𝘽𝙤𝙩 𝙏𝙮𝙥𝙚\t\t: <code>YKX</code>"""
       await e.reply(text, parse_mode='html', link_preview=None )

        

    
        
text = """
██╗░░░██╗██╗░░░██╗██╗░░██╗██╗░░██╗██╗
╚██╗░██╔╝██║░░░██║██║░██╔╝██║░██╔╝██║
░╚████╔╝░██║░░░██║█████═╝░█████═╝░██║
░░╚██╔╝░░██║░░░██║██╔═██╗░██╔═██╗░██║
░░░██║░░░╚██████╔╝██║░╚██╗██║░╚██╗██║
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝"""

print(text)
print("")
print("SMEX! Yukki Mult1 5p4mX UBot v3.1.1.11 beta1 Started Sucessfully.")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
