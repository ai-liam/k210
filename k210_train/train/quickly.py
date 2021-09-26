
import argparse, os, sys, shutil

# python3 ./k210_train/train/quickly.py -t classifier -z datasets/test_classifier_datasets.zip -o ../our
def main():
    supported_types = ["classifier", "detector"]
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(curr_dir)

    parser.add_argument("-t", "--type", type=str, help="train type, classifier or detector", choices=supported_types, default="classifier")
    parser = argparse.ArgumentParser(description="train model")
    parser.add_argument("-z", "--zip", type=str, help="datasets zip file path", default="")
    parser.add_argument("-d", "--datasets", type=str, help="datasets directory", default="")
    parser.add_argument("-o", "--out", type=str, help="out directory", default=os.path.join(curr_dir, "out"))
    args = parser.parse_args()
    print("type:",args.type)
    print("out:",args.out)
    print("zip:",args.zip)
    print("datasets:",args.datasets)


if __name__ == "__main__":
    sys.exit(main())