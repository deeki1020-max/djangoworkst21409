
# このスクリプトは Django プロジェクト内の .py ファイルの変更を監視し、
# 変更が検知されると Django 開発サーバーを自動で再起動します。
# manage.py のパスは vscode_manage_config.json から取得されます。

import json
import os

import json5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .vscode/debugpy
apps_path = os.path.join(SCRIPT_DIR, "apps.json")        # ← 正しい場所
launch_path = os.path.join(os.path.dirname(SCRIPT_DIR), "launch.json")  # .vscode/launch.json

# 1. プロジェクト一覧を取得（generate_inputs.py で保存された apps.json を読み込む）
with open(apps_path, "r", encoding="utf-8") as f:
    apps = json.load(f)

# 2. launch.json を読み込む
with open(launch_path, "r", encoding="utf-8") as f:
    launch = json5.load(f)

# 3. inputs セクションの selectProject を更新
for input_item in launch.get("inputs", []):
    if input_item.get("id") == "selectProject":
        input_item["options"] = apps

# 4. launch.json を上書き保存
with open(launch_path, "w", encoding="utf-8") as f:
    json.dump(launch, f, indent=2, ensure_ascii=False)

print("launch.json の inputs.options を更新しました。")
