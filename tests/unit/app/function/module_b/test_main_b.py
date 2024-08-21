import sys
import os

print("test_main_bのsys.path")
sys.path.insert(1, os.path.abspath(f"{os.getcwd()}/app/function/module_b"))
sys.path.remove(
    r"C:\Users\aifor\prog\practice_pytest\practice_pytest\app\function\module_a"
)
for r in sys.path:
    print(r)
from app.function.module_b.main_b import main


class TestMainB:
    def test_main(self):
        print(main())
