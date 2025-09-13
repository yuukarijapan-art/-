import random
from datetime import datetime

BASIC_QUOTES = [
    "おはよう。今日の一歩が、半年後のあなたを変える。",
    "小さな前進でも、続ければ大きな景色になる。",
    "深呼吸して、良い一日を。",
    "人と比べるより、昨日の自分を越えていこう。",
    "コツコツは最強。焦らない、止まらない。",
    "笑顔は伝染する。あなたの周りから世界を明るく。",
    "まずは5分だけやってみる。気づけば進んでる。",
    "完璧より、まず完了。次で磨けばいい。",
    "迷ったら、ワクワクする方へ。",
    "未来は、いまの選択で静かに動き出す。",
]

def choose_basic():
    today = datetime.now().strftime("%Y-%m-%d")
    base = random.choice(BASIC_QUOTES)
    hashtags = "#朝活 #おはよう #前向き #習慣化 #今日も頑張ろう"
    return f"{base}\n\n{today}\n{hashtags}"
