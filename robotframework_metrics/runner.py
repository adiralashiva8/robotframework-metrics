import os
from optparse import OptionParser
from .robotmetrics import generate_report


def parse_options():
    parser = OptionParser()

    parser.add_option(
        '-I', '--inputpath',
        dest='path',
        default=None
    )

    parser.add_option(
        '-R', '--report',
        dest='report_name',
        default='report.html'
    )

    parser.add_option(
        '-L', '--log',
        dest='log_name',
        default='log.html'
    )

    parser.add_option(
        '-O', '--output',
        dest='output',
        default=None
    )

    parser.add_option(
        '-E', '--email',
        dest='email',
        default='True'
    )

    opts, args = parser.parse_args()
    return parser, opts, args


def main():
    parser, opts, arguments = parse_options()

    generate_report(opts)
