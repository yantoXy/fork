# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB/blob/main/LICENSE/>.
#


import asyncio
import sys
import time
from datetime import datetime
from typing import Any, Dict
from aiohttp import ClientSession
from gpytranslate import Translator
from pyrogram import Client
from pyrogram.types import *
from Bdrl.config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    STRING_SESSION as string1,
    STRING_SESSION2 as string2,
    STRING_SESSION3 as string3,
    STRING_SESSION4 as string4,
    STRING_SESSION5 as string5,
    DB_URL,
)
from Bdrl.logging import LOGGER


LOOP = asyncio.get_event_loop_policy().get_event_loop()
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}


API_ID = API_ID
API_HASH = API_HASH
DB_URL = DB_URL

if not string1:
    LOGGER(__name__).error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    LOGGER(__name__).error("No API_ID Found! Exiting!")
    sys.exit()

if not API_HASH:
    LOGGER(__name__).error("No API_HASH Found! Exiting!")
    sys.exit()


if string1:
    app = Client(
        name="bdrl1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=string1,
        plugins=dict(root="Bdrl/plugins"),
        in_memory=True,
    )
if string2:
    app2 = Client(
        name="bdrl2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=string2,
        plugins=dict(root="Bdrl/plugins"),
        in_memory=True,
    )
else:
    app2 = None
if string3:
    app3 = Client(
        name="bdrl3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=string3,
        plugins=dict(root="Bdrl/plugins"),
        in_memory=True,
    )
else:
    app3 = None
if string4:
    app4 = Client(
        name="bdrl4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=string4,
        plugins=dict(root="Bdrl/plugins"),
        in_memory=True,
    )
else:
    app4 = None
if string5:
    app5 = Client(
        name="bdrl5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=string5,
        plugins=dict(root="Bdrl/plugins"),
        in_memory=True,
    )
else:
    app5 = None

if BOT_TOKEN:
    bot = Client(
        name="assistantbot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
    )
else:
    bot = None
