"""
auto_restart.py

このスクリプトは、Django プロジェクトの .py および .html ファイルの変更を監視し、
変更が検知されると Django 開発サーバーを自動で再起動します。
"""

import json
import os
import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# 定数設定
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "vscode_manage_config.json")

# 最後に使用した manage.py のパスを取得
def load_manage_py():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("last_manage_py")
    return None

# Django サーバープロセスを管理するクラス
class DjangoServerManager:
    def __init__(self, manage_py_path):
        self.manage_py_path = manage_py_path
        self.process = None

    def start_server(self):
        if self.process is None:
            print("Django サーバーを起動します...")
            cmd = [sys.executable, self.manage_py_path, "runserver", "--noreload"]
            try:
                self.process = subprocess.Popen(cmd)
            except Exception as e:
                print(f"サーバー起動失敗: {e}")

    def stop_server(self):
        if self.process is not None:
            print("Django サーバーを停止します...")
            self.process.terminate()
            self.process.wait()
            exit_code = self.process.returncode
            print(f"Django サーバーの終了コード: {exit_code}")
            self.process = None

    def restart_server(self):
        print("Django サーバーを再起動します...")
        self.stop_server()
        time.sleep(1)
        self.start_server()

# ファイル変更イベントハンドラ
class ChangeHandler(FileSystemEventHandler):
    def __init__(self, server_manager):
        self.server_manager = server_manager

    def on_modified(self, event):
        if event.src_path.endswith(('.py', '.html')):
            print(f"変更検知: {event.src_path}")
            self.server_manager.restart_server()

# メイン処理
if __name__ == "__main__":
    manage_py = load_manage_py()
    if not manage_py:
        print("manage.py のパスが設定されていません。")
        exit(1)

    project_dir = os.path.dirname(manage_py)
    server_manager = DjangoServerManager(manage_py)
    server_manager.start_server()

    event_handler = ChangeHandler(server_manager)
    observer = Observer()
    observer.schedule(event_handler, path=project_dir, recursive=True)
    observer.start()

    print(f"{project_dir} を監視中... .py および .html ファイルの変更で Django を再起動します。")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        server_manager.stop_server()
    observer.join()
