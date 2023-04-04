import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import pyperclip
import platform
import socket
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

notion_api_key = os.environ.get('NOTION_API_KEY')

notion = Client(auth=notion_api_key)

database_id = os.environ.get('DATABASE_ID')

@app.route('/save_to_notion', methods=['POST'])
def save_to_notion():
    content = request.json.get('content')

    if not content:
        return jsonify({"error": "Content is required"}), 400

    device_name = get_device_name()
    create_notion_page(content, device_name)

    return jsonify({"message": "Content saved to Notion"}), 201


def get_device_name():
    system = platform.system()
    hostname = socket.gethostname()
    return f"{system}-{hostname}"

def create_notion_page(content, device_name):
    new_page = {
        "Content": {
            "title": [
                {
                    "text": {
                        "content": content
                    }
                }
            ]
        },
        "Device Name": {
            "rich_text": [
                {
                    "text": {
                        "content": device_name
                    }
                }
            ]
        }
    }

    notion.pages.create(parent={"database_id": database_id}, properties=new_page)


def clipboard_monitor():
    prev_text = ''
    while True:
        try:
            text = pyperclip.paste()
            if text != prev_text:
                prev_text = text
                device_name = get_device_name()
                create_notion_page(text, device_name)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    clipboard_monitor()
    app.run()
