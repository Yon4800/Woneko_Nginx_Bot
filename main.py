from misskey import Misskey, NoteVisibility
from dotenv import load_dotenv
import random
import os

load_dotenv()
mk = Misskey(os.getenv("SERVER"))
mk.token = os.getenv("TOKEN")

wonekonote = [
    "おぽんぽん ん:neko_tired2:",
    "ん～～～～～～～～～～～:neko_tired2:",
    "みゃんみゃん:neko_relax:",
    "ん:neko_tired2:💢",
    "おぽんぽん 4 Pro :neko_tired2:",
    "ん、、、ん、、、ん、、、、、、おぽんぽん:neko_tired2:",
    "おぽんぽん買って:neko_tired2:",
    "$[ruby OrangePi おぽんぽん] くれ:neko_tired2:",
    "$[ruby OrangePi おぽんぽん] 買って:neko_tired2:",
    "$[ruby OrangePi おぽんぽん] 買ってー:neko_tired2:"
    "みゃんみゃん:neko_relax: んーーーーーーーーーー:neko_tired2:",
    "22:22分です:neko_tired2:",
    "わにゃん ん:neko_tired2:",
    "えほえほ:neko_cry:",
    "わん:neko_tired2:",
    "わーん:neko_tired2:",
    "WAN:neko_tired2:",
    "をねこ:neko_relax::neko_tired2:",
    "うぃーん:neko_tired2:",
    "えさくれ:neko_tired2:",
    "はは、:neko_tired2:",
    "こY:neko_cry:",
    ":neko_tired2: :explosion:",
    "あ、、、あ、、、あ、、、、、、:apache_apaxtuxtixe::neko_tired2:",
    "繧ｪ繝ｼ繝ｫ繧ｦ繧｣繝翫�縺医�縺斐�繧�￥縺ｫ縺倥ｅ縺�↑縺ｪ縺ｮ縺翫⊃繧薙⊃繧薙⊇縺励＞:neko_tired2:",
    "すべてソーセージ:neko_tired2:",
    "Allwinner A527のSBCかってー:neko_relax:",
    "Allwinner A733のSBCかってー:neko_relax:",
    "Allwinner A838のSBCかってー:neko_relax:",
    "あーん:neko_cry:",
    "をねことは何者なのか...我々はアマゾンの奥地へ向かった...",
    "Hello:neko_relax:",
    "何かあったらYon4800に言ってね:neko_relax:",
    "んーーーー！！！んーーーー！！！:neko_tired2:"
]

polls = [
    "OrangePi 4 Pro",
    "OrangePi Zero 3",
    "Radxa Cubie A5E",
    "Radxa Rock Pi S",
    "Radxa Zero 3E",
    "おぽんぽん",
    "ん、、、ん、、、ん、、、、、、:neko_tired2:",
    ":nginx_nnginxi:",
    "Allwinner A733",
    "Allwinner A527",
    "Allwinner H618",
    "Rockchip RK3568",
    "Rockchip RK3308",
    ":neko_relax:",
    ":neko_tired2:",
    ":neko_cry:",
    ":orangepi:",
    "おすし",
    "ハンバーガー",
    "ラーメン",
    "青椒肉絲",
    "プルコギ",
    "シーフード",
    "イカの塩辛",
    "をねこの闇を暴く",
    ":orangepi: の闇を暴く",
    "おぽんぽんの闇を暴く",
    "んーーーーの闇を暴く",
    ":neko_relax: の闇を暴く",
    ":neko_tired2: の闇を暴く",
    ":nginx_nnginxi: の闇を暴く",
    "ごはん:neko_relax:",
]

randnginx = random.randint(0, 100)
randnnnnginx = random.randint(0, 200)
randPoll = random.randint(0, 75)
if randnginx == 0:
    mk.notes_create(":nginx_nnginxi: :neko_tired2:", visibility=NoteVisibility.HOME)
elif randnnnnginx == 0:
    mk.notes_create(
        "ん、、、ん、、、ん、、、、、、:nginx_nnginxi: :neko_tired2:",
        visibility=NoteVisibility.HOME,
    )
elif randPoll == 0:
    mk.notes_create(
        "みゃんみゃん❤:neko_relax:",
        poll={
            "choices": random.sample(polls, 4),
            "multiple": False,
            "expiredAfter": 24 * 60 * 60 * 1000,
        },
        visibility=NoteVisibility.HOME,
    )
else:
    mk.notes_create(random.choice(wonekonote), visibility=NoteVisibility.HOME)
