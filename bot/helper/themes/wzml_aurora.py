
#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🌟 Repo'  # Emojis add visual appeal
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = '📢 Updates'
    ST_BN2_URL = 'https://t.me/WZML_X'
    ST_MSG = '''✨ <i>🚀 Unleash the power of mirroring with this bot! 🪞 Mirror links, files, and torrents to Google Drive, rclone clouds, Telegram, or DDL servers.</i>
    <b>Type {help_command} to explore available commands 🤖</b>'''
    ST_BOTPM = '''✉️ <i>🤖 I'm ready to handle your files and links privately. Start using me...</i>'''
    ST_UNAUTH = '''🚫 <i>🔒 Unauthorized user! Deploy your own WZML-X Mirror-Leech bot.</i>'''
    OWN_TOKEN_GENERATE = '''⚠️ <b>🔑 This temporary token doesn't belong to you!</b>\n\n<i>Please generate your own token.</i>'''
    USED_TOKEN = '''⚠️ <b>🔑 This temporary token has already been used!</b>\n\n<i>Please generate a new one.</i>'''
    LOGGED_PASSWORD = '''🔑 <b>🤖 Bot is already logged in via password.</b>\n\n<i>No need to accept temporary tokens.</i>'''
    ACTIVATE_BUTTON = '✨ Activate Temporary Token 🔑'
    TOKEN_MSG = '''<b><u>✨ 🔑 Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '🔑 <b>🤖 Already logged in!</b>'
    INVALID_PASS = '⛔ <b>🔑 Invalid Password!</b>\n\n<i>Please provide the correct password.</i>'
    PASS_LOGGED = '🔑 <b>✅ Permanent Login Successful!</b>'
    LOGIN_USED = '🔑 <b>🤖 Bot Login Usage:</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📜 Log Display 📊'
    WEB_PASTE_BT = '🌐 Web Paste (SB) 📝'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '🔰 Basic ℹ️'
    USER_BT = '👤 Users 👥'
    MICS_BT = '⚙️ Mics 🛠️'
    O_S_BT = '👑 Owner & Sudos 🛡️'
    CLOSE_BT = '❌ Close 🚪'
    HELP_HEADER = "✨ <b><i>🤖 Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor details. ℹ️</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''📊 <b><i>🤖 BOT STATISTICS:</i></b>
├ ⬆️ Bot Uptime: {bot_uptime}

┌ 🧠 <b><i>RAM (MEMORY):</i></b>
│ 🚦 {ram_bar} {ram}%
├ 💾 U: {ram_u} | 📝 F: {ram_f} | 🧮 T: {ram_t}

┌ 💽 <b><i>SWAP MEMORY:</i></b>
│ 🚦 {swap_bar} {swap}%
├ 💾 U: {swap_u} | 📝 F: {swap_f} | 🧮 T: {swap_t}

┌ 💾 <b><i>DISK:</i></b>
│ 🚦 {disk_bar} {disk}%
│ ⬇️ Total Disk Read: {disk_read}
│ ⬆️ Total Disk Write: {disk_write}
├ 💾 U: {disk_u} | 📝 F: {disk_f} | 🧮 T: {disk_t}
    
    '''
    SYS_STATS = '''⚙️ <b><i>🖥️ OS SYSTEM:</i></b>
│ ⬆️ OS Uptime: {os_uptime}
│ ℹ️ OS Version: {os_version}
├ 💻 OS Arch: {os_arch}

⚙️ <b><i>🌐 NETWORK STATS:</i></b>
│ ⬆️ Upload Data: {up_data}
│ ⬇️ Download Data: {dl_data}
│ 📤 Pkts Sent: {pkt_sent}k
│ 📥 Pkts Received: {pkt_recv}k
├ 🧮 Total I/O Data: {tl_data}

┌ ⚙️ <b>CPU:</b>
│ 🚦 {cpu_bar} {cpu}%
│ ℹ️ CPU Frequency: {cpu_freq}
│ 📊 System Avg Load: {sys_load}
│ 💾 P-Core(s): {p_core} | 📝 V-Core(s): {v_core}
├ 🧮 Total Core(s): {total_core}
├ 💻 Usable CPU(s): {cpu_use}
    '''
    REPO_STATS = '''🗂️ <b><i>📦 REPO STATISTICS:</i></b>
│ ⬆️ Bot Updated: {last_commit}
│ ℹ️ Current Version: {bot_version}
│ 🆕 Latest Version: {lat_version}
├ 📝 Last ChangeLog: {commit_details}

🗂️ <b>REMARKS:</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''🛑 <b><i>🤖 BOT LIMITATIONS:</i></b>
│ ⬇️ Direct Limit: {DL} GB
│  torrent Limit: {TL} GB
│ ☁️ GDrive Limit: {GL} GB
│ 🎬 YT-DLP Limit: {YL} GB
│ 🎶 Playlist Limit: {PL}
│ 💾 Mega Limit: {ML} GB
│ 🔄 Clone Limit: {CL} GB
├ leech Limit: {LL} GB

│ 🔑 Token Validity: {TV}
│ ⏰ User Time Limit: {UTI} / task
│ 👥 User Parallel Tasks: {UT}
├ 🤖 Bot Parallel Tasks: {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '🔄 <i>🤖 Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''🔄 <b><i>✅ Restarted Successfully!</i></b>
│ 📅 Date: {date}
│ ⏱️ Time: {time}
│ 🌍 TimeZone: {timz}
├ ℹ️ Version: {version}'''
    RESTARTED = '''🔄 <b><i>🤖 Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '⏳ <i>📡 Starting Ping...</i>'
    PING_VALUE = '<b>📡 Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>🚀 Task Started</i></b>
│ ⚙️ Mode: {Mode}
├ 👤 By: {Tag}\n\n"""
    LINKS_SOURCE = """➡️ <b>🔗 Source:</b>
├ 📅 Added On: {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➡️ <b><u>🚀 Task Started:</u></b>\n│\n├ 🔗 Link: <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➡️ <b><u> leech Started:</u></b>\n│\n│ 👤 User: {mention} ( #ID{uid} )\n├ 🔗 Source: <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>📦 {Name}</i></b>\n│\n'
    SIZE =                  '│ 📏 Size: {Size}\n'
    ELAPSE =                '│ ⏰ Elapsed: {Time}\n'
    MODE =                  '│ ⚙️ Mode: {Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '│ 🔢 Total Files: {Files}\n'
    L_CORRUPTED_FILES =     '│ 💔 Corrupted Files: {Corrupt}\n'
    L_CC =                  '├ 👤 By: {Tag}\n\n'
    PM_BOT_MSG =            '➡️ <b><i>📤 File(s) have been sent above</i></b>'
    L_BOT_MSG =             '➡️ <b><i>🤖 File(s) have been sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➡️ <b><i>🔗 File(s) have been sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '│ ℹ️ Type: {Mimetype}\n'
    M_SUBFOLD =             '│ 📂 SubFolders: {Folder}\n'
    TOTAL_FILES =           '│ 🔢 Files: {Files}\n'
    RCPATH =                '│ ℹ️ Path: <code>{RCpath}</code>\n'
    M_CC =                  '├ 👤 By: {Tag}\n\n'
    M_BOT_MSG =             '➡️ <b><i>🔗 Link(s) have been sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '💾 Save Message'
    RCLONE_LINK =     '⚙️ RClone Link'
    DDL_LINK =        '⚡ {Serv} Link'
    SOURCE_URL =      '🔗 Source Link'
    INDEX_LINK_F =    '📁 Index Link'
    INDEX_LINK_D =    '⚠️ Index Link'
    VIEW_LINK =       '👁️ View Link'
    CHECK_PM =        '💬 View in Bot PM'
    CHECK_LL =        '📝 View in Links Log'
    MEDIAINFO_LINK =  'ℹ️ MediaInfo'
    SCREENSHOTS =     '🖼️ ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>📦 {Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n│ 🚦 {Bar}'  # Added emoji here
    PROCESSED =         '\n│ ✅ Processed: {Processed}'
    STATUS =            '\n│ 📶 Status: <a href="{Url}">{Status}</a>'  # Changed emoji
    ETA =                                                ' | ⏳ ETA: {Eta}'
    SPEED =             '\n│ 🚀 Speed: {Speed}'  # Emoji for speed
    ELAPSED =                                     ' | ⏱️ Elapsed: {Elapsed}'
    ENGINE =            '\n│ ⚙️ Engine: {Engine}'  # Emoji for engine
    STA_MODE =          '\n│ ⚙️ Mode: {Mode}'
    SEEDERS =           '\n│ 🌱 Seeders: {Seeders} | '
    LEECHERS =                                           '🦹 Leechers: {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n│ 📦 Size: {Size}'
    SEED_SPEED =     '\n│ ⚡ Speed: {Speed} | '
    UPLOADED =                                     '⬆️ Uploaded: {Upload}'
    RATIO =          '\n│ ♻️ Ratio: {Ratio} | '
    TIME =                                         '⏰ Time: {Time}'
    SEED_ENGINE =    '\n│ ⚙️ Engine: {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n│ 📦 Size: {Size}'
    NON_ENGINE =     '\n│ ⚙️ Engine: {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n│ 👤 User: <code>{User}</code> | '
    ID =                                                        '🆔 ID: <code>{Id}</code>'
    BTSEL =          '\n│ 🕹️ Select: {Btsel}'
    CANCEL =         '\n└ 🚫 {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '📊 <b><i>🤖 Bot Stats</i></b>\n' # changed emoji
    TASKS =  '│ 📌 Tasks: {Tasks}\n'
    BOT_TASKS = '│ 📌 Tasks: {Tasks}/{Ttask} | 📝 AVL: {Free}\n'
    Cpu = '│ 💻 CPU: {cpu}% | '
    FREE =                      '💾 F: {free} [{free_p}%]'
    Ram = '\n│ 🧠 RAM: {ram}% | '
    uptime =                     '⬆️ UPTIME: {uptime}'
    DL = '\n└ ⬇️ DL: {DL}/s | ' # Download
    UL =                        '⬆️ UL: {UL}/s' #upload

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '🔄 Refresh\n{Page}'
    NEXT = '⏩'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>📦 {COUNT_NAME}</i></b>\n│\n'
    COUNT_SIZE = '│ 📏 Size: {COUNT_SIZE}\n'
    COUNT_TYPE = '│ ℹ️ Type: {COUNT_TYPE}\n'
    COUNT_SUB =  '│ 📂 SubFolders: {COUNT_SUB}\n'
    COUNT_FILE = '│ 🔢 Files: {COUNT_FILE}\n'
    COUNT_CC =   '├ 👤 By: {COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔎 Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>✅ Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = '🚫 No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>🚫 No Active Downloads!</i>
    
📊 <b><i>🤖 Bot Stats</i></b>
│ 💻 CPU: {cpu}% | 💾 F: {free} [{free_p}%]
└ 🧠 RAM: {ram} | ⬆️ UPTIME: {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py
    USER_SETTING = '''⚙️ <b><u>👤 User Settings:</u></b>
        
┌ 📝 Name: {NAME} ( <code>{ID}</code> )
│ ℹ️ Username: {USERNAME}
│ 🌍 Telegram DC: {DC}
└ 🏳️ Language: {LANG}

➡️ <u><b>ℹ️ Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''⚙️ <b><u>🌐 Universal Settings: {NAME}</u></b>

┌ 🎬 <b>YT-DLP Options:</b> <b><code>{YT}</code></b>
│ 📅 <b>Daily Tasks:</b> <code>{DT}</code> per day
│ ⏰ <b>Last Bot Used:</b> <code>{LAST_USED}</code>
│ 🔑 <b>User Session:</b> <code>{USESS}</code>
│ ℹ️ <b>MediaInfo Mode:</b> <code>{MEDIAINFO}</code>
│ 💾 <b>Save Mode:</b> <code>{SAVE_MODE}</code>
└ 💬 <b>User Bot PM:</b> <code>{BOT_PM}</code>'''

    MIRROR = '''⚙️ <b><u>🪞 Mirror/Clone Settings: {NAME}</u></b>

┌ ⚙️ <b>RClone Config:</b> <i>{RCLONE}</i>
│ ℹ️ <b>Mirror Prefix:</b> <code>{MPREFIX}</code>
│ ℹ️ <b>Mirror Suffix:</b> <code>{MSUFFIX}</code>
│ ℹ️ <b>Mirror Remname:</b> <code>{MREMNAME}</code>
│ ⚡ <b>DDL Server(s):</b> <i>{DDL_SERVER}</i>
│ 🔑 <b>User TD Mode:</b> <i>{TMODE}</i>
│ 🧮 <b>Total User TD(s):</b> <i>{USERTD}</i>
└ 📅 <b>Daily Mirror:</b> <code>{DM}</code> per day'''

    LEECH = '''⚙️ <b><u> leech Settings for {NAME}</u></b>

┌ 📅 <b>Daily leech:</b> <code>{DL}</code> per day
│ ℹ️ <b>leech Type:</b> <i>{LTYPE}</i>
│ 🖼️ <b>Custom Thumbnail:</b> <i>{THUMB}</i>
│ 💾 <b>leech Split Size:</b> <code>{SPLIT_SIZE}</code>
│ ⚖️ <b>Equal Splits:</b> <i>{EQUAL_SPLIT}</i>
│ 🎬 <b>Media Group:</b> <i>{MEDIA_GROUP}</i>
│ 📝 <b>leech Caption:</b> <code>{LCAPTION}</code>
│ ℹ️ <b>leech Prefix:</b> <code>{LPREFIX}</code>
│ ℹ️ <b>leech Suffix:</b> <code>{LSUFFIX}</code>
│ 🗑️ <b>leech Dumps:</b> <code>{LDUMP}</code>
└ ℹ️ <b>leech Remname:</b> <code>{LREMNAME}</code>'''

