from models.model_a import ModelA
import config as function_config


def main():
    m = ModelA()
    a = m.run()

    print(f"run: {a}, {function_config.ENV_X_A=}")
    return a


if __name__ == "__main__":
    main()
