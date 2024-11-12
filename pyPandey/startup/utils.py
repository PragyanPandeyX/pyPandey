# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamPandey/pyPandey/blob/main/LICENSE>.

from importlib import util
from sys import modules

# for addons

configPaths = [
    "ub",
    "var",
    "support",
    "userbot",
    "telebot",
    "fridaybot",
    "uniborg.util",
    "telebot.utils",
    "userbot.utils",
    "userbot.events",
    "userbot.config",
    "fridaybot.utils",
    "fridaybot.Config",
    "userbot.uniborgConfig",
]


def load_addons(plugin_name):
    base_name = plugin_name.split("/")[-1].split("\\")[-1].replace(".py", "")
    if base_name.startswith("__"):
        return
    from pyPandey import fns

    from .. import HNDLR, LOGS, asst, pdB, Pragyan_bot
    from .._misc import _supporter as config
    from .._misc._assistant import asst_cmd, callback, in_pattern
    from .._misc._decorators import Pragyan_cmd
    from .._misc._supporter import Config, admin_cmd, sudo_cmd
    from .._misc._wrappers import eod, eor
    from ..configs import Var
    from ..dB._core import HELP

    name = plugin_name.replace("/", ".").replace("\\", ".").replace(".py", "")
    spec = util.spec_from_file_location(name, plugin_name)
    mod = util.module_from_spec(spec)
    for path in configPaths:
        modules[path] = config
    modules["pyPandey.functions"] = fns
    mod.LOG_CHANNEL = pdB.get_key("LOG_CHANNEL")
    mod.pdB = pdB
    mod.asst = asst
    mod.tgbot = asst
    mod.Pragyan_bot = Pragyan_bot
    mod.ub = Pragyan_bot
    mod.bot = Pragyan_bot
    mod.Pragyan = Pragyan_bot
    mod.borg = Pragyan_bot
    mod.telebot = Pragyan_bot
    mod.jarvis = Pragyan_bot
    mod.friday = Pragyan_bot
    mod.eod = eod
    mod.edit_delete = eod
    mod.LOGS = LOGS
    mod.in_pattern = in_pattern
    mod.hndlr = HNDLR
    mod.handler = HNDLR
    mod.HNDLR = HNDLR
    mod.CMD_HNDLR = HNDLR
    mod.Config = Config
    mod.Var = Var
    mod.eor = eor
    mod.edit_or_reply = eor
    mod.asst_cmd = asst_cmd
    mod.Pragyan_cmd = Pragyan_cmd
    mod.on_cmd = Pragyan_cmd
    mod.callback = callback
    mod.Redis = pdB.get_key
    mod.admin_cmd = admin_cmd
    mod.sudo_cmd = sudo_cmd
    mod.HELP = HELP.get("Addons", {})
    mod.CMD_HELP = HELP.get("Addons", {})

    spec.loader.exec_module(mod)
    modules[name] = mod
    doc = modules[name].__doc__.format(i=HNDLR) if modules[name].__doc__ else ""
    if "Addons" in HELP.keys():
        update_cmd = HELP["Addons"]
        try:
            update_cmd.update({base_name: doc})
        except BaseException:
            pass
    else:
        try:
            HELP.update({"Addons": {base_name: doc}})
        except BaseException as em:
            pass
