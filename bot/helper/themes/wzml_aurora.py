
#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🌌 ✦ Repo ✦'
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = '📢 ✦ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ✦'
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
    USER_BT = '👤 Users'
    MICS_BT = '⚙️ Tweak Tools'
    O_S_BT = '👑 Owner & Sudos'
    CLOSE_BT = '❌ Close'
    HELP_HEADER = "🔥 Guide to Awesomeness 🔥\n\nTap a button to dive into each command's secrets! 🕵️"

    # async def stats(client, message):
    BOT_STATS = '''🚀 Bot Stats 🧠\n\n⏱️ Uptime: {bot_uptime}\n\n📊 Ram 🧠\n{ram_bar} {ram}%\nUsed: {ram_u} | Free: {ram_f} | Total: {ram_t}\n\n🔀 Swap Memory 🔀\n{swap_bar} {swap}%\nUsed: {swap_u} | Free: {swap_f} | Total: {swap_t}\n\n💾 Disk 💾\n{disk_bar} {disk}%\nRead: {disk_read}\nWrite: {disk_write}\nUsed: {disk_u} | Free: {disk_f} | Total: {disk_t}'''

    SYS_STATS = '''⚙️ Machine System ⚙️\n\n⏱️ OS Uptime: {os_uptime}\nℹ️ OS Version: {os_version}\n💻 OS Architecture: {os_arch}\n\n📡 Network Stats 📡\n⬆️ Upload: {up_data}\n⬇️ Download: {dl_data}\n📤 Sent: {pkt_sent}k\n📥 Received: {pkt_recv}k\n⚡ Total Traffic: {tl_data}\n\n🔥 Core Power 🔥\n{cpu_bar} {cpu}%\nClock Speed: {cpu_freq}\nLoad: {sys_load}\n🔥 Real Cores: {p_core} | 💻 Virtual Cores: {v_core}\nTotal Cores: {total_core}\nUsable: {cpu_use}'''

    REPO_STATS = '''📚 CPU 📚\n\n✨ Last Mod: {last_commit}\n🤖 Bot Build: {bot_version}\n🔥 Newest Drop: {lat_version}\n📜 Patch Notes: {commit_details}\n\n🔮 Dev's Message: <code>{remarks}</code>'''

    BOT_LIMITS = '''🛑 Bot Restraints ⛓️\n\n🔗 Direct Limits: {DL} GB\n🌀 Torrent Limits: {TL} GB\n☁️ GDrive Limits: {GL} GB\n🎬 YT-DLP Limit: {YL} GB\n🎶 Playlist Limit: {PL}\n💾 Mega Limit: {ML} GB\n🔄 Clone Limit: {CL} GB\nLeach Limits: {LL} GB\n\n🔑 Key Life: {TV}\n⏰ User Wait: {UTI} / task\n👯 User Tasks: {UT}\n🤖 Bot Parallel Tasks: {BT}'''

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '🔄 Bot Rebooting... 🚀'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''✅ Back Online ✅\n\n📅 Date: {date}\n⏰ Time: {time}\n🌍 Time Zone: {timz}\n🤖 Version: {version}'''
    RESTARTED = '''🔄 Bot is back! 🔥'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '⏳ Bot is Feeling Pulse... 📡'
    PING_VALUE = '⚡ Pong! ⚡\n<code>{value} ms</code>'

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """🚀 Quest Start 🚀\n\n⚙️ Mode: {Mode}\n👤 Captain: {Tag}"""
    LINKS_SOURCE = """🔗 Source Found 🔗\n\n📅 Looted On: {On}\n\n{Source}"""

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➡️ Transfer Beam Engaged! 💫\n\n🔗 Link: <a href='{msg_link}'>Warp Here</a>"
    L_LOG_START = "➡️ Stealing Speed 💨\n\n👤 Shadow Agent: {mention} ( #ID{uid} )\n🔗 Target: <a href='{msg_link}'>Lock On</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = '💀 Loot Drop 💀\n\n<b>{Name}</b>\n\n'
    SIZE = 'Size: {Size}\n'
    ELAPSE = 'Time: {Time}\n'
    MODE = 'Mode: {Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES = 'Total Files: {Files}\n'
    L_CORRUPTED_FILES = 'Shattered Files: {Corrupt}\n'
    L_CC = 'Sourced By: {Tag}\n\n'
    PM_BOT_MSG = '➡️ File Has been Sent! 💓!'
    L_BOT_MSG = '➡️ Secret Stash to Bot PM! ✉️'
    L_LL_MSG = '➡️ Stash Link Available! 🗺️\n'

    # ----- MIRROR -------
    M_TYPE = 'Content Type: {Mimetype}\n'
    M_SUBFOLD = 'Sub Hideouts: {Folder}\n'
    TOTAL_FILES = 'Total Drops: {Files}\n'
    RCPATH = 'Stash Path: <code>{RCpath}</code>\n'
    M_CC = 'Stash Handled By: {Tag}\n\n'
    M_BOT_MSG = '➡️ Cloud keys Dispatched! 🔑'

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
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME = '💀 ✦ {Name} ✦ 💀'

    #####---------PROGRESSIVE STATUS-------
    BAR = '\n{Bar} ✦'
    PROCESSED = '\n✅ Proceed: {Processed}'
    STATUS = '\n📶 Status: <a href="{Url}">{Status}</a>'
    ETA = ' | ⏰ ETA™: {Eta}'
    SPEED = '\n💨 Speed: {Speed}'
    ELAPSED = ' | ⏱️ Past: {Elapsed}'
    ENGINE = '\n⚙️ Engine: {Engine}'
    STA_MODE = '\n🕹️ Style: {Mode}'
    SEEDERS = '\n🌱 Helpers: {Seeders} | '
    LEECHERS = '🦹 Looters: {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE = '\n📦 Weight: {Size}'
    SEED_SPEED = '\n⚡ Burst: {Speed} | '
    UPLOADED = '⬆️ Airborne: {Upload}'
    RATIO = '\n♻️ Cycle: {Ratio} | '
    TIME = '⏰ Duration: {Time}'
    SEED_ENGINE = '\n⚙️ Heart: {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = '\n📦 Weight: {Size}'
    NON_ENGINE = '\n⚙️ Core: {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER = '\n👤 Hero: <code>{User}</code> | '
    ID = '🆔 Tag: <code>{Id}</code>'
    BTSEL = '\n🕹️ Pick: {Btsel}'
    CANCEL = '\n🚫 Cancle: {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '🤖 Bot Stats 🤖\n'
    TASKS = '📌 Quests: {Tasks}\n'
    BOT_TASKS = '📌 Quests: {Tasks}/{Ttask} | 📝 Free Slots: {Free}\n'
    Cpu = '💻 CPU: {cpu}% | '
    FREE = '💾 Free: {free} [{free_p}%]'
    Ram = '\n🧠 RAM: {ram}% | '
    uptime = '✅ Online Time: {uptime}'
    DL = '\n⬇️ DL: {DL}/s | '
    UL = '⬆️ UL: {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '🔄 REFRESH\n{Page}'
    NEXT = '⏩'

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'Portal Blocked!\nRepeat portal detected.\n{content} portals found:'

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = 'Counting Portals... 💫'
    COUNT_NAME = '🌚 ✦ {COUNT_NAME} ✦ 🌚\n\n'
    COUNT_SIZE = 'Size: {COUNT_SIZE}\n'
    COUNT_TYPE = 'Type: {COUNT_TYPE}\n'
    COUNT_SUB = 'SubFolders: {COUNT_SUB}\n'
    COUNT_FILE = 'Total Files: {COUNT_FILE}\n'
    COUNT_CC = 'cc: {COUNT_CC}\n'

    # LIST ---> gd_list.py
    LIST_SEARCHING = '🔎 Scanning for <i>{NAME}</i>'
    LIST_FOUND = '✅ Portal Found! {NO} entries for <i>{NAME}</i>'
    LIST_NOT_FOUND = '🚫 No Trace Found for <i>{NAME}</i>'

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''🚫 No active tasks!\n\n🤖 Bot Systems 🤖\n💻 CPU: {cpu}% | 🌀 Free: {free} [{free_p}%]\n📟 RAM: {ram} | ⏰ Run Time: {uptime}'''

    # USER Setting --> user_setting.py
    USER_SETTING = '''⚙️ Hero Profile ⚙️\n\nName: {NAME} ( <code>{ID}</code> )\nAlias: {USERNAME}\nDC: {DC}\nlang: {LANG}\n\nℹ️ Secret Codes:\n-s or -set: Direct Imprint'''

    UNIVERSAL = '''⚙️ Universal Settings  ⚙️\n\nYT-DLP Options: <code>{YT}</code>\nDaily Tasks: <code>{DT}</code>\nLast Bot Used: <code>{LAST_USED}</code>\nUser Session: <code>{USESS}</code>\nScreeshoot Mode: <code>{MEDIAINFO}</code>\nSave Code: <code>{SAVE_MODE}</code>\nPM Link: <code>{BOT_PM}</code>'''

    MIRROR = '''⚙️ Mirror Rituals 🪞\n\nRClone Key: <i>{RCLONE}</i>\nCallsign: <code>{MPREFIX}</code>\nEnding: <code>{MSUFFIX}</code>\nRename Spell: <code>{MREMNAME}</code>\nDestination: <i>{DDL_SERVER}</i>\nTeam Drive: <i>{TMODE}</i>\nTeam Strength: <i>{USERTD}</i>\nDaily Summon: <code>{DM}</code>'''

    LEECH = '''⚙️ Leech Settings ⚙️\n\nDaily Leech: <code>{DL}</code>\nType: <i>{LTYPE}</i>\nCustom Thumbnail: <i>{THUMB}</i>\nSplit Size: <code>{SPLIT_SIZE}</code>\nEqual Spilit: <i>{EQUAL_SPLIT}</i>\nMedia Group: <i>{MEDIA_GROUP}</i>\nLeech Captions: <code>{LCAPTION}</code>\nPrefix: <code>{LPREFIX}</code>\nLeech Suffix: <code>{LSUFFIX}</code>\nLeech Dump: <code>{LDUMP}</code>\nLeech ReName: <code>{LREMNAME}</code>'''

    
