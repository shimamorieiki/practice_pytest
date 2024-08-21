from models.model_a import ModelA
import config as function_config
from utils import config


def main():
    m = ModelA()
    a = m.run()

    print(f"run: {a}, {function_config.ENV_X_A=}, {config.ENV_UTIL=}")
    return a


if __name__ == "__main__":
    main()
