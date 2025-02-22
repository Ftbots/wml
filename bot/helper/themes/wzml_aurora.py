
#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🌌 ✦ Repo ✦'
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = '📢 ✦ Updates ✦'
    ST_BN2_URL = 'https://t.me/NxLeech'
    ST_MSG = '''✨ 🚀 Mirror Magic ✨\n\nTurn links 🔗, files 📁, and torrents 磁 into Google Drive clouds ☁️, Rclone hubs ⚙️, Telegram stashes 📦, or DDL drops ⚡ with a tap!\n\nTap <code>{help_command}</code> to unlock bot powers 🧙!'''
    ST_BOTPM = '''✉️ Secret Bot Cave 🦇! Drop links or files here 🤫!'''
    ST_UNAUTH = '''🚫 Zone locked 🔒! Deploy your own WZML-X mirror bot 🧙.'''
    OWN_TOKEN_GENERATE = '''⚠️ Oops! Token Thief! 🦹 Get your own ✨!'''
    USED_TOKEN = '''⚠️ Uh-oh! Token used 💔! Make a fresh ✨!'''
    LOGGED_PASSWORD = '''🔑 Password locked! 🤖 Secure access granted ✅!'''
    ACTIVATE_BUTTON = '✨ Activate Token 🔑'
    TOKEN_MSG = '''🔑 ✨ Temp Token Alert ✨🔑\n\nCode: <code>{token}</code>\nTime Left: {validity}'''

    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '🔑 Logged In! 😎'
    INVALID_PASS = '⛔ Whoops! Wrong password 😫!'
    PASS_LOGGED = '🔑 Power user unlocked! 💪!'
    LOGIN_USED = '🔑 Code entry: <code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📜 Scroll the Log 📜'
    WEB_PASTE_BT = '🌐 Web Paste Wiz 🪄'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '🔰 Basic Info'
    USER_BT = '👤 Team Members'
    MICS_BT = '⚙️ Tweak Tools'
    O_S_BT = '👑 Boss Mode'
    CLOSE_BT = '❌ Exit Stage'
    HELP_HEADER = "🔥 Guide to Awesomeness 🔥\n\nTap a button to dive into each command's secrets! 🕵️"

    # async def stats(client, message):
    BOT_STATS = '''🚀 <b>Bot Brain Stats</b> 🧠\n\n⏱️ <b>Uptime:</b> {bot_uptime}\n\n📊 <b>Memory Zone</b> 🧠\n{ram_bar} {ram}%\n<b>Used:</b> {ram_u} | <b>Free:</b> {ram_f} | <b>Total:</b> {ram_t}\n\n🔀 <b>Swap Power</b> 🔀\n{swap_bar} {swap}%\n<b>Used:</b> {swap_u} | <b>Free:</b> {swap_f} | <b>Total:</b> {swap_t}\n\n💾 <b>Digital Stash</b> 💾\n{disk_bar} {disk}%\n<b>Read:</b> {disk_read}\n<b>Write:</b> {disk_write}\n<b>Used:</b> {disk_u} | <b>Free:</b> {disk_f} | <b>Total:</b> {disk_t}'''

    SYS_STATS = '''⚙️ <b>Machine Room</b> ⚙️\n\n⏱️ <b>Uptime:</b> {os_uptime}\nℹ️ <b>OS Flavor:</b> {os_version}\n💻 <b>Architecture:</b> {os_arch}\n\n📡 <b>Signal Waves</b> 📡\n⬆️ <b>Upload:</b> {up_data}\n⬇️ <b>Download:</b> {dl_data}\n📤 <b>Sent:</b> {pkt_sent}k\n📥 <b>Received:</b> {pkt_recv}k\n⚡ <b>Total Traffic:</b> {tl_data}\n\n🔥 <b>Core Power</b> 🔥\n{cpu_bar} {cpu}%\n<b>Clock Speed:</b> {cpu_freq}\n<b>Load:</b> {sys_load}\n🔥 <b>Real Cores:</b> {p_core} | 💻 <b>Virtual Cores:</b> {v_core}\n<b>Total Cores:</b> {total_core}\n<b>Usable:</b> {cpu_use}'''

    REPO_STATS = '''📚 <b>Bot Origin Story</b> 📚\n\n✨ <b>Last Mod:</b> {last_commit}\n🤖 <b>Bot Build:</b> {bot_version}\n🔥 <b>Newest Drop:</b> {lat_version}\n📜 <b>Patch Notes:</b> {commit_details}\n\n🔮 <b>Dev's Message:</b> <code>{remarks}</code>'''

    BOT_LIMITS = '''🛑 <b>Bot Restraints</b> ⛓️\n\n🔗 <b>Direct Snag:</b> {DL} GB\n🌀 <b>Torrent Takedown:</b> {TL} GB\n☁️ <b>Cloud Cage:</b> {GL} GB\n🎬 <b>YouTube Rip:</b> {YL} GB\n🎶 <b>Playlist Parade:</b> {PL}\n💾 <b>Mega Hoard:</b> {ML} GB\n🔄 <b>Clone Warp:</b> {CL} GB\nLeach Lagoon: {LL} GB\n\n🔑 <b>Key Life:</b> {TV}\n⏰ <b>User Wait:</b> {UTI} / task\n👯 <b>User Tasks:</b> {UT}\n🤖 <b>Bot Brigade:</b> {BT}'''

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '🔄 Bot Rebooting... 🚀'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''✅ <b>Back Online</b> ✅\n\n📅 <b>Date:</b> {date}\n⏰ <b>Time:</b> {time}\n🌍 <b>Time Zone:</b> {timz}\n🤖 <b>Version:</b> {version}'''
    RESTARTED = '''🔄 Bot is back! 🔥'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '⏳ Bot is Feeling Pulse... 📡'
    PING_VALUE = '⚡ <b>Pong!</b> ⚡\n<code>{value} ms</code>'

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """🚀 <b>Quest Start</b> 🚀\n\n⚙️ <b>Mode:</b> {Mode}\n👤 <b>Captain:</b> {Tag}"""
    LINKS_SOURCE = """🔗 <b>Source Found</b> 🔗\n\n📅 <b>Looted On:</b> {On}\n\n{Source}"""

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➡️ <b>Transfer Beam Engaged!</b> 💫\n\n🔗 <b>Link:</b> <a href='{msg_link}'>Warp Here</a>"
    L_LOG_START = "➡️ <b>Stealing Speed</b> 💨\n\n👤 <b>Shadow Agent:</b> {mention} ( #ID{uid} )\n🔗 <b>Target:</b> <a href='{msg_link}'>Lock On</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = '📦 <b>Loot Drop</b> 📦\n\n<b>{Name}</b>\n\n'
    SIZE = '<b>Size:</b> {Size}\n'
    ELAPSE = '<b>Time:</b> {Time}\n'
    MODE = '<b>Mode:</b> {Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES = '<b>All Drops:</b> {Files}\n'
    L_CORRUPTED_FILES = '<b>Shattered Drops:</b> {Corrupt}\n'
    L_CC = '<b>Sourced By:</b> {Tag}\n\n'
    PM_BOT_MSG = '➡️ <b>Stash Sent!</b> 📦!'
    L_BOT_MSG = '➡️ <b>Secret Stash to Bot PM!</b> ✉️'
    L_LL_MSG = '➡️ <b>Stash Map Available!</b> 🗺️\n'

    # ----- MIRROR -------
    M_TYPE = '<b>Content Type:</b> {Mimetype}\n'
    M_SUBFOLD = '<b>Sub Hideouts:</b> {Folder}\n'
    TOTAL_FILES = '<b>Total Drops:</b> {Files}\n'
    RCPATH = '<b>Stash Path:</b> <code>{RCpath}</code>\n'
    M_CC = '<b>Stash Handled By:</b> {Tag}\n\n'
    M_BOT_MSG = '➡️ <b>Cloud keys Dispatched!</b> 🔑'

    # ----- BUTTONS -------
    CLOUD_LINK = '☁️ Cloud Portal'
    SAVE_MSG = '💾 Save Powerup'
    RCLONE_LINK = '⚙️ RClone Engine'
    DDL_LINK = '⚡ {Serv} Warp'
    SOURCE_URL = '🔗 Source Link'
    INDEX_LINK_F = '📁 Index Zone'
    INDEX_LINK_D = '⚠️ Index Hazard'
    VIEW_LINK = '👁️ Glimpse Loot'
    CHECK_PM = '💬 PM Inventory'
    CHECK_LL = '📝 Loot Logs'
    MEDIAINFO_LINK = 'ℹ️ Loot Intel'
    SCREENSHOTS = '🖼️ Visions'

    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    def get_progress_bar(self, percentage):
        """Generates a stylized progress bar."""
        filled = int(percentage / 10)  # For a 10-unit bar
        bar = f"[{'𒊹︎︎︎' * filled}{'.' * (10 - filled)}]" #using 𒊹︎︎︎ as progress
        return bar

    BAR = '\n{Bar} {percentage}%'  # Progress bar
    PROCESSED = '\n🛰️ Downloading: {Processed} / {total}'  # crafted
    STATUS = '\n⏱️ ETA: {Eta} 🚀 Speed: {Speed}'  # url
    ENGINE = '\n⚙️ Engine: {Engine} | #Leech'  # url
    USER = '\n👤 Commander: {User} | 🚫 /cancel'  # seeder
    BOT_SYSTEM = '\n🛰️ Bot Systems 🛰️'
    CPU = '\n💻 CPU: {cpu}% | 💾 RAM: {free}% | ⚡ Uptime: {uptime}'  # leecher
    SYSTEM_STATUS = '\n📡 DL: {DL} | 📤 UL: {UL}'
    CREDIT = '\nPowered by NxLeech' #new line with credit

    ####--------OVERALL MSG FOOTER----------
    USER = '\n👤 Hero: <code>{User}</code> | '
    ID = '🆔 Tag: <code>{Id}</code>'
    BTSEL = '\n🕹️ Pick: {Btsel}'
    CANCEL = '\n🚫 End Quest: {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '🤖 Bot Pulse 🤖\n'
    TASKS = '📌 Quests: {Tasks}\n'
    BOT_TASKS = '📌 Quests: {Tasks}/{Ttask} | 📝 Free Slots: {Free}\n'
    Cpu = '💻 CPU Surge: {cpu}% | '
    FREE = '💾 Free RAM: {free} [{free_p}%]'
    Ram = '\n🧠 RAM Flow: {ram}% | '
    uptime = '⬆️ Online Time: {uptime}'
    DL = '\n⬇️ Incoming: {DL}/s | '
    UL = '⬆️ Outgoing: {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '🔄 Recharge\n{Page}'
    NEXT = '⏩'

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'Portal Blocked!\nRepeat portal detected.\n{content} portals found:'

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = 'Counting Portals... 💫'
    COUNT_NAME = '📦 ✦ {COUNT_NAME} ✦ 📦\n\n'
    COUNT_SIZE = '<b>Size:</b> {COUNT_SIZE}\n'
    COUNT_TYPE = '<b>Essence:</b> {COUNT_TYPE}\n'
    COUNT_SUB = '<b>Sub-Portals:</b> {COUNT_SUB}\n'
    COUNT_FILE = '<b>Total Portals:</b> {COUNT_FILE}\n'
    COUNT_CC = '<b>Guide:</b> {COUNT_CC}\n'

    # LIST ---> gd_list.py
    LIST_SEARCHING = '🔎 Scanning for <i>{NAME}</i>'
    LIST_FOUND = '✅ <b>Portal Found!</b> {NO} entries for <i>{NAME}</i>'
    LIST_NOT_FOUND = '🚫 No Trace Found for <i>{NAME}</i>'

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''🚫 <b>No active quests!</b>\n\n🤖 <b>Bot Systems</b> 🤖\n💻 CPU: {cpu}% | 💾 Free RAM: {free} [{free_p}%]\n🧠 RAM: {ram} | ⬆️ Run Time: {uptime}'''

    # USER Setting --> user_setting.py
    USER_SETTING = '''⚙️ <b>Hero Profile</b> ⚙️\n\n<b>Name:</b> {NAME} ( <code>{ID}</code> )\n<b>Alias:</b> {USERNAME}\n<b>World Region:</b> {DC}\n<b>Spoken Tongue:</b> {LANG}\n\nℹ️ <b>Secret Codes:</b>\n-s or -set: Direct Imprint'''

    UNIVERSAL = '''⚙️ <b>Global Powers</b> ⚙️\n\nYouTube Unlock: <code>{YT}</code>\nDaily Rituals: <code>{DT}</code>\nLast Channel: <code>{LAST_USED}</code>\nSession Seal: <code>{USESS}</code>\nVision Mode: <code>{MEDIAINFO}</code>\nSave Code: <code>{SAVE_MODE}</code>\nPM Link: <code>{BOT_PM}</code>'''

    MIRROR = '''⚙️ <b>Mirror Rituals</b> 🪞\n\nRClone Key: <i>{RCLONE}</i>\nCallsign: <code>{MPREFIX}</code>\nEnding: <code>{MSUFFIX}</code>\nRename Spell: <code>{MREMNAME}</code>\nDestination: <i>{DDL_SERVER}</i>\nTeam Drive: <i>{TMODE}</i>\nTeam Strength: <i>{USERTD}</i>\nDaily Summon: <code>{DM}</code>'''

    LEECH = '''⚙️ <b>Steal Settings</b> ⚙️\n\nDaily Raids: <code>{DL}</code>\nType: <i>{LTYPE}</i>\nImage Sigil: <i>{THUMB}</i>\nSplit Chunk: <code>{SPLIT_SIZE}</code>\nEqual Share: <i>{EQUAL_SPLIT}</i>\nMedia Group: <i>{MEDIA_GROUP}</i>\nCrafting: <code>{LCAPTION}</code>\nPrefix: <code>{LPREFIX}</code>\nEnding: <code>{LSUFFIX}</code>\nBurial Site: <code>{LDUMP}</code>\nAlter Name: <code>{LREMNAME}</code>'''

    ####--------Replaced the previous section with this ---------

    def get_readable_message(self, progress, bot_stats):
        """Generates the formatted progress and stats message."""
        percentage = progress.get('percentage', 0)
        bar = self.get_progress_bar(percentage)  # Get the progress bar

        msg = f"""
🌚 {progress.get('name')} 🌚
{bar} {percentage}%
{self.PROCESSED.format(Processed=progress.get('processed'), total = progress.get('total'))}
{self.STATUS.format(Eta=progress.get('eta'), Speed=progress.get('speed'))}
{self.ENGINE.format(Engine=progress.get('engine'))}
{self.USER.format(User=progress.get('user'))}

{self.BOT_SYSTEM}
{self.CPU.format(cpu=bot_stats.get('cpu'), free=bot_stats.get('free'), uptime=bot_stats.get('uptime'))}
{self.SYSTEM_STATUS.format(DL=bot_stats.get('dl'), UL=bot_stats.get('ul'))}
{self.CREDIT}
"""
        return msg
        
