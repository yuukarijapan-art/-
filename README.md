# Instagram AutoPost (Render Cron / Private, No Public HTTP)

このパックは Render の **Cron Job** として動かします。Webサーバーを公開しないので外部アクセスの心配が少ない設計です。

- 毎朝 07:00 (JST) に1回実行（`render.yaml` で設定済み）
- 画像生成はPillowでローカル完結
- まずは `DRY_RUN=1`（投稿せず画像とログだけ）
- シークレットはRenderの **Environment variables & secrets** に保存（Gitに入れない）

## 使い方（要点）
1. このフォルダをGitHubにアップロード（ルートに `render.yaml` が見える状態）
2. Render → **+ New → Blueprint** → GitHubのリポジトリを選択 → **Apply/Deploy**
3. サービスを開いて **Environment** に以下を追加
   - `OPENAI_API_KEY`（必要なら。未使用なら `USE_OPENAI=0`）
   - `USE_OPENAI=1` または `0`
   - `DRY_RUN=1`（最初は1）
   - `TIMEZONE=Asia/Tokyo`
   - （任意）`WIDTH=1080`, `HEIGHT=1350`, `FONT_PATH=./fonts/NotoSansJP-Regular.ttf`
4. **Run Job** で手動実行→Logsで `[DRY-RUN] 画像作成のみ完了:` が出ればOK

## 次の段階（Instagram投稿）
- IG Graph APIは **image_url** が必須。生成画像をS3等にアップしてURLを作り、`instagram_api.py` を呼び出す処理を追加してください（必要なら追記コードを用意します）。
