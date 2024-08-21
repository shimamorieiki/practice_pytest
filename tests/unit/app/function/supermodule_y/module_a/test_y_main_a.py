import sys
import os


if "config" in sys.modules:
    sys.modules.pop("config")

if "models.model_a" in sys.modules:
    # キャッシュを削除して再importする
    sys.modules.pop("models.model_a")

# 絶対パスを指定する
models_path = os.path.abspath(f"{os.getcwd()}/app/function/supermodule_y/module_a")
sys.path.insert(0, models_path)
from app.function.supermodule_y.module_a.main_a import main

sys.path.remove(models_path)


class TestMainA:
    def test_main(self):
        print(main())
