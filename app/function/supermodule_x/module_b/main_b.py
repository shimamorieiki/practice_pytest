from models.model_b import ModelB


def main():
    m = ModelB()
    a = m.run()
    print(a)
    return a


if __name__ == "__main__":
    main()
