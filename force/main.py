from argparse import ArgumentParser
from functools import reduce
from turtle import exitonclick

from .force import Force, add_force
from . import draw


def main():
    args = parse_args()
    forces = [Force(*force) for force in args.force]
    if args.calculate:
        res = reduce(add_force, forces)
        print(res)
    else:
        draw.setup(args.speed, args.gpp, args.gpp_size)
        if args.draw == 'par':
            res = draw.par(forces)
        else:
            res = draw.htt(forces)
        print(res)
        draw.shutdown()


def parse_args():
    parser = ArgumentParser('force')

    parser.add_argument(
        '-f', '--force',
        action='append',
        required=True,
        nargs=2, metavar=('size', 'direction'),
        type=float
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-c', '--calculate',
        action='store_true'
    )
    group.add_argument(
        '-d', '--draw',
        choices=('par', 'htt')
    )
    parser.add_argument(
        '-s', '--speed',
        type=float,
        default=6
    )
    parser.add_argument(
        '-g', '--gpp',
        action='store_true'
    )
    parser.add_argument(
        '--gpp-size',
        type=float,
        default=25
    )

    return parser.parse_args()
