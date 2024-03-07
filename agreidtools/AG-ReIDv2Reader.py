import argparse

from datasets import AG_ReID_v2


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='AG-ReID.v2 Data Reader.')
    parser.add_argument('--data_path', required=True, default='./data')
    args = parser.parse_args()

    dset = AG_ReID_v2(root=args.data_path)
    