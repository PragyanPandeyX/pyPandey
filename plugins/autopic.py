# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamPandey/Pandey/blob/main/LICENSE/>.


import asyncio
import os
import random
from random import shuffle

from telethon.tl.functions.photos import UploadProfilePhotoRequest

from pyPandey.fns.helper import download_file
from pyPandey.fns.tools import get_google_images

from . import LOGS, get_help, get_string, pdB, Pragyan_bot, Pragyan_cmd

__doc__ = get_help("help_autopic")


@Pragyan_cmd(pattern="autopic( (.*)|$)")
async def autopic(e):
    search = e.pattern_match.group(1).strip()
    if pdB.get_key("AUTOPIC") and not search:
        pdB.del_key("AUTOPIC")
        return await e.eor(get_string("autopic_5"))
    if not search:
        return await e.eor(get_string("autopic_1"), time=5)
    e = await e.eor(get_string("com_1"))
    gi = googleimagesdownload()
    args = {
        "keywords": search,
        "limit": 50,
        "format": "jpg",
        "output_directory": "./resources/downloads/",
    }
    try:
        pth = await gi.download(args)
        ok = pth[0][search]
    except Exception as er:
        LOGS.exception(er)
        return await e.eor(str(er))
    if not ok:
        return await e.eor(get_string("autopic_2").format(search), time=5)
    await e.eor(get_string("autopic_3").format(search))
    pdB.set_key("AUTOPIC", search)
    SLEEP_TIME = pdB.get_key("SLEEP_TIME") or 1221
    while True:
        for lie in ok:
            if pdB.get_key("AUTOPIC") != search:
                return
            file = await e.client.upload_file(lie)
            await e.client(UploadProfilePhotoRequest(file))
            await asyncio.sleep(SLEEP_TIME)
        shuffle(ok)


if search := pdB.get_key("AUTOPIC"):
    images = {}
    sleep = pdB.get_key("SLEEP_TIME") or 1221

    async def autopic_func():
        search = pdB.get_key("AUTOPIC")
        if images.get(search) is None:
            images[search] = await get_google_images(search)
        if not images.get(search):
            return
        img = random.choice(images[search])
        filee = await download_file(img["original"], "resources/downloads/autopic.jpg")
        file = await Pragyan_bot.upload_file(filee)
        await Pragyan_bot(UploadProfilePhotoRequest(file))
        os.remove(filee)

    try:
        from apscheduler.schedulers.asyncio import AsyncIOScheduler

        schedule = AsyncIOScheduler()
        schedule.add_job(autopic_func, "interval", seconds=sleep)
        schedule.start()
    except ModuleNotFoundError as er:
        LOGS.error(f"autopic: '{er.name}' not installed.")
