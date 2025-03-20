from pathlib import Path


def main() -> None:
    whls = list(Path("dist").rglob("*.whl"))
    if whls:
        print(whls[0])


if __name__ == "__main__":
    main()
