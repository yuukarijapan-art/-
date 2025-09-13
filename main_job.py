import os, json, uuid
from datetime import datetime
from dotenv import load_dotenv
from caption_sources import choose_basic
from image_maker import make_image


def getenv(name, default=None, cast=str):
    v = os.getenv(name, default)
    if v is None:
        return None
    if cast is int:
        try:
            return int(v)
        except:
            return default
    return v


def generate_caption():
    use_openai = os.getenv("USE_OPENAI", "0") == "1"
    api_key = os.getenv("OPENAI_API_KEY", "")

    if use_openai and api_key:
        try:
            import openai
            openai.api_key = api_key
            prompt = "朝のインスタ用に、前向きで短い日本語の一言と軽いハッシュタグを1〜2行で作成してください。"
            resp = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=60,
                temperature=0.8,
            )
            return resp["choices"][0]["text"].strip()
        except Exception:
            pass
    return choose_basic()


def run():
    load_dotenv()
    out_dir = os.path.join(os.getcwd(), "out")
    os.makedirs(out_dir, exist_ok=True)

    caption = generate_caption()
    width = int(getenv("WIDTH", 1080))
    height = int(getenv("HEIGHT", 1350))
    font_path = getenv("FONT_PATH", None)
    uid = uuid.uuid4().hex[:8]
    img_path = os.path.join(out_dir, f"post_{datetime.now().strftime('%Y%m%d')}_{uid}.jpg")
    make_image(img_path, caption, width=width, height=height, font_path=font_path)

    logline = {"time": datetime.now().isoformat(), "caption": caption, "image_path": img_path.replace("\\\\", "/")}
    with open(os.path.join(out_dir, "log.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(logline, ensure_ascii=False) + "\n")

    dry = os.getenv("DRY_RUN", "1") == "1"
    if dry:
        print("[DRY-RUN] 画像作成のみ完了:", img_path)
        return

    access_token = os.getenv("FB_ACCESS_TOKEN", "")
    ig_id = os.getenv("IG_BUSINESS_ACCOUNT_ID", "")
    if not access_token or not ig_id:
        print("[SKIP] トークン未設定のため投稿をスキップ。DRY_RUN=0にしている場合は設定を確認してください。")
        return

    # TODO: ここで image_path をS3等へアップロードして image_url を取得 → instagram_api を呼ぶ
    print("[INFO] 投稿には image_url が必要です。アップロード実装後にIG投稿処理を有効化してください。")


if __name__ == "__main__":
    run()
