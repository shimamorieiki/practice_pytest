import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv(override=True)

# 環境変数の取得
ENV_UTIL = os.getenv("ENV_UTIL")
