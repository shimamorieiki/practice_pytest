from models.model_b import ModelB
import config as function_config


def main():
    m = ModelB()
    a = m.run()
    print(f"run: {a}, {function_config.ENV_X_B=}")
    return a


if __name__ == "__main__":
    main()
