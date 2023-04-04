# Clipboard to Notion

Clipboard to Notionは、クリップボードの内容を自動的にNotionに保存するFlaskアプリケーションです。このアプリケーションは、クリップボードからテキストを取得し、デバイス名とともにNotionデータベースに新しいページとして保存します。

## Features

- クリップボードの内容（テキスト）を自動的にNotionデータベースに保存
- 端末名も同時に保存

## Installation

1. このリポジトリをクローンまたはダウンロードします。

`git clone https://github.com/hiroki76/clipboard-to-notion.git`  

2. 仮想環境を作成し、アクティブ化します（オプション）。

`python -m venv venv  source venv/bin/activate`  

3. `requirements.txt`から依存関係をインストールします。

`pip install -r requirements.txt`


## Usage

1. Notion APIキーを取得し、プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下のように記述します。  

`NOTION_API_KEY=your_notion_api_key`
`DATABASE_ID=your_notion_database_id`

2. `your_notion_database_id`と`your_notion_api_key` をアプリケーションで使用するNotionデータベースのAPI_KEYとIDに更新します。

3. Notion上のデーターベースへ`Content`と`Device Name`の列を作成します。コネクトも追加します。

4. アプリケーションを実行します。  
`python app.py`
