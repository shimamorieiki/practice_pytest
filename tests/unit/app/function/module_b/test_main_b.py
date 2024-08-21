import sys
import os

print("test_main_bのsys.path")
models_path = os.path.abspath(f"{os.getcwd()}/app/function/module_b")
sys.path.insert(0, models_path)
for r in sys.path:
    print(r)
from app.function.module_b.main_b import main
sys.path.remove(models_path)


class TestMainB:
    def test_main(self):
        print(main())
