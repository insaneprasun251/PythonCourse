import yaml
import argparse
import sys


def main(number, another_number, output):
    result = number * another_number
    print(f'The result is {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('--config', '-c', dest='config', type=argparse.FileType('r'), help='config file in YAML format',
                        default=None)
    parser.add_argument('--output', '-o', dest='output', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        config = yaml.load(args.config)
        # No need to transform values
        args.n1 = config['ARGUMENTS']['n1']
        args.n2 = config['ARGUMENTS']['n2']
    main(args.n1, args.n2, args.output)
