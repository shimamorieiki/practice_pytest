import sys

print("test_main_aのsys.path")
for r in sys.path:
    print(r)
from app.function.module_a.main_a import main


class TestMainA:
    def test_main(self):
        print(main())
