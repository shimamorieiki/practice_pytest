# import sys

# sys.path.append("app/function/module_a")
from app.function.module_a.main_a import main


class TestMainA:
    def test_main(self):
        print(main())
