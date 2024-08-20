from models.model_a import ModelA


def main():
    m = ModelA()
    a = m.run()
    print(a)
    return a


if __name__ == "__main__":
    main()
