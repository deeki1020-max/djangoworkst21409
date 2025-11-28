# このスクリプトは Django プロジェクト内の manage.py を自動検出・選択し、
# 指定されたコマンドを実行するためのランチャーです。
# 最後に使用した manage.py のパスは vscode_manage_config.json に保存されます。

# vscode_manage_config.json: 最後に使用した manage.py のパスを記録する設定ファイルです。

import json
import os
import subprocess
import sys

# * スクリプトと同じディレクトリに設定ファイルを置く
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "vscode_manage_config.json")

# * manage.pyファイルがあるフォルダを探す処理
def find_all_manage_py(start_path):
    matches = []
    for root, dirs, files in os.walk(start_path):
        if 'manage.py' in files:
            matches.append(os.path.join(root, 'manage.py'))
    return matches

# * プロジェクトが複数あった場合に選択しを表示し選択する処理
def choose_manage_py(paths):
    print("複数の manage.py が見つかりました。使用するものを選んでください：")
    for i, path in enumerate(paths):
        print(f"{i + 1}: {path}")
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if 1 <= choice <= len(paths):
                return paths[choice - 1]
        except ValueError:
            pass
        print("無効な入力です。もう一度お試しください。")

# * 最後に選択したプロジェクトを呼び出す処理（保存先vscode_manage_config.json）
def load_last_choice():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if os.path.exists(data.get("last_manage_py", "")):
                    return data["last_manage_py"]
        except Exception:
            pass
    return None

# * 最後に選択したプロジェクトを保存しておく処理（保存先vscode_manage_config.json）
def save_last_choice(path):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump({"last_manage_py": path}, f)
    except Exception:
        pass

# * 最後に選択したプロジェクトをリセット（保存先vscode_manage_config.json）
def reset_choice():
    if os.path.exists(CONFIG_PATH):
        os.remove(CONFIG_PATH)
        print("記憶された manage.py のパスをリセットしました。")
    else:
        print("記憶ファイルは存在しません。")

if __name__ == "__main__":
    if "--reset" in sys.argv:
        reset_choice()
        sys.exit(0)

    base_dir = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
    print("manage.py 探索開始位置:", base_dir)

    last_used = load_last_choice()
    if last_used:
        print(f"前回使用した manage.py を再利用します: {last_used}")
        subprocess.run([sys.executable, last_used] + sys.argv[1:])
        sys.exit(0)

    candidates = find_all_manage_py(base_dir)
    if not candidates:
        print("manage.py が見つかりませんでした。")
        sys.exit(1)

    selected = candidates[0] if len(candidates) == 1 else choose_manage_py(candidates)
    save_last_choice(selected)
    try:
        subprocess.run([sys.executable, selected] + sys.argv[1:])
    except KeyboardInterrupt:
        print("Django サーバーを中断しました。")
