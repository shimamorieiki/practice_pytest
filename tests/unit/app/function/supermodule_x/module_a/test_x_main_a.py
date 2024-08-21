import sys
import os

if "config" in sys.modules:
    sys.modules.pop("config")

if "models.model_a" in sys.modules:
    # キャッシュを削除して再importする
    sys.modules.pop("models.model_a")

print("test_x_main_aのsys.path")
models_path = os.path.abspath(f"{os.getcwd()}/app/function/supermodule_x/module_a")
sys.path.insert(0, models_path)
for r in sys.path:
    print(r)
from app.function.supermodule_x.module_a.main_a import main

sys.path.remove(models_path)


class TestMainA:
    def test_main(self):
        print(main())
