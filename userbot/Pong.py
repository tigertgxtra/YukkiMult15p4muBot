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
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10
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
import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          UploadProfilePhotoRequest)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from Yukki import *

@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pong"))

async def pinx(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pinx!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 pinx!!!\n`{ms}` 𝗺𝘀")
