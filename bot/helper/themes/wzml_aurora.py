
#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🌌 ✦ Repo ✦' # github
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X' # Github link
    ST_BN2_NAME = '📢 ✦ Updates ✦' # update channel name
    ST_BN2_URL = 'https://t.me/NxLeech' # update channel link
    ST_MSG = '''✨ 🚀 Mirror Magic ✨\n\nTurn links 🔗, files 📁, and torrents 磁 into Google Drive clouds ☁️, Rclone hubs ⚙️, Telegram stashes 📦, or DDL drops ⚡ with a tap!\n\nTap <code>{help_command}</code> to unlock bot powers 🧙!''' #Start msg
    ST_BOTPM = '''✉️ Secret Bot Cave 🦇! Drop links or files here 🤫!''' # PM MSG
    ST_UNAUTH = '''🚫 Zone locked 🔒! Deploy your own WZML-X mirror bot 🧙.''' # Unauthorized User
    OWN_TOKEN_GENERATE = '''⚠️ Oops! Token Thief! 🦹 Get your own ✨!''' # Own token request
    USED_TOKEN = '''⚠️ Uh-oh! Token used 💔! Make a fresh ✨!''' # Used token
    LOGGED_PASSWORD = '''🔑 Password locked! 🤖 Secure access granted ✅!''' # password protect
    ACTIVATE_BUTTON = '✨ Activate Token 🔑' #Activate button text
    TOKEN_MSG = '''🔑 ✨ Temp Token Alert ✨🔑\n\nCode: <code>{token}</code>\nTime Left: {validity}''' # token

    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅ Activated ✅' # Activated msg
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '🔑 Logged In! 😎' #Logged in msg
    INVALID_PASS = '⛔ Whoops! Wrong password 😫!' # Wrong pass
    PASS_LOGGED = '🔑 Power user unlocked! 💪!' #Logged
    LOGIN_USED = '🔑 Code entry: <code>/cmd [password]</code>' #Login instruction
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📜 Scroll the Log 📜' #log
    WEB_PASTE_BT = '🌐 Web Paste Wiz 🪄' #webpaste
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '🔰 Basic Info' # Basic info btn
    USER_BT = '👤 Team Members' #Team members
    MICS_BT = '⚙️ Tweak Tools' #Tweak tool
    O_S_BT = '👑 Boss Mode' #Boss mode
    CLOSE_BT = '❌ Exit Stage' #close bot
    HELP_HEADER = "🔥 Guide to Awesomeness 🔥\n\nTap a button to dive into each command's secrets! 🕵️" #help msg

    # async def stats(client, message):
    BOT_STATS = '''🚀 <b>Bot Brain Stats</b> 🧠\n\n⏱️ <b>Uptime:</b> {bot_uptime}\n\n📊 <b>Memory Zone</b> 🧠\n{ram_bar} {ram}%\n<b>Used:</b> {ram_u} | <b>Free:</b> {ram_f} | <b>Total:</b> {ram_t}\n\n🔀 <b>Swap Power</b> 🔀\n{swap_bar} {swap}%\n<b>Used:</b> {swap_u} | <b>Free:</b> {swap_f} | <b>Total:</b> {swap_t}\n\n💾 <b>Digital Stash</b> 💾\n{disk_bar} {disk}%\n<b>Read:</b> {disk_read}\n<b>Write:</b> {disk_write}\n<b>Used:</b> {disk_u} | <b>Free:</b> {disk_f} | <b>Total:</b> {disk_t}''' #bot stats

    SYS_STATS = '''⚙️ <b>Machine Room</b> ⚙️\n\n⏱️ <b>Uptime:</b> {os_uptime}\nℹ️ <b>OS Flavor:</b> {os_version}\n💻 <b>Architecture:</b> {os_arch}\n\n📡 <b>Signal Waves</b> 📡\n⬆️ <b>Upload:</b> {up_data}\n⬇️ <b>Download:</b> {dl_data}\n📤 <b>Sent:</b> {pkt_sent}k\n📥 <b>Received:</b> {pkt_recv}k\n⚡ <b>Total Traffic:</b> {tl_data}\n\n🔥 <b>Core Power</b> 🔥\n{cpu_bar} {cpu}%\n<b>Clock Speed:</b> {cpu_freq}\n<b>Load:</b> {sys_load}\n🔥 <b>Real Cores:</b> {p_core} | 💻 <b>Virtual Cores:</b> {v_core}\n<b>Total Cores:</b> {total_core}\n<b>Usable:</b> {cpu_use}''' # system stats

    REPO_STATS = '''📚 <b>Bot Origin Story</b> 📚\n\n✨ <b>Last Mod:</b> {last_commit}\n🤖 <b>Bot Build:</b> {bot_version}\n🔥 <b>Newest Drop:</b> {lat_version}\n📜 <b>Patch Notes:</b> {commit_details}\n\n🔮 <b>Dev's Message:</b> <code>{remarks}</code>''' #repo stats

    BOT_LIMITS = '''🛑 <b>Bot Restraints</b> ⛓️\n\n🔗 <b>Direct Snag:</b> {DL} GB\n🌀 <b>Torrent Takedown:</b> {TL} GB\n☁️ <b>Cloud Cage:</b> {GL} GB\n🎬 <b>YouTube Rip:</b> {YL} GB\n🎶 <b>Playlist Parade:</b> {PL}\n💾 <b>Mega Hoard:</b> {ML} GB\n🔄 <b>Clone Warp:</b> {CL} GB\n<b>Leach Lagoon:</b> {LL} GB\n\n🔑 <b>Key Life:</b> {TV}\n⏰ <b>User Wait:</b> {UTI} / task\n👯 <b>User Tasks:</b> {UT}\n🤖 <b>Bot Brigade:</b> {BT}''' #bot limits

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '🔄 Bot Rebooting... 🚀' #restart
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''✅ <b>Back Online</b> ✅\n\n📅 <b>Date:</b> {date}\n⏰ <b>Time:</b> {time}\n🌍 <b>Time Zone:</b> {timz}\n🤖 <b>Version:</b> {version}''' #restart success
    RESTARTED = '''🔄 Bot is back! 🔥''' #restarted
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '⏳ Bot is Feeling Pulse... 📡' #ping
    PING_VALUE = '⚡ <b>Pong!</b> ⚡\n<code>{value} ms</code>' #ping value

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """🚀 <b>Quest Start</b> 🚀\n\n⚙️ <b>Mode:</b> {Mode}\n👤 <b>Captain:</b> {Tag}""" # download start
    LINKS_SOURCE = """🔗 <b>Source Found</b> 🔗\n\n📅 <b>Looted On:</b> {On}\n\n{Source}""" # Source link

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➡️ <b>Transfer Beam Engaged!</b> 💫\n\n🔗 <b>Link:</b> <a href='{msg_link}'>Warp Here</a>" # pm transfer
    L_LOG_START = "➡️ <b>Stealing Speed</b> 💨\n\n👤 <b>Shadow Agent:</b> {mention} ( #ID{uid} )\n🔗 <b>Target:</b> <a href='{msg_link}'>Lock On</a>" # leech

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = '📦 <b>Loot Drop</b> 📦\n\n<b>{Name}</b>\n\n' #drop msg
    SIZE = '<b>Size:</b> {Size}\n' #size
    ELAPSE = '<b>Time:</b> {Time}\n' #elapse time
    MODE = '<b>Mode:</b> {Mode}\n' #Mode

    # ----- LEECH -------
    L_TOTAL_FILES = '<b>All Drops:</b> {Files}\n' #ALL drops msg
    L_CORRUPTED_FILES = '<b>Shattered Drops:</b> {Corrupt}\n' #corrupted drop msg
    L_CC = '<b>Sourced By:</b> {Tag}\n\n' #drop sourced by msg
    PM_BOT_MSG = '➡️ <b>Stash Sent!</b> 📦!' #pm stash sent
    L_BOT_MSG = '➡️ <b>Secret Stash to Bot PM!</b> ✉️' #secret stash
    L_LL_MSG = '➡️ <b>Stash Map Available!</b> 🗺️\n' #stash map

    # ----- MIRROR -------
    M_TYPE = '<b>Content Type:</b> {Mimetype}\n' #content
    M_SUBFOLD = '<b>Sub Hideouts:</b> {Folder}\n' #sub folder
    TOTAL_FILES = '<b>Total Drops:</b> {Files}\n' # Total drop
    RCPATH = '<b>Stash Path:</b> <code>{RCpath}</code>\n' #path
    M_CC = '<b>Stash Handled By:</b> {Tag}\n\n' #Stash handled
    M_BOT_MSG = '➡️ <b>Cloud keys Dispatched!</b> 🔑' #key dispatch

    # ----- BUTTONS -------
    CLOUD_LINK = '☁️ Cloud Portal' #cloud portal button
    SAVE_MSG = '💾 Save Powerup' #save power up
    RCLONE_LINK = '⚙️ RClone Engine' # rclone engine
    DDL_LINK = '⚡ {Serv} Warp' # ddl warp
    SOURCE_URL = '🔗 Source Link' # source link
    INDEX_LINK_F = '📁 Index Zone' # index zone
    INDEX_LINK_D = '⚠️ Index Hazard' #index hazard
    VIEW_LINK = '👁️ Glimpse Loot' # Glimpse
    CHECK_PM = '💬 PM Inventory' # pm inventory
    CHECK_LL = '📝 Loot Logs' #loot logs
    MEDIAINFO_LINK = 'ℹ️ Loot Intel' #loot intel
    SCREENSHOTS = '🖼️ Visions' #Vision

    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME = '📦 ✦ {Name} ✦ 📦' #Name

    #####---------PROGRESSIVE STATUS-------
    BAR = '\n{Bar} ✦' # Progress bar
    PROCESSED = '\n✅ Crafted: {Processed}' #crafted
    STATUS = '\n📶 Signal: <a href="{Url}">{Status}</a>' # url
    ETA = ' | ⏰ Soon™: {Eta}' # eta
    SPEED = '\n💨 Velocity: {Speed}' #speed
    ELAPSED = ' | ⏱️ Time Warp: {Elapsed}' #elapse
    ENGINE = '\n⚙️ Core: {Engine}' # engine
    STA_MODE = '\n🕹️ Style: {Mode}' #mode
    SEEDERS = '\n🌱 Helpers: {Seeders} | ' # seeder
    LEECHERS = '🦹 Looters: {Leechers}' #leecher

    ####--------SEEDING----------
    SEED_SIZE = '\n📦 Weight: {Size}' #size
    SEED_SPEED = '\n⚡ Burst: {Speed} | ' # speed
    UPLOADED = '⬆️ Airborne: {Upload}' #upload
    RATIO = '\n♻️ Cycle: {Ratio} | ' #ratio
    TIME = '⏰ Duration: {Time}' # duration
    SEED_ENGINE = '\n⚙️ Heart: {Engine}' #seed engine

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = '\n📦 Weight: {Size}' #size
    NON_ENGINE = '\n⚙️ Core: {Engine}' #engine

    ####--------OVERALL MSG FOOTER----------
    USER = '\n👤 Hero: <code>{User}</code> | ' #User id
    ID = '🆔 Tag: <code>{Id}</code>' # Tag id
    BTSEL = '\n🕹️ Pick: {Btsel}' # btsel
    CANCEL = '\n🚫 End Quest: {Cancel}\n\n' #cancel

    ####------FOOTER--------
    FOOTER = '🤖 Bot Pulse 🤖\n' #Bot pulse
    TASKS = '📌 Quests: {Tasks}\n' #task
    BOT_TASKS = '📌 Quests: {Tasks}/{Ttask} | 📝 Free Slots: {Free}\n' #freetask
    Cpu = '💻 CPU Surge: {cpu}% | ' #cpu surge
    FREE = '💾 Free RAM: {free} [{free_p}%]' #freeram
    Ram = '\n🧠 RAM Flow: {ram}% | ' #ramflow
    uptime = '⬆️ Online Time: {uptime}' #up time
    DL = '\n⬇️ Incoming: {DL}/s | ' # download
    UL = '⬆️ Outgoing: {UL}/s' #upload

    ###--------BUTTONS-------
    PREVIOUS = '⏪' #previou
    REFRESH = '🔄 Recharge\n{Page}' #recharge
    NEXT = '⏩' #next

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'Portal Blocked!\nRepeat portal detected.\n{content} portals found:' #duplicate portal

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = 'Counting Portals... 💫' # Counting portals
    COUNT_NAME = '📦 ✦ {COUNT_NAME} ✦ 📦\n\n' # Count name
    COUNT_SIZE = '<b>Size:</b> {COUNT_SIZE}\n' #countsize
    COUNT_TYPE = '<b>Essence:</b> {COUNT_TYPE}\n' # count essence
    COUNT_SUB = '<b>Sub-Portals:</b> {COUNT_SUB}\n' # Sub portal
    COUNT_FILE = '<b>Total Portals:</b> {COUNT_FILE}\n' # Total Portal
    COUNT_CC = '<b>Guide:</b> {COUNT_CC}\n' #cc

    # LIST ---> gd_list.py
    LIST_SEARCHING = '🔎 Scanning for <i>{NAME}</i>' # Searching for
    LIST_FOUND = '✅ <b>Portal Found!</b> {NO} entries for <i>{NAME}</i>' # Portal found
    LIST_NOT_FOUND = '🚫 No Trace Found for <i>{NAME}</i>' # Not found

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''🚫 <b>No active quests!</b>\n\n🤖 <b>Bot Systems</b> 🤖\n💻 CPU: {cpu}% | 💾 Free RAM: {free} [{free_p}%]\n🧠 RAM: {ram} | ⬆️ Run Time: {uptime}''' #not active download

    # USER Setting --> user_setting.py
    USER_SETTING = '''⚙️ <b>Hero Profile</b> ⚙️\n\n<b>Name:</b> {NAME} ( <code>{ID}</code> )\n<b>Alias:</b> {USERNAME}\n<b>World Region:</b> {DC}\n<b>Spoken Tongue:</b> {LANG}\n\nℹ️ <b>Secret Codes:</b>\n-s or -set: Direct Imprint''' #user setting

    UNIVERSAL = '''⚙️ <b>Global Powers</b> ⚙️\n\nYouTube Unlock: <code>{YT}</code>\nDaily Rituals: <code>{DT}</code>\nLast Channel: <code>{LAST_USED}</code>\nSession Seal: <code>{USESS}</code>\nVision Mode: <code>{MEDIAINFO}</code>\nSave Code: <code>{SAVE_MODE}</code>\nPM Link: <code>{BOT_PM}</code>''' #universal

    MIRROR = '''⚙️ <b>Mirror Rituals</b> 🪞\n\nRClone Key: <i>{RCLONE}</i>\nCallsign: <code>{MPREFIX}</code>\nEnding: <code>{MSUFFIX}</code>\nRename Spell: <code>{MREMNAME}</code>\nDestination: <i>{DDL_SERVER}</i>\nTeam Drive: <i>{TMODE}</i>\nTeam Strength: <i>{USERTD}</i>\nDaily Summon: <code>{DM}</code>''' #mirror

    LEECH = '''⚙️ <b>Steal Settings</b> ⚙️\n\nDaily Raids: <code>{DL}</code>\nType: <i>{LTYPE}</i>\nImage Sigil: <i>{THUMB}</i>\nSplit Chunk: <code>{SPLIT_SIZE}</code>\nEqual Share: <i>{EQUAL_SPLIT}</i>\nMedia Group: <i>{MEDIA_GROUP}</i>\nCrafting: <code>{LCAPTION}</code>\nPrefix: <code>{LPREFIX}</code>\nEnding: <code>{LSUFFIX}</code>\nBurial Site: <code>{LDUMP}</code>\nAlter Name: <code>{LREMNAME}</code>''' #leech
