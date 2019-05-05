# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

#zhoe = LINE()
zhoe = LINE("EE89DBkpY8BH35Vc518b.qyorTSk1T2V1niU7QSKXcW.qmQcqFbDF8rJ9D6rkANUnVh2ucNFW6dq+G9ABaOb6Dk=")

zhoeMid = zhoe.profile.mid
zhoeProfile = zhoe.getProfile()
zhoeSettings = zhoe.getSettings()
zhoePoll = OEPoll(zhoe)
botStart = time.time()
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)

print ("╔═════════════════════════\n║╔════════════════════════\n║║♻ Chalyyzhu login\n║╚════════════════════════\n╚═════════════════════════")

#==============================SETING====================================

msg_dict = {}


wait = {
    "autoAdd": True,
    "limit": 30,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": False,
    "autoResponPc": False,
    "autoJoinTicket": False,
    "Leave": True,
    "Welcome": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "kickMention":False,
    "lang":"JP",
    "public": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
wait["myProfile"]["displayName"] = zhoeProfile.displayName
wait["myProfile"]["statusMessage"] = zhoeProfile.statusMessage
wait["myProfile"]["pictureStatus"] = zhoeProfile.pictureStatus
coverId = zhoe.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

#====kumpulan DEF ==============================================================

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    zhoe.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                zhoe.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    zhoe.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "╭════════╬🔎╬════════╮" + "\n" + \
                    "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                    "╰════════╬🔎╬════════╯" + "\n" + \
                    "╭════════╬🔎╬════════╮" + "\n" + \
                    "                      ☡ HELP MESAGE ☡" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Help " + "\n" + \
                    "║♻ " + key + "Tts " + "\n" + \
                    "║♻ " + key + "Translate " + "\n" + \
                    "║♻ " + key + "Token " + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                            ♳ STATUS ♳" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Restart" + "\n" + \
                    "║♻ " + key + "Runtime" + "\n" + \
                    "║♻ " + key + "Sp" + "\n" + \
                    "║♻ " + key + "Speed" + "\n" + \
                    "║♻ " + key + "Status" + "\n" + \
                    "║♻ Mkey" + "\n" + \
                    "║♻ Setkey「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                       🛠    SETTINGS   🛠" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Autoadd「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autojoin「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autojointicket「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autoleave「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autoread「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autorespon「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Autoresponpc「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Welcome「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Responleave「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Checkcontact「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Checkpost「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Checksticker「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Unsendchat「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                              🔞 SELF 🔞" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Backupprofile" + "\n" + \
                    "║♻ " + key + "Changebio:「ǫᴜᴇʀʏ」" + "\n" + \
                    "║♻ " + key + "Changename:「ǫᴜᴇʀʏ」" + "\n" + \
                    "║♻ " + key + "Cloneprofile「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Changepictureprofile" + "\n" + \
                    "║♻ " + key + "Me" + "\n" + \
                    "║♻ " + key + "Mymid" + "\n" + \
                    "║♻ " + key + "Myname" + "\n" + \
                    "║♻ " + key + "Mybio" + "\n" + \
                    "║♻ " + key + "Mypicture" + "\n" + \
                    "║♻ " + key + "Myvideoprofile" + "\n" + \
                    "║♻ " + key + "Mycover" + "\n" + \
                    "║♻ " + key + "Restoreprofile" + "\n" + \
                    "║♻ " + key + "Stealcontact「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealmid「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealname「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealbio「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealpicture「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealvideoprofile「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Stealcover「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                         💝   SPECIAL   💝" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Lurking" + "\n" + \
                    "║♻ " + key + "Lurking「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
                    "║♻ " + key + "Mention" + "\n" + \
                    "║♻ " + key + "Mimic「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Mimicadd「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Mimicdel「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Mimiclist" + "\n" + \
                    "║♻ " + key + "Sider「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Tagall" + "\n" + \
                    "║♻ " + key + "Public「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                            👥   GROUP   👥" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Changegrouppicture" + "\n" + \
                    "║♻ " + key + "Groupcreator" + "\n" + \
                    "║♻ " + key + "Groupid" + "\n" + \
                    "║♻ " + key + "Groupname" + "\n" + \
                    "║♻ " + key + "Grouppicture" + "\n" + \
                    "║♻ " + key + "Groupticket" + "\n" + \
                    "║♻ " + key + "Groupticket「ᴏɴ/ᴏғғ」" + "\n" + \
                    "║♻ " + key + "Groupmemberlist" + "\n" + \
                    "║♻ " + key + "Groupinfo" + "\n" + \
                    "║♻ " + key + "Grouplist" + "\n" + \
                    "║♻ " + key + "Invitegc「ᴀᴍᴏᴜɴᴛ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                           🎧   MEDIA   🎧" + "\n" + \
                    "╭═══════════════════╮" + "\n" + \
                    "║♻ " + key + "Checkdate「ᴅᴀᴛᴇ」" + "\n" + \
                    "║♻ " + key + "Checklocation「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Checkpraytime「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Checkwheater「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "║♻ " + key + "Checkwebsite「ᴜʀʟ」" + "\n" + \
                    "║♻ " + key + "Instainfo 「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
                    "║♻ " + key + "image 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "║♻ " + key + "liric 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "║♻ " + key + "music 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "║♻ " + key + "youtube「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    " ☛  ʙʏ : Zhoe" + "\n" + \
                    "╰════════╬♞╬════════╯" + "\n" + \
                    "╭════════╬♞╬════════╮" + "\n" + \
                    "                      🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                    "╰════════╬♞╬════════╯"
    return helpMessage

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬🔎╬════════╯" + "\n" + \
                        "╭════════╬🔎╬════════╮" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╭═══════════════════╮ " + "\n" + \
                        "║♻ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "║♻ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "║♻ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "║♻ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "║♻ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "║♻ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "║♻ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "║♻ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "║♻ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "║♻ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "║♻ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "║♻ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "║♻ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "║♻ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "║♻ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "║♻ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "║♻ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "║♻ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "║♻ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "║♻ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "║♻ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "║♻ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "║♻ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "║♻ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "║♻ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "║♻ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "║♻ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "║♻ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "║♻ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "☛  ʙʏ : Zhoe" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "   Contoh : Say id Chalyyzhu "

    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬🔎╬════════╯" + "\n" + \
                        "╭════════╬🔎╬════════╮" + "\n" + \
                        "             ◄]·🚩·ᴛʀᴀɴsʟᴀᴛᴇ·🚩·[►" + "\n" + \
                        "╭═══════════════════╮" + "\n" + \
                        "║♻ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "║♻ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "║♻ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "║♻ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "║♻ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "║♻ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "║♻ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "║♻ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "║♻ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "║♻ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "║♻ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "║♻ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "║♻ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "║♻ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "║♻ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "║♻ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "║♻ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "║♻ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "║♻ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "║♻ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "║♻ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "║♻ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "║♻ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "║♻ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "║♻ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "║♻ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "║♻ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "║♻ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "║♻ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "║♻ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "║♻ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "║♻ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "║♻ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "║♻ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "║♻ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "║♻ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "║♻ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "║♻ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "║♻ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "║♻ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "║♻ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "║♻ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "║♻ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "║♻ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "║♻ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "║♻ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "║♻ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "║♻ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "║♻ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "║♻ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "║♻ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "║♻ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "║♻ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "║♻ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "║♻ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "║♻ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "║♻ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "║♻ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "║♻ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "║♻ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "║♻ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "║♻ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "║♻ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "║♻ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "║♻ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "║♻ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "║♻ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "║♻ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "║♻ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "║♻ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "║♻ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "║♻ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "║♻ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        " ☛  ʙʏ : Zhoe" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        " Contoh : Tr-id Family "
    return helpTranslate
    
def helptoken():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpToken = "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬🔎╬════════╯" + "\n" + \
                        "╭════════╬🔎╬════════╮" + "\n" + \
                        "             ◄]·🚩·TOKEN GENERATOR·🚩·[►" + "\n" + \
                        "╭═══════════════════╮" + "\n" + \
                        "║♻ " + key + "Desktopwin" + "\n" + \
                        "║♻ " + key + "Desktopmac" + "\n" + \
                        "║♻ " + key + "Chromeos" + "\n" + \
                        "║♻ " + key + "Iosipadipad" + "\n" + \
                        "║♻ " + key + "Win10" + "\n" + \
                        "║♻ " + key + "Get token" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        " ☛  ʙʏ : Zhoe" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        " Gunakan dengan bijak"
    return helpToken
    
def helppublic():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpPublic = "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬🔎╬════════╯" + "\n" + \
                        "╭════════╬🔎╬════════╮" + "\n" + \
                        "                    ◄]·🚩·HELP PUBLIC·🚩·[►" + "\n" + \
                        "╭════════════════════╮" + "\n" + \
                        "║♻ " + key + "Help " + "\n" + \
                        "║♻ " + key + "Tts " + "\n" + \
                        "║♻ " + key + "Translate " + "\n" + \
                        "║♻ " + key + "Token " + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "                      ☡ HELP MESAGE ☡" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "╭═══════════════════╮" + "\n" + \
                        "║♻ " + key + "Mymid" + "\n" + \
                        "║♻ " + key + "Myname" + "\n" + \
                        "║♻ " + key + "Mybio" + "\n" + \
                        "║♻ " + key + "Mypicture" + "\n" + \
                        "║♻ " + key + "Myvideoprofile" + "\n" + \
                        "║♻ " + key + "Mycover" + "\n" + \
                        "║♻ " + key + "Me" + "\n" + \
                        "║♻ " + key + "Speed" + "\n" + \
                        "║♻ " + key + "Tagall" + "\n" + \
                        "║♻ " + key + "Crash" + "\n" + \
                        "║♻ " + key + "image 「sᴇᴀʀᴄʜ」" + "\n" + \
                        "║♻ " + key + "liric 「sᴇᴀʀᴄʜ」" + "\n" + \
                        "║♻ " + key + "music 「sᴇᴀʀᴄʜ」" + "\n" + \
                        "║♻ " + key + "youtube「sᴇᴀʀᴄʜ」" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        " ☛  ʙʏ : Zhoe" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        "╭════════╬♞╬════════╮" + "\n" + \
                        "                       🗡 cнαℓүүzнυ вσт 🗡" + "\n" + \
                        "╰════════╬♞╬════════╯" + "\n" + \
                        " Mode public EDITION"
    return helpPublic

def zhoeBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                zhoe.findAndAddContactsByMid(op.param1)
            zhoe.sendMessage(op.param1, "ʜᴀʟʟᴏ, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ \n「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n ʙʏ: \n cнαℓүүzнυ вσт \n 🚻🚺 ")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if zhoeMid in op.param3:
                if wait["autoJoin"] == True:
                    zhoe.acceptGroupInvitation(op.param1)
                dan = zhoe.getContact(op.param2)
                tgb = zhoe.getGroup(op.param1)
                sendMention(op.param1, "Hallo @!      , Tanks for invite ME. ".format(str(tgb.name)),[op.param2])
                zhoe.sendContact(op.param1, op.param2)
                zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                
        if op.type == 15:
            if wait["Leave"] == True:
            	dan = zhoe.getContact(op.param2)
            	tgb = zhoe.getGroup(op.param1)
            	sendMention(op.param1, "yah baperan nihh @!      , knapa ya dia meninggalkan  {} \n papayyy  ".format(str(tgb.name)),[op.param2])
            	zhoe.sendContact(op.param1, op.param2)
            	zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
            if wait["Welcome"] == True:
            	dan = zhoe.getContact(op.param2)
            	tgb = zhoe.getGroup(op.param1)
            	sendMention(op.param1, "hai@!         ,\n ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \n jangan lupa cek note \n jalan jalan nyari tikungan baru gih..!! ".format(str(tgb.name)),[op.param2])
            	zhoe.sendContact(op.param1, op.param2)
            	zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 22:
            if wait["leaveRoom"] == True:
                zhoe.leaveRoom(op.param1)

        if op.type == 24:
            if wait["leaveRoom"] == True:
                zhoe.leaveRoom(op.param1)

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != zhoe.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                zhoe.sendMessage(to, str(helpMessage))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                zhoe.sendMessage(to, str(helpTextToSpeech))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                zhoe.sendMessage(to, str(helpTranslate))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd == "token":
                                helpToken = helptoken()
                                zhoe.sendMessage(to, str(helpToken))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    zhoe.sendMessage(to, "🔪JANGAN ADA TYPO 🔪")
                                else:
                                    wait["keyCommand"] = str(key).lower()
                                    zhoe.sendMessage(to, "SUCCES CHANGE KEY 🔧 [ {} ]".format(str(key).lower()))
                            elif cmd == "sp":
                            	zhoe.sendMessage(to, "⏭ Loading...")
                            	sp = int(round(time.time() *1000))
                            	zhoe.sendMessage(to,"My speed : %sms" % (sp - op.createdTime))
                            elif cmd == "speed":
                            	start = time.time()
                            	zhoe.sendMessage(to, "⏭ Loading...")
                            	elapsed_time = time.time() - start
                            	zhoe.sendMessage(to, "My speed : %sms" % (elapsed_time))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                zhoe.sendMessage(to, "Runing in.. {}".format(str(runtime)))
                            elif cmd == "restart":
                                zhoe.sendMessage(to, "Bote have been Restart")
                                restartBot()
                            elif cmd == "about":
                                try:
                                	arr = []
                                	owner = "u0b24e20b11c94bda952e8a68601e4239"
                                	creator = zhoe.getContact(owner)
                                	contact = zhoe.getContact(zhoeMid)
                                	grouplist = zhoe.getGroupIdsJoined()
                                	contactlist = zhoe.getAllContactIds()
                                	blockedlist = zhoe.getBlockedContactIds()
                                	ret_ = "╔══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ʟɪɴᴇ : {}".format(contact.displayName)
                                	ret_ += "\n╠✪ ɢʀᴏᴜᴘ : {}".format(str(len(grouplist)))
                                	ret_ += "\n╠✪ ғʀɪᴇɴᴅ : {}".format(str(len(contactlist)))
                                	ret_ += "\n╠✪ ʙʟᴏᴄᴋᴇᴅ : {}".format(str(len(blockedlist)))
                                	ret_ += "\n╠══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ᴠᴇʀsɪᴏɴ : ᴘʀᴇᴍɪᴜᴍ sᴇʟғ ᴘʏз"
                                	ret_ += "\n╠✪ ᴄʀᴇᴀᴛᴏʀ : {}".format(creator.displayName)
                                	ret_ += "\n╚══[ ᴅᴏɴ'ᴛ ʙᴇ ʀᴇᴍᴀᴋᴇ 😝 ]"
                                	zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                                	zhoe.sendMessage(msg.to, str(ret_))
                                except Exception as e:
                                	zhoe.sendMessage(msg.to, str(e))
                                
#==================================================================
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "autoadd on":
                                wait["autoAdd"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ")
                            elif cmd == "autoadd off":
                                wait["autoAdd"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                            elif cmd == "autojoin on":
                                wait["autoJoin"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ")
                            elif cmd == "autojoin off":
                                wait["autoJoin"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ ᴏғғ")
                            elif cmd == "autoleave on":
                                wait["autoLeave"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ")
                            elif cmd == "autoleave off":
                                wait["autoLeave"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏғғ")
                            elif cmd == "autoresponpc on":
                                wait["autoResponPc"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏɴ")
                            elif cmd == "autoresponpc off":
                                wait["autoResponPc"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏғғ")
                            elif cmd == "autorespon on":
                                wait["autoRespon"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏɴ")
                            elif cmd == "welcome on":
                            		wait["Welcome"] = True
                            		zhoe.sendMessage(msg.to, "Respon WELCOME on")
                            elif cmd == "welcome off":
                            		wait["Welcome"] = False
                            		zhoe.sendMessage(msg.to, "Respon WELCOME off")
                            elif cmd == "responleave on":
                            		wait["Leave"] = True
                            		zhoe.sendMessage(msg.to, "Respon LEAVE on")
                            elif cmd == "responleave off":
                            		wait["Leave"] = False
                            		zhoe.sendMessage(msg.to, "Respon LEAVE off")
                            elif cmd == "autorespon off":
                                wait["autoRespon"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏғғ")
                            elif cmd == "autoread on":
                                wait["autoRead"] = True
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ")
                            elif cmd == "autoread off":
                                wait["autoRead"] = False
                                zhoe.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏғғ")
                            elif cmd == "autojointicket on":
                                wait["autoJoinTicket"] = True
                                zhoe.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏɴ")
                            elif cmd == "autoJoinTicket off":
                                wait["autoJoinTicket"] = False
                                zhoe.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏғғ")
                            elif cmd == "contact on":
                                wait["checkContact"] = True
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                            elif cmd == "contact off":
                                wait["checkContact"] = False
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")
                            elif cmd == "checkpost on":
                                wait["checkPost"] = True
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏɴ")
                            elif cmd == "checkpost off":
                                wait["checkPost"] = False
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏғғ")
                            elif cmd == "checksticker on":
                                wait["checkSticker"] = True
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏɴ")
                            elif cmd == "checksticker off":
                                wait["checkSticker"] = False
                                zhoe.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏғғ")
                            elif cmd == "unsendchat on":
                                wait["unsendMessage"] = True
                                zhoe.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ")
                            elif cmd == "unsendchat off":
                                wait["unsendMessage"] = False
                                zhoe.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ")
                            elif cmd == "public on":
                                wait["public"] = True
                                zhoe.sendMessage(to, "Mode publik ON")
                            elif cmd == "public off":
                                wait["public"] = False
                                zhoe.sendMessage(to, "Mode publik OFF")
                            elif cmd == "notag on":
                                wait["kickMention"] = True
                                zhoe.sendMessage(to, "☠️DANGER TAG KICK ON☠️")
                            elif cmd == "notag off":
                                wait["kickMention"] = False
                                zhoe.sendMessage(to, "KICK TAG OFF ✔")
                                
                            elif cmd == "status":
                                try:
                                    ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                                    if wait["Welcome"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] Respon WELCOME「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] Respon WELCOME「⚫」"
                                    if wait["Leave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] Respon LEAVE「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] Respon LEAVE 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                                    if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                                    if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                                    if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                                    if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                                    if wait["autoResponPc"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚫」"
                                    if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                                    if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                                    if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                                    if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                                    if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                                    ret_ += "\n╚═════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]═════╝"
                                    if wait["kickMention"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ☠️DANGER TAG KICK☠️「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] KICK TAG 「⚫」"
                                    zhoe.sendMessage(to, str(ret_))
                                    zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                                except Exception as e:
                                    zhoe.sendMessage(msg.to, str(e))
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "crash":
                                zhoe.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = zhoe.getProfile()
                                    profile.displayName = string
                                    zhoe.updateProfile(profile)
                                    zhoe.sendMessage(to,"ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = zhoe.getProfile()
                                    profile.statusMessage = string
                                    zhoe.updateProfile(profile)
                                    zhoe.sendMessage(to,"ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd == "me":
                                zhoe.sendContact(to, sender)
                            elif cmd == "mymid":
                                zhoe.sendMessage(to, "[ ᴍɪᴅ ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = zhoe.getContact(sender)
                                zhoe.sendMessage(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = zhoe.getContact(sender)
                                zhoe.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = zhoe.getContact(sender)
                                zhoe.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = zhoe.getContact(sender)
                                zhoe.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = zhoe.getProfileCoverURL(sender)          
                                path = str(channel)
                                zhoe.sendImageWithURL(to, path)
                            elif cmd.startswith ('invitegc '):
                            	if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    zhoe.sendMessage(to, "sᴜᴄᴄᴇs ɪɴᴠɪᴛᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ")
                                    for var in range(0,num):
                                        group = zhoe.getGroup(to)
                                        members = [mem.mid for mem in group.members]
                                        zhoe.inviteIntoGroupCall(to, contactIds=members)
#test spam inv
                            elif cmd.startswith ("cilok @"):
                            	tgb = text.replace("cilok @","")
                            	key = eval(msg.contentMetadata["MENTION"])
                            	mi = key["MENTIONEES"][0]["M"]
                            	dan = tgb.split(" ")
                            	namagrup = dan[1]
                            	jumlah = int(dan[2])
                            	grups = zhoe.groups
                            	zhoe.findAndAddContactsByMid(mi)
                            	if jumlah <= 1000:
                            		for var in range(0,jumlah):
                            			try:
                            				zhoe.createGroup(namagrup, [mi])
                            				for i in grups:
                            					grup = zhoe.getGroup(i)
                            					if grup.name == namagrup:
                            						zhoe.inviteIntoGroup(grup.id, [mi])
                            						zhoe.leaveGroup(grup.id)
                            				sendMention(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            			except Exception as Nigga:
                            				zhoe.sendMessage(to, str(Nigga))
                            	else:
                            		zhoe(to, "@! kebanyakan njer!!", [sender])


                            
                            
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = zhoe.getContact(ls)
                                        zhoe.cloneContactProfile(ls)
                                        zhoe.sendMessage(to, "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs : {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    zhoeProfile = zhoe.getProfile()
                                    zhoeProfile.displayName = str(wait["myProfile"]["displayName"])
                                    zhoeProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                    zhoeProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                    zhoe.updateProfileAttribute(8, zhoeProfile.pictureStatus)
                                    zhoe.updateProfile(zhoeProfile)
                                    coverId = str(wait["myProfile"]["coverId"])
                                    zhoe.updateProfileCoverById(coverId)
                                    zhoe.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                                except Exception as e:
                                    zhoe.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = zhoe.getProfile()
                                    wait["myProfile"]["displayName"] = str(profile.displayName)
                                    wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = zhoe.getProfileDetail()["result"]["objectId"]
                                    wait["myProfile"]["coverId"] = str(coverId)
                                    zhoe.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                                except Exception as e:
                                    zhoe.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    zhoe.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = zhoe.getContact(ls)
                                        zhoe.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = zhoe.getContact(ls)
                                        zhoe.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = zhoe.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        zhoe.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = zhoe.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        zhoe.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if zhoe != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = zhoe.getProfileCoverURL(ls)
                                            path = str(channel)
                                            zhoe.sendImageWithURL(to, str(path))
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == 'groupcreator':
                                group = zhoe.getGroup(to)
                                GS = group.creator.mid
                                zhoe.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = zhoe.getGroup(to)
                                zhoe.sendMessage(to, "[ɢʀᴏᴜᴘ ɪᴅ : : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = zhoe.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                zhoe.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = zhoe.getGroup(to)
                                zhoe.sendMessage(to, "[ɢʀᴏᴜᴘ ɴᴀᴍᴇ : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = zhoe.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = zhoe.reissueGroupTicket(to)
                                        zhoe.sendMessage(to, "[ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        zhoe.sendMessage(to, "ᴛʜᴇ ǫʀ ɢʀᴏᴜᴘ ɪs ɴᴏᴛ ᴏᴘᴇɴ ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ ɪᴛ ғɪʀsᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ {}openqr".format(str(wait["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = zhoe.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        zhoe.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                                    else:
                                        group.preventedJoinByTicket = False
                                        zhoe.updateGroup(group)
                                        zhoe.sendMessage(to, "sᴜᴄᴄᴇs ᴏᴘᴇɴ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = zhoe.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        zhoe.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                                    else:
                                        group.preventedJoinByTicket = True
                                        zhoe.updateGroup(group)
                                        zhoe.sendMessage(to, "sᴜᴄᴄᴇs ᴄʟᴏsᴇ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupinfo':
                                group = zhoe.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "ɴᴏᴛ ғᴏᴜɴᴅ"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏʟ'"
                                else:
                                    gQr = "ᴏᴘᴇɴ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(zhoe.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔════[ ·✪ɢʀᴏᴜᴘ ɪɴғᴏ✪· ]════╗"
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {}".format(str(group.name))
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɪᴅ : {}".format(group.id)
                                ret_ += "\n╠❂➣ ᴄʀᴇᴀᴛᴏʀ :  {}".format(str(gCreator))
                                ret_ += "\n╠❂➣ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n╠❂➣ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠❂➣ ǫʀ ɢʀᴏᴜᴘ : {}".format(gQr)
                                ret_ += "\n╠❂➣ ᴛɪᴄᴋᴇᴛ ɢʀᴏᴜᴘ : {}".format(gTicket)
                                ret_ += "\n╚═════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]═════╝"
                                zhoe.sendMessage(to, str(ret_))
                                zhoe.sendImageWithURL(to, path)
                            elif cmd == 'memberlist':
                                if msg.toType == 2:
                                    group = zhoe.getGroup(to)
                                    ret_ = "╔══[ ᴍᴇᴍʙᴇʀ  ʟɪsᴛ ]══✪"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(group.members)))
                                    zhoe.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = zhoe.groups
                                    ret_ = "╔═[ ✯ ɢʀᴏᴜᴘ  ʟɪsᴛ ✯ ]═✪"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = zhoe.getGroup(gid)
                                        ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(groups)))
                                    zhoe.sendMessage(to, str(ret_))
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "changepictureprofile":
                                wait["changePictureProfile"] = True
                                zhoe.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in wait["changeGroupPicture"]:
                                        wait["changeGroupPicture"].append(to)
                                    zhoe.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == 'tagall':
                                group = zhoe.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    zhoe.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    zhoe.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                                    

                            elif cmd == "cuy" or text.lower() == '☺':
                                   group = zhoe.getGroup(msg.to)
                                   nama = [contact.mid for contact in group.members]
                                   k = len(nama)//20
                                   for a in range(k+1):
                                       txt = u''
                                       s=0
                                       b=[]
                                       for i in group.members[a*20 : (a+1)*20]:
                                           b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                           s += 7
                                           txt += u'@Zero \n'
                                       zhoe.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                   
                            elif cmd == "sider on":
                            	try:
                            		del cctv['point'][msg.to]
                            		del cctv['sidermem'][msg.to]
                            		del cctv['cyduk'][msg.to]
                            	except:
                            		pass
                            	cctv['point'][msg.to] = msg.id
                            	cctv['sidermem'][msg.to] = ""
                            	cctv['cyduk'][msg.to]=True
                            	wait["Sider"] = True
                            	zhoe.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "sider off":
                            	if msg.to in cctv['point']:
                            		cctv['cyduk'][msg.to]=False
                            		wait["Sider"] = False
                            		zhoe.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏғғ")
                            	else:
                            		zhoe.sendMessage(msg.to,"sɪᴅᴇʀ ɴᴏᴛ sᴇᴛ")           
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    zhoe.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏɴ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    zhoe.sendMessage(receiver,"sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    zhoe.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏғғ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    zhoe.sendMessage(receiver,"ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    zhoe.sendMessage(msg.to, "ʀᴇsᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                                else:
                                    zhoe.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴋᴛɪᴠᴇ, ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ʀᴇsᴇᴛ")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        zhoe.sendMessage(receiver,"ɴᴏ sɪᴅᴇʀ")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = zhoe.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ ʀ ᴇ ᴀ ᴅ ᴇ ʀ ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        zhoe.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    zhoe.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        wait["mimic"]["target"][target] = True
                                        zhoe.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                                        break
                                    except:
                                        zhoe.sendMessage(msg.to,"ғᴀɪʟᴇᴅ ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del wait["mimic"]["target"][target]
                                        zhoe.sendMessage(msg.to,"ᴛᴀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                                        break
                                    except:
                                        zhoe.sendMessage(msg.to,"ғᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                                    
                            elif cmd == "mimiclist":
                                if wait["mimic"]["target"] == {}:
                                    zhoe.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ")
                                else:
                                    mc = "╔════[ ·✪·ᴍɪᴍɪᴄ ʟɪsᴛ·✪· ]════╗"
                                    for mi_d in wait["mimic"]["target"]:
                                        mc += "\n╠❂➣ "+zhoe.getContact(mi_d).displayName
                                    mc += "\n╚═════[  ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]═════╝"
                                    zhoe.sendMessage(msg.to,mc)

                            elif cmd.startswith("setspamcall: "):
                                     proses = text.split(":")
                                     strnum = text.replace(proses[0] + ":","")
                                     num =  int(strnum)
                                     wait["limit"] = num
                                     zhoe.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                            elif cmd.startswith("bahbehboh"):
                                if msg.toType == 2:
                                   group = zhoe.getGroup(to)
                                   members = [mem.mid for mem in group.members]
                                   jmlh = int(wait["limit"])
                                   zhoe.sendMessage(msg.to, "Invitation Call Grous {} In Progress ".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                    for x in range(jmlh):
                                     try:
                                        zhoe.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        zhoe.sendMessage(msg.to,str(e))
                                    else:
                                        zhoe.sendMessage(msg.to,"Invitation Call Groups Done")
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if wait["mimic"]["status"] == False:
                                        wait["mimic"]["status"] = True
                                        zhoe.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
                                elif mic == "off":
                                    if wait["mimic"]["status"] == True:
                                        wait["mimic"]["status"] = False
                                        zhoe.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏғғ")
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    zhoe.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    zhoe.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "sᴜʙᴜʜ : " and data[2] != "ᴅᴢᴜʜᴜʀ : " and data[3] != "ᴀsʜᴀʀ : " and data[4] != "ᴍᴀɢʜʀɪʙ : " and data[5] != "ɪsʜᴀ : ":
                                    ret_ = "╔═══[ ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ]"
                                    ret_ += "\n╠══[ sᴇᴋɪᴛᴀʀ " + data[0] + " ]"
                                    ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠❂➣ " + data[1]
                                    ret_ += "\n╠❂➣ " + data[2]
                                    ret_ += "\n╠❂➣ " + data[3]
                                    ret_ += "\n╠❂➣ " + data[4]
                                    ret_ += "\n╠❂➣ " + data[5]
                                    ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                    zhoe.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔═══[ ᴡᴇᴀᴛʜᴇʀ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠❂➣ sᴜʜᴜ : " + data[1].replace("Suhu : ","") + "°ᴄ"
                                        ret_ += "\n╠❂➣ ᴋᴇʟᴇᴍʙᴀʙᴀɴ : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠❂➣ ᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ : " + data[3].replace("Tekanan udara : ","") + "ʜᴘᴀ "
                                        ret_ += "\n╠❂➣ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ : " + data[4].replace("Kecepatan angin : ","") + "ᴍ/s"
                                        ret_ += "\n╠════[ ᴛɪᴍᴇ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S') + " ᴡɪʙ"
                                        ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                        zhoe.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔═══[ ʟᴏᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0]
                                        ret_ += "\n╠❂➣  ɢᴏᴏɢʟᴇ ᴍᴀᴘs : " + link
                                        ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                        zhoe.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        zhoe.sendImageWithURL(to, str(path))
                                        zhoe.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split(".")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            zhoe.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            zhoe.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        zhoe.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split(".")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    zhoe.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    zhoe.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say "):
                                sep = text.split(" ")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("Say " + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return zhoe.sendMessage(to, "ʟᴀɴɢᴜᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                zhoe.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("image"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        zhoe.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("music "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(".")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}ᴍᴜsɪᴄ {}.「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    zhoe.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                            zhoe.sendImageWithURL(to, str(data["result"]["img"]))
                                            zhoe.sendMessage(to, str(ret_))
                                            zhoe.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("lyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(".")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}ʟʏʀɪᴄ {}.「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    zhoe.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        zhoe.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("youtube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣{} ]".format(str(data["title"]))
                                    ret_ += "\n╠❂ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                zhoe.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return zhoe.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                zhoe.sendMessage(to, str(A))
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
                        if text.lower() == "mykey":
                            zhoe.sendMessage(to, "ᴋᴇʏᴄᴏᴍᴍᴀɴᴅ sᴀᴀᴛ ɪɴɪ [ {} ]".format(str(wait["keyCommand"])))
                        elif text.lower() == "setkey on":
                            wait["setKey"] = True
                            zhoe.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
                        elif text.lower() == "setkey off":
                            wait["setKey"] = False
                            zhoe.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#

#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
#######################TAMBAHAN###################################
#######################Token generator###################################

#TEST TOKEN

                        elif text.lower() == 'chromeos': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/CHROMEOS', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'iosipad': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/IOSIPAD', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'desktopmac': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/DESKTOPMAC', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'desktopwin': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/DESKTOPWIN', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'win10': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/WIN10', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)


                        elif text.lower() == 'get token':
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linktkn'])
                                    f.close()
                                    r = requests.get(link)
                                    ar = r.text
                                    zhoe.sendMessage(msg.to, ar)
                                    os.system('rm {}.txt'.format(msg._from)) 

                        


#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
  #========================================================              
#=========================================================================================================================================#

#=========================================================================================================================================#
                    elif msg.contentType == 1:
                        if wait["changePictureProfile"] == True:
                            path = zhoe.downloadObjectMsg(msg_id)
                            wait["changePictureProfile"] = False
                            zhoe.updateProfilePicture(path)
                            zhoe.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ")
                        if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = zhoe.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                zhoe.updateGroupPicture(to, path)
                                zhoe.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ")
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                            zhoe.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = zhoe.getContact(msg.contentMetadata["mid"])
                                if zhoe != None:
                                    cover = zhoe.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    zhoe.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                zhoe.sendMessage(to, str(ret_))
                            except:
                                zhoe.sendMessage(to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = zhoe.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                zhoe.sendMessage(to, str(ret_))
                            except:
                                zhoe.sendMessage(to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            msg = op.message
            if wait["autoResponPc"] == True:
                if msg.toType == 0:
                    zhoe.sendChatChecked(sender,msg_id)
                    contact = zhoe.getContact(sender)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    zhoe.sendImageWithURL(sender, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    zhoe.sendMessage(sender,dee)
#MODE PUBLIC TEST
        if op.type == 26:
            if wait["public"] == True:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != zhoe.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpPublic = helppublic()
                                zhoe.sendMessage(to, str(helpPublic))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                zhoe.sendMessage(to, str(helpTextToSpeech))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                zhoe.sendMessage(to, str(helpTranslate))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                                
                            elif cmd == "token":
                                helpToken = helptoken()
                                zhoe.sendMessage(to, str(helpToken))
                                zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                                
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    zhoe.sendMessage(to, "🔪JANGAN ADA TYPO 🔪")
                                else:
                                    wait["keyCommand"] = str(key).lower()
                                    zhoe.sendMessage(to, "SUCCES CHANGE KEY 🔧 [ {} ]".format(str(key).lower()))
                            elif cmd == "speed":
                            	start = time.time()
                            	zhoe.sendMessage(to, "⏭ Loading...")
                            	elapsed_time = time.time() - start
                            	zhoe.sendMessage(to, "My speed : %sms" % (elapsed_time))

                            elif cmd == "status":
                                try:
                                    ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                                    if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                                    if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                                    if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                                    if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                                    if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                                    if wait["autoResponPc"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚫」"
                                    if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                                    if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                                    if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                                    if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                                    if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                                    ret_ += "\n╚═════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]═════╝"
                                    zhoe.sendMessage(to, str(ret_))
                                    zhoe.sendContact(to, "u0b24e20b11c94bda952e8a68601e4239")
                                except Exception as e:
                                    zhoe.sendMessage(msg.to, str(e))
                            elif cmd.startswith("say "):
                                sep = text.split(" ")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say " + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return zhoe.sendMessage(to, "ʟᴀɴɢᴜᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                zhoe.sendAudio(to,"hasil.mp3")
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return zhoe.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                zhoe.sendMessage(to, str(A))
                            elif cmd == "me":
                                zhoe.sendContact(to, sender)
                            elif cmd == "mymid":
                                zhoe.sendMessage(to, "[ ᴍɪᴅ ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = zhoe.getContact(sender)
                                zhoe.sendMessage(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = zhoe.getContact(sender)
                                zhoe.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = zhoe.getContact(sender)
                                zhoe.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = zhoe.getContact(sender)
                                zhoe.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = zhoe.getProfileCoverURL(sender)          
                                path = str(channel)
                                zhoe.sendImageWithURL(to, path)

                            elif cmd == 'tagall':
                                group = zhoe.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    zhoe.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    zhoe.sendMessage(msg.to, "Total {} Mention".format(str(len(nama))))
                            elif cmd == "crash":
                                zhoe.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")

                            elif cmd == "cuy" or text.lower() == '☺':
                                   group = zhoe.getGroup(msg.to)
                                   nama = [contact.mid for contact in group.members]
                                   k = len(nama)//20
                                   for a in range(k+1):
                                       txt = u''
                                       s=0
                                       b=[]
                                       for i in group.members[a*20 : (a+1)*20]:
                                           b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                           s += 7
                                           txt += u'@Zero \n'
                                       zhoe.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                   
######################

                            elif cmd.startswith("image"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        zhoe.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("music "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(".")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}ᴍᴜsɪᴄ {}.「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    zhoe.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ 🗡 cнαℓүүzнυ вσт 🗡 ✯ ]"
                                            zhoe.sendImageWithURL(to, str(data["result"]["img"]))
                                            zhoe.sendMessage(to, str(ret_))
                                            zhoe.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("lyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(".")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}ʟʏʀɪᴄ {}.「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    zhoe.sendMessage(to, str(ret_))
#######################Token generator###################################

#TEST TOKEN

                        if text.lower() == 'chromeos': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/CHROMEOS', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'iosipad': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/IOSIPAD', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'desktopmac': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/DESKTOPMAC', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'desktopwin': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/DESKTOPWIN', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)

                        elif text.lower() == 'win10': ## HEADER CONTOH DESKTOPWIN
                            urllib.request.urlretrieve('http://api.eater.tech/WIN10', '{}.txt'.format(msg._from))
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linkqr'])
                                    f.close()
                                    zhoe.sendMessage(msg.to, link)


                        elif text.lower() == 'get token':
                            with open('{}.txt'.format(msg._from), 'r') as f:
                                qr = f.read()
                                j = json.loads(qr)
                                for p in j['result']:
                                    link = (p['linktkn'])
                                    f.close()
                                    r = requests.get(link)
                                    ar = r.text
                                    zhoe.sendMessage(msg.to, "Cek token mu di PM")
                                    zhoe.sendMessage(sender, "[ ᴍɪᴅ ]\n{}".format(sender))
                                    zhoe.sendMessage(sender, ar)
                                    os.system('rm {}.txt'.format(msg._from)) 

                        


#------------------------------------============================------------------------------------#
#======================-----------✰ 🗡 cнαℓүүzнυ вσт 🗡 ✰-----------======================#
#------------------------------------============================------------------------------------#
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != zhoe.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        zhoe.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            zhoe.sendMessage(msg.to,text)
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                zhoe.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                zhoe.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = zhoe.findGroupByTicket(ticket_id)
                                    zhoe.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    zhoe.sendMessage(to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name))
   
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if zhoeMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	zhoe.sendChatChecked(sender,msg_id)
                                    	contact = zhoe.getContact(sender)
                                    	zhoe.sendImageWithURL(sender, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	sendMention(sender, "woiiii @!      , \n tag tag bae , ada apa sihhh??", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = zhoe.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!      "
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            zhoe.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
        
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = zhoe.getContact(op.param2).displayName
                            dan = zhoe.getContact(op.param2)
                            tgb = zhoe.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "ᴡᴏʏ ☞ @!       ☜\nᴅɪ {} ᴋᴏᴋ ᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ".format(str(tgb.name)),[op.param2])
                                        zhoe.sendContact(op.param1, op.param2)
                                        zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                    else:
                                        sendMention(op.param1, "ᴍʙʟᴏ ☞ @!       ☜\nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ ᴅɪ {} \nsɪɴɪ ɢᴀʙᴜɴɢ ᴍᴀ ᴋɪᴛᴀ".format(str(tgb.name)),[op.param2])
                                        zhoe.sendContact(op.param1, op.param2)
                                        zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                else:
                                    sendMention(op.param1, "ʜɪʟɪʜ ☞ @!       ☜\nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ ᴅɪ {} ".format(str(tgb.name)),[op.param2])
                                    zhoe.sendContact(op.param1, op.param2)
                                    zhoe.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = zhoePoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                zhoeBot(op)
                zhoePoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
