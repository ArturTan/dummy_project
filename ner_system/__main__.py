from argparse import ArgumentParser
from ner_system.ner_system import show_ners


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--string", required=True)
    parser.add_argument("--language", required=True)
    args = parser.parse_args()
    print(show_ners(args.string, args.language))
