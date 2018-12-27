import os
from optparse import OptionParser
from .robotmetrics import generate_report


def parse_options():
    parser = OptionParser()

    parser.add_option(
        '--logo',
        dest='logo',
        default='https://cdn.pixabay.com/photo/2016/08/02/10/42/wifi-1563009_960_720.jpg'
    )

    parser.add_option(
        '--ignorelib',
        dest='ignore',
        default=None,
    )

    parser.add_option(
        '--to',
        dest='to',
        default=None,
    )

    parser.add_option(
        '--from',
        dest='sender',
        default=None,
    )

    parser.add_option(
        '--cc',
        dest='cc',
        default=None,
    )

    parser.add_option(
        '--pwd',
        dest='pwd',
        default=None,
    )

    parser.add_option(
        '--ignoretype',
        dest='ignoretype',
        default=None,
    )

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
