# import sys

# sys.path.append("app/function/module_b")
from app.function.module_b.main_b import main


class TestMainB:
    def test_main(self):
        print(main())
