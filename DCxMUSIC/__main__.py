import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DCxMUSIC import LOGGER, app, userbot
from DCxMUSIC.core.call import DC
from DCxMUSIC.misc import sudo
from DCxMUSIC.plugins import ALL_MODULES
from DCxMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DCxMUSIC.plugins" + all_module)
    LOGGER("DCxMUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await DC.start()
    try:
        await DC.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DCxMUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await DC.decorators()
    LOGGER("DCxMUSIC").info(
        "f09d8493f09d848cf09d849cf09d8488f09d8497f09d848af09d8493f09d8488f09d8495f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488f09d8493f09d848cf09d8496f09d848af09d8492f09d848bf09d8495f09d8488"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DCxMUSIC").info("Stopping DC Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
