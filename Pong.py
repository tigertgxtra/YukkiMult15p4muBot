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
