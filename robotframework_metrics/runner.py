import os
from optparse import OptionParser
from .robotmetrics import generate_report


def parse_options():
    parser = OptionParser()

    parser.add_option(
        '--logo',
        dest='logo',
        default='https://cdn.pixabay.com/photo/2016/08/02/10/42/wifi-1563009_960_720.jpg',
        help="User logo (default: dummy wifi image )"
    )

    parser.add_option(
        '--ignorelib',
        dest='ignore',
        default=None,
        help="""Ignore keywords of specified library in report 
        (default: 'BuiltIn', 'SeleniumLibrary', 'String', 'Collections', 'DateTime')"""
    )

    parser.add_option(
        '--to',
        dest='to',
        default=None,
        help="To address (default: None )"
    )

    parser.add_option(
        '--from',
        dest='sender',
        default=None,
        help="From address (default: None )"
    )

    parser.add_option(
        '--cc',
        dest='cc',
        default=None,
        help="CC address (default: None )"
    )

    parser.add_option(
        '--pwd',
        dest='pwd',
        default=None,
        help="Password of email (default: None )"
    )

    parser.add_option(
        '--ignoretype',
        dest='ignoretype',
        default=None,
        help="""Ignore keywords with specified type in report
        (default: foritem, for )"""
    )

    parser.add_option(
        '-I', '--inputpath',
        dest='path',
        default=None,
        help="Path of result files (default: current folder)"
    )

    parser.add_option(
        '-R', '--report',
        dest='report_name',
        default='report.html',
        help="Name of report.html (default: report.html)"
    )

    parser.add_option(
        '-L', '--log',
        dest='log_name',
        default='log.html',
        help="Name of log.html (default: log.html)"
    )

    parser.add_option(
        '-O', '--output',
        dest='output',
        default=None,
        help="Name of output.xml (default: output.xml)"
    )

    parser.add_option(
        '-E', '--email',
        dest='email',
        default='True',
        help="Send email with metrics report when -E or --email is True (default: True)"
    )

    opts, args = parser.parse_args()
    return parser, opts, args


def main():
    parser, opts, arguments = parse_options()

    generate_report(opts)
