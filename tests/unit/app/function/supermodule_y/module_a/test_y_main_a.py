import sys
import os

print("test_y_main_aのsys.path")
models_path = os.path.abspath(f"{os.getcwd()}/app/function/supermodule_y/module_a")
sys.path.insert(0, models_path)
for r in sys.path:
    print(r)
from app.function.supermodule_y.module_a.main_a import main

sys.path.remove(models_path)


class TestMainA:
    def test_main(self):
        print(main())
