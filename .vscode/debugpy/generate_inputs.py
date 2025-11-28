
# このスクリプトは Django プロジェクトルートにあるフォルダを走査し、
# 有効なプロジェクト一覧を apps.json に保存します。
# VS Code の launch.json の inputs セクション更新に利用されます。

# apps.json: プロジェクトルートにある Django プロジェクト一覧を記録するファイルです。


import json
import os

# 除外フォルダ
EXCLUDE = {'.vscode', 'djangovm', '__pycache__'}
# スクリプトのあるディレクトリ（.vscode/setting）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# プロジェクトルート（.vscode/setting の1階層上）
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))

# * ROOTで指定したディレクトリから1フォルダを取りだす
apps = [
    name for name in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, name)) and name not in EXCLUDE
]

# * apps.json をスクリプトと同じ場所に保存
apps_path = os.path.join(SCRIPT_DIR, 'apps.json')
with open(apps_path, 'w', encoding='utf-8') as f:
    json.dump(apps, f, indent=2, ensure_ascii=False)

