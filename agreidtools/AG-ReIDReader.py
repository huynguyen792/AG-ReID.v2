import argparse

from datasets import AG_ReID


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='AG-ReID Data Reader.')
    parser.add_argument('--data_path', required=True, default='./data')
    args = parser.parse_args()

    dset = AG_ReID(root=args.data_path)
    