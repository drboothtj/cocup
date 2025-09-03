import argparse
from argparse import RawTextHelpFormatter


def get_parser():
    '''
    create a parser object for cocup
    '''
    parser = argparse.ArgumentParser(
        "cocup",
        description="cocup: Thom's COokie CUtter for Python",
        epilog="Written by Dr. Thom Booth, 2025.",
        formatter_class=RawTextHelpFormatter
        )
    parser.add_argument(
      'project_name',
      type=str
    )
    parser.add_argument(
      '-a', '--author',
      default=None,
      type=str
    )
    parser.add_argument(
      '-e', '--email',
      default=None,
      type=str
    )
    parser.add_argument(
      '-r', '--requirements',
      default=None,
      type=str
    )
    return parser

def parse_args():
    '''
    get the arguments from the console via the parser
    '''
    arg_parser = get_parser()
    args = arg_parser.parse_args()
    return args
