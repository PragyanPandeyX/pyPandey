# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamPandey/Pandey/blob/main/LICENSE/>.
"""
✘ Commands Available -

•`{i}addprofanity`
   If someone sends bad word in a chat, Then bot will delete that message.

•`{i}remprofanity`
   From chat from Profanity list.

"""

from pyPandey.dB.nsfw_db import profan_chat, rem_profan

from . import get_string, ultroid_cmd


@ultroid_cmd(pattern="(add|rem)profanity$", admins_only=True)
async def addp(e):
    cas = e.pattern_match.group(1)
    add = cas == "add"
    if add:
        profan_chat(e.chat_id, "mute")
        await e.eor(get_string("prof_1"), time=10)
        return
    rem_profan(e.chat_id)
    await e.eor(get_string("prof_2"), time=10)
