from . import eor, SUDO_HNDLR, Pragyan_cmd
from os import mkdir
from . import HNDLR, get_string, inline_mention, pdB, Pragyan_bot
from pyPandey._misc import sudoers  # Correct import for sudoers

@Pragyan_cmd(pattern="sur")
async def szudo(e):
    reply = await e.get_reply_message()
    rid = "{}".format(reply.sender_id)
    pdB.set_key("SUDOS", list(rid))
    pdB.set_key("FULLSUDO", rid)
    name = await e.client.get_entity(int(rid))
    una = name.username
    fn = name.first_name
    ln = name.last_name
    men = inline_mention(name)
    ii = pdB.get_key("FULLSUDO")
    await e.reply(f"""**Added** {men} **as FULLSUDO and SUDO User**

First name : {fn}
Last name : {ln}
id : {ii}
username : {una}
HNDLR : {HNDLR}
SUDO_HNDLR : {SUDO_HNDLR}
""")

@Pragyan_cmd(pattern="su$")
async def _(ult):
    x = await ult.eor("**Adding.....**")
    n = pdB.get_key("SUDOS") or []
    async for m in ult.client.iter_participants(ult.chat_id):
        if not (m.bot or m.deleted):
            n.append(m.id)

    n = list(set(n))
    pdB.set_key('SUDOS', n)
    pdB.set_key('FULLSUDO', " ".join(str(i) for i in n))
    await x.edit(f"""
**Added FULLSUDO and SUDO in this group members**

HNDLR : {HNDLR}
SUDO_HNDLR : {SUDO_HNDLR}""")

    await ult.respond("**Now checking....**")
    sudos = sudoers()
    if not sudos:
        return await ult.eor(get_string("sudo_3"), time=5)
    msg = ""
    for i in sudos:
        try:
            name = await ult.client.get_entity(int(i))
        except BaseException:
            name = None
        if name:
            msg += f"• {inline_mention(name)} ( `{i}` )\n"
        else:
            msg += f"• `{i}` -> Invalid User\n"
    m = pdB.get_key("SUDO") or True
    if not m:
        m = "[False](https://graph.org/Pandey-04-06)"
        await ult.eor(
            f"**SUDO MODE : {m}\n\nList of SUDO Users :**\n{msg}", link_preview=False
        )

    if not "sudo":
        mkdir("sudo")

    if len(msg) > 4096:
        with open("list.txt", "w") as ld:
            ld.write(f"{msg}")
    b, _ = await ult.client.fast_uploader(f"list.txt")
    c = await ult.client.send_file(ult.chat, b)

@Pragyan_cmd(pattern="blocksudo")
async def block_sudo(e):
    reply = await e.get_reply_message()
    if not reply:
        return await e.reply("Please reply to the user you want to block from SUDO.")

    rid = "{}".format(reply.sender_id)

    # Get the current list of SUDO users
    sudos = pdB.get_key("SUDOS") or []
    full_sudo = pdB.get_key("FULLSUDO")

    # Debug prints to track values
    print("User ID to block:", rid)
    print("Current SUDO list before removal:", sudos)

    if rid not in sudos:
        return await e.reply("This user is not in the SUDO list.")

    # Remove the user from the SUDO list
    sudos.remove(rid)
    pdB.set_key("SUDOS", sudos)

    # Check if the user is the FULLSUDO and clear that entry if necessary
    if full_sudo == rid:
        pdB.set_key("FULLSUDO", None)

    # Debug print after removal
    print("Updated SUDO list after removal:", pdB.get_key("SUDOS"))

    # Notify that the user has been blocked
    name = await e.client.get_entity(int(rid))
    men = inline_mention(name)

    await e.reply(f"**Removed** {men} **from SUDO and blocked from using the bot.**")
