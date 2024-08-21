import sys
import os

if "config" in sys.modules:
    sys.modules.pop("config")

if "models.model_b" in sys.modules:
    # キャッシュを削除して再importする
    sys.modules.pop("models.model_b")

print("test_x_main_bのsys.path")
models_path = os.path.abspath(f"{os.getcwd()}/app/function/supermodule_x/module_b")
sys.path.insert(0, models_path)
for r in sys.path:
    print(r)
from app.function.supermodule_x.module_b.main_b import main

sys.path.remove(models_path)


class TestMainB:
    def test_main(self):
        print(main())
