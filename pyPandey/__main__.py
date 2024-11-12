# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamPandey/pyPandey/blob/main/LICENSE>.

from . import *


def main():
    import os
    import sys
    import time

    from .fns.helper import bash, time_formatter, updater
    from .startup.funcs import (
        WasItRestart,
        autopilot,
        customize,
        fetch_ann,
        plug,
        ready,
        startup_stuff,
    )
    from .startup.loader import load_other_plugins

    try:
        from apscheduler.schedulers.asyncio import AsyncIOScheduler
    except ImportError:
        AsyncIOScheduler = None

    # Option to Auto Update On Restarts..
    if (
        pdB.get_key("UPDATE_ON_RESTART")
        and os.path.exists(".git")
        and Pragyan_bot.run_in_loop(updater())
    ):
        Pragyan_bot.run_in_loop(bash("bash installer.sh"))

        os.execl(sys.executable, sys.executable, "-m", "pyPandey")

    Pragyan_bot.run_in_loop(startup_stuff())

    Pragyan_bot.me.phone = None

    if not Pragyan_bot.me.bot:
        pdB.set_key("OWNER_ID", Pragyan_bot.uid)

    LOGS.info("Initialising...")

    Pragyan_bot.run_in_loop(autopilot())

    pmbot = pdB.get_key("PMBOT")
    manager = pdB.get_key("MANAGER")
    addons = pdB.get_key("ADDONS") or Var.ADDONS
    vcbot = pdB.get_key("VCBOT") or Var.VCBOT
    if HOSTED_ON == "okteto":
        vcbot = False

    if (HOSTED_ON == "termux" or pdB.get_key("LITE_DEPLOY")) and pdB.get_key(
        "EXCLUDE_OFFICIAL"
    ) is None:
        _plugins = "autocorrect autopic audiotools compressor forcesubscribe fedutils gdrive glitch instagram nsfwfilter nightmode pdftools profanityfilter writer youtube"
        pdB.set_key("EXCLUDE_OFFICIAL", _plugins)

    load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

    suc_msg = """
            ----------------------------------------------------------------------
                Pandey has been deployed! Visit @ThePandey for updates!!
            ----------------------------------------------------------------------
    """

    # for channel plugins
    plugin_channels = pdB.get_key("PLUGIN_CHANNEL")

    # Customize Pandey Assistant...
    Pragyan_bot.run_in_loop(customize())

    # Load Addons from Plugin Channels.
    if plugin_channels:
        Pragyan_bot.run_in_loop(plug(plugin_channels))

    # Send/Ignore Deploy Message..
    if not pdB.get_key("LOG_OFF"):
        Pragyan_bot.run_in_loop(ready())

    # TODO: Announcement API IS DOWN
    # if AsyncIOScheduler:
    #     scheduler = AsyncIOScheduler()
    #     scheduler.add_job(fetch_ann, "interval", minutes=12 * 60)
    #     scheduler.start()

    # Edit Restarting Message (if It's restarting)
    Pragyan_bot.run_in_loop(WasItRestart(pdB))

    try:
        cleanup_cache()
    except BaseException:
        pass

    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •ULTROID•"
    )
    LOGS.info(suc_msg)


if __name__ == "__main__":
    main()

    asst.run()
