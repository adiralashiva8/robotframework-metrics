import os
import argparse
from .robotmetrics import generate_report
from .robotmetrics import IGNORE_LIBRARIES
from .robotmetrics import IGNORE_TYPES
from .version import __version__


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    general = parser.add_argument_group("General")
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        dest='version',
        help='Display application version information'
    )

    general.add_argument(
        '--ignorelib',
        dest='ignore',
        default=IGNORE_LIBRARIES,
        nargs="+",
        help="Ignore keywords of specified library in report"
    )

    general.add_argument(
        '--ignoretype',
        dest='ignoretype',
        default=IGNORE_TYPES,
        nargs="+",
        help="Ignore keywords of specified type in report"
    )

    general.add_argument(
        '-I', '--inputpath',
        dest='path',
        default=os.path.curdir,
        help="Path of result files"
    )

    general.add_argument(
        '-M', '--metrics-report-name',
        dest='metrics_report_name',
        help="Output name of the generate metrics report"
    )

    general.add_argument(
        '-O', '--output',
        dest='output',
        default="output.xml",
        help="Name of output.xml"
    )

    # general.add_argument(
    #     '-sk', '--showkeyword',
    #     dest='showkeyword',
    #     default="True",
    #     help="Display keywords in metrics report"
    # )

    general.add_argument(
        '-skt', '--showkwtimes',
        dest='showkwtimes',
        default="True",
        help="Display keyword times in metrics report"
    )

    general.add_argument(
        '-t', '--showtags',
        dest='showtags',
        default="False",
        help="Display test case tags in test metrics"
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_options()

    if args.version:
        print(__version__)
        exit(0)

    generate_report(args)