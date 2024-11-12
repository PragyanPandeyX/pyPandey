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
    thumb = "resources/extras/Pragyan.jpg"


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
    from .version import Pragyan_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    pdB = PandeyDB()
    update_envs()

    LOGS.info(f"Connecting to {pdB.name}...")
    if pdB.ping():
        LOGS.info(f"Connected to {pdB.name} Successfully!")

    BOT_MODE = pdB.get_key("BOTMODE")
    DUAL_MODE = pdB.get_key("DUAL_MODE")

    USER_MODE = pdB.get_key("USER_MODE")
    if USER_MODE:
        DUAL_MODE = False

    if BOT_MODE:
        if DUAL_MODE:
            pdB.del_key("DUAL_MODE")
            DUAL_MODE = False
        Pragyan_bot = None

        if not pdB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        Pragyan_bot = PandeyClient(
            validate_session(Var.SESSION, LOGS),
            pdB=pdB,
            app_version=Pragyan_version,
            device_model="Pandey",
        )
        Pragyan_bot.run_in_loop(autobot())

    if USER_MODE:
        asst = Pragyan_bot
    else:
        asst = PandeyClient("asst", bot_token=pdB.get_key("BOT_TOKEN"), pdB=pdB)

    if BOT_MODE:
        Pragyan_bot = asst
        if pdB.get_key("OWNER_ID"):
            try:
                Pragyan_bot.me = Pragyan_bot.run_in_loop(
                    Pragyan_bot.get_entity(pdB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder and asst._bot:
        Pragyan_bot.run_in_loop(enable_inline(Pragyan_bot, asst.me.username))

    vcClient = vc_connection(pdB, Pragyan_bot)

    _version_changes(pdB)

    HNDLR = pdB.get_key("HNDLR") or "."
    DUAL_HNDLR = pdB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = pdB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyPandey 2022 © TeamPandey")

    from logging import getLogger

    LOGS = getLogger("pyPandey")

    Pragyan_bot = asst = pdB = vcClient = None
