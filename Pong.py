async def pinx(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pinx!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 pinx!!!\n`{ms}` 𝗺𝘀")
