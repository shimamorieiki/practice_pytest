import sys
import os

# キャッシュを削除して再importする
sys.modules.pop("models.model_b")

# 絶対パスを指定する
models_path = os.path.abspath(f"{os.getcwd()}/app/function/supermodule_y/module_b")
sys.path.insert(0, models_path)
from app.function.supermodule_y.module_b.main_b import main

sys.path.remove(models_path)


class TestMainB:
    def test_main(self):
        print(main())
