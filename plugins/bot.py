# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamPandey/Pandey/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_bot")

import os
import sys
import time
from platform import python_version as pyver
from random import choice

from telethon import __version__
from telethon.errors.rpcerrorlist import (
    BotMethodInvalidError,
    ChatSendMediaForbiddenError,
)

from pyPandey.version import __version__ as UltVer

from . import HOSTED_ON, LOGS

try:
    from git import Repo
except ImportError:
    LOGS.error("bot: 'gitpython' module not found!")
    Repo = None

from telethon.utils import resolve_bot_file_id

from . import (
    ATRA_COL,
    LOGS,
    OWNER_NAME,
    ULTROID_IMAGES,
    Button,
    Carbon,
    Telegraph,
    Var,
    allcmds,
    asst,
    bash,
    call_back,
    callback,
    def_logs,
    eor,
    get_string,
    heroku_logs,
    in_pattern,
    inline_pic,
    restart,
    shutdown,
    start_time,
    time_formatter,
    pdB,
    Pragyan_cmd,
    Pragyan_version,
    updater,
)


def ULTPIC():
    return inline_pic() or choice(ULTROID_IMAGES)


buttons = [
    [
        Button.url(get_string("bot_3"), "https://github.com/TeamPandey/Pandey"),
        Button.url(get_string("bot_4"), "t.me/PandeySupportChat"),
    ]
]

# Will move to strings
alive_txt = """
The Pandey Userbot

  ◍ Version - {}
  ◍ Py-Pandey - {}
  ◍ Telethon - {}
"""

in_alive = "{}\n\n🌀 <b>Pandey Version -><b> <code>{}</code>\n🌀 <b>PyPandey -></b> <code>{}</code>\n🌀 <b>Python -></b> <code>{}</code>\n🌀 <b>Uptime -></b> <code>{}</code>\n🌀 <b>Branch -></b>[ {} ]\n\n• <b>Join @TeamPandey</b>"


@callback("alive")
async def alive(event):
    text = alive_txt.format(Pragyan_version, UltVer, __version__)
    await event.answer(text, alert=True)


@Pragyan_cmd(
    pattern="alive( (.*)|$)",
)
async def lol(ult):
    match = ult.pattern_match.group(1).strip()
    inline = None
    if match in ["inline", "i"]:
        try:
            res = await ult.client.inline_query(asst.me.username, "alive")
            return await res[0].click(ult.chat_id)
        except BotMethodInvalidError:
            pass
        except BaseException as er:
            LOGS.exception(er)
        inline = True
    pic = pdB.get_key("ALIVE_PIC")
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = pdB.get_key("ALIVE_TEXT") or get_string("bot_1")
#    y = Repo().active_branch
    y = "main"
#    xx = Repo().remotes[0].config_reader.get("url")
    xx = "https://github.com/TeamPandey/PandeyBackup.git"
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    if inline:
        kk = f"<a href={rep}>{y}</a>"
        parse = "html"
        als = in_alive.format(
            header,
            f"{Pragyan_version} [{HOSTED_ON}]",
            UltVer,
            pyver(),
            uptime,
            kk,
        )

        if _e := pdB.get_key("ALIVE_EMOJI"):
            als = als.replace("🌀", _e)
    else:
        parse = "md"
        als = (get_string("alive_1")).format(
            header,
            OWNER_NAME,
            f"{Pragyan_version} [{HOSTED_ON}]",
            UltVer,
            uptime,
            pyver(),
            __version__,
            kk,
        )

        if a := pdB.get_key("ALIVE_EMOJI"):
            als = als.replace("✵", a)
    if pic:
        try:
            await ult.reply(
                als,
                file=pic,
                parse_mode=parse,
                link_preview=False,
                buttons=buttons if inline else None,
            )
            return await ult.try_delete()
        except ChatSendMediaForbiddenError:
            pass
        except BaseException as er:
            LOGS.exception(er)
            try:
                await ult.reply(file=pic)
                await ult.reply(
                    als,
                    parse_mode=parse,
                    buttons=buttons if inline else None,
                    link_preview=False,
                )
                return await ult.try_delete()
            except BaseException as er:
                LOGS.exception(er)
    await eor(
        ult,
        als,
        parse_mode=parse,
        link_preview=False,
        buttons=buttons if inline else None,
    )


@Pragyan_cmd(pattern="ping$", chats=[], type=["official", "assistant"])
async def _(event):
    start = time.time()
    x = await event.eor("Pong !")
    end = round((time.time() - start) * 1000)
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.edit(get_string("ping").format(end, uptime))


@Pragyan_cmd(
    pattern="cmds$",
)
async def cmds(event):
    await allcmds(event, Telegraph)


heroku_api = Var.HEROKU_API


@Pragyan_cmd(
    pattern="restart$",
    fullsudo=True,
)
async def restartbt(ult):
    ok = await ult.eor(get_string("bot_5"))
    call_back()
    who = "bot" if ult.client._bot else "user"
    pdB.set_key("_RESTART", f"{who}_{ult.chat_id}_{ok.id}")
    if heroku_api:
        return await restart(ok)
    await bash("git pull && pip3 install -r requirements.txt")
    if len(sys.argv) > 1:
        os.execl(sys.executable, sys.executable, "main.py")
    else:
        os.execl(sys.executable, sys.executable, "-m", "pyPandey")


@Pragyan_cmd(
    pattern="shutdown$",
    fullsudo=True,
)
async def shutdownbot(ult):
    await shutdown(ult)


@Pragyan_cmd(
    pattern="logs( (.*)|$)",
    chats=[],
)
async def _(event):
    opt = event.pattern_match.group(1).strip()
    file = f"Pragyan{sys.argv[-1]}.log" if len(sys.argv) > 1 else "Pragyan.log"
    if opt == "heroku":
        await heroku_logs(event)
    elif opt == "carbon" and Carbon:
        event = await event.eor(get_string("com_1"))
        with open(file, "r") as f:
            code = f.read()[-2500:]
        file = await Carbon(
            file_name="Pragyan-logs",
            code=code,
            backgroundColor=choice(ATRA_COL),
        )
        if isinstance(file, dict):
            await event.eor(f"`{file}`")
            return
        await event.reply("**Pandey Logs.**", file=file)
    elif opt == "open":
        with open("Pragyan.log", "r") as f:
            file = f.read()[-4000:]
        return await event.eor(f"`{file}`")
    else:
        await def_logs(event, file)
    await event.try_delete()


@in_pattern("alive", owner=True)
async def inline_alive(ult):
    pic = pdB.get_key("ALIVE_PIC")
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = pdB.get_key("ALIVE_TEXT") or get_string("bot_1")
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f"<a href={rep}>{y}</a>"
    als = in_alive.format(
        header, f"{Pragyan_version} [{HOSTED_ON}]", UltVer, pyver(), uptime, kk
    )

    if _e := pdB.get_key("ALIVE_EMOJI"):
        als = als.replace("🌀", _e)
    builder = ult.builder
    if pic:
        try:
            if ".jpg" in pic:
                results = [
                    await builder.photo(
                        pic, text=als, parse_mode="html", buttons=buttons
                    )
                ]
            else:
                if _pic := resolve_bot_file_id(pic):
                    pic = _pic
                    buttons.insert(
                        0, [Button.inline(get_string("bot_2"), data="alive")]
                    )
                results = [
                    await builder.document(
                        pic,
                        title="Inline Alive",
                        description="@TeamPandey",
                        parse_mode="html",
                        buttons=buttons,
                    )
                ]
            return await ult.answer(results)
        except BaseException as er:
            LOGS.exception(er)
    result = [
        await builder.article(
            "Alive", text=als, parse_mode="html", link_preview=False, buttons=buttons
        )
    ]
    await ult.answer(result)


@Pragyan_cmd(pattern="update( (.*)|$)")
async def _(e):
    xx = await e.eor(get_string("upd_1"))
    if e.pattern_match.group(1).strip() and (
        "fast" in e.pattern_match.group(1).strip()
        or "soft" in e.pattern_match.group(1).strip()
    ):
        await bash("git pull -f && pip3 install -r requirements.txt")
        call_back()
        await xx.edit(get_string("upd_7"))
        os.execl(sys.executable, "python3", "-m", "pyPandey")
        # return
    m = await updater()
    branch = (Repo.init()).active_branch
    if m:
        x = await asst.send_file(
            pdB.get_key("LOG_CHANNEL"),
            ULTPIC(),
            caption="• **Update Available** •",
            force_document=False,
            buttons=Button.inline("Changelogs", data="changes"),
        )
        Link = x.message_link
        await xx.edit(
            f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
    else:
        await xx.edit(
            f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/TeamPandey/Pandey/tree/{branch}">[{branch}]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )


@callback("updtavail", owner=True)
async def updava(event):
    await event.delete()
    await asst.send_file(
        pdB.get_key("LOG_CHANNEL"),
        ULTPIC(),
        caption="• **Update Available** •",
        force_document=False,
        buttons=Button.inline("Changelogs", data="changes"),
    )
