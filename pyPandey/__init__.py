# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamPandey/pyPandey/blob/main/LICENSE>.

import os
import sys
import dns.resolver
import socket

from .version import __version__

run_as_module = __package__ in sys.argv or sys.argv[0] == "-m"


class ULTConfig:
    lang = "en"
    thumb = "resources/extras/ultroid.jpg"


def custom_resolver(hostname):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["8.8.8.8", "8.8.4.4"]  # Using Google's DNS servers
    answers = resolver.resolve(hostname, "A")
    return answers[0].address


original_getaddrinfo = socket.getaddrinfo


def custom_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    try:
        ip = custom_resolver(host)
        return [(socket.AF_INET, socket.SOCK_STREAM, proto, "", (ip, port))]
    except Exception as e:
        return original_getaddrinfo(host, port, family, type, proto, flags)


socket.getaddrinfo = custom_getaddrinfo


if run_as_module:
    import time

    from .configs import Var
    from .startup import *
    from .startup._database import PandeyDB
    from .startup.BaseClient import PandeyClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import ultroid_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    udB = PandeyDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    USER_MODE = udB.get_key("USER_MODE")
    if USER_MODE:
        DUAL_MODE = False

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        ultroid_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        ultroid_bot = PandeyClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=ultroid_version,
            device_model="Pandey",
        )
        ultroid_bot.run_in_loop(autobot())

    if USER_MODE:
        asst = ultroid_bot
    else:
        asst = PandeyClient("asst", bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        ultroid_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                ultroid_bot.me = ultroid_bot.run_in_loop(
                    ultroid_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder and asst._bot:
        ultroid_bot.run_in_loop(enable_inline(ultroid_bot, asst.me.username))

    vcClient = vc_connection(udB, ultroid_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyPandey 2022 © TeamPandey")

    from logging import getLogger

    LOGS = getLogger("pyPandey")

    ultroid_bot = asst = udB = vcClient = None
