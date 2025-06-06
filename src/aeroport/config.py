import argparse
import logging
import pathlib
import os
import time

from decorateurs import benchmark

PATHLOG = pathlib.Path("../../logs")
PATHEXP = pathlib.Path("../../exports")
LEVEL = logging.WARNING
CREATE = False

def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Valeur attendue: true/false')


def init():
    global PATHEXP,PATHLOG,LEVEL, CREATE

    # ce que je peux attendre de la ligne de commance
    parser = argparse.ArgumentParser(
        prog='AirOps',
        description='Gere une compagnie aerienne')
    parser.add_argument('-l', '--logs')
    parser.add_argument('-e', '--exports')
    parser.add_argument('-c', '--create', type=str2bool)
    parser.add_argument('-d', '--debug',  type=int)

    # analyse de la ligne de commande
    args = parser.parse_args()

    CREATE = args.create

    if args.logs:
        PATHLOG = pathlib.Path(args.logs)
    if args.exports:
        PATHEXP = pathlib.Path(args.exports)

    if args.debug:
        LEVEL = args.debug * 10

    if not PATHLOG.is_dir():
        os.mkdir(PATHLOG)

    if not PATHEXP.is_dir():
        os.mkdir(PATHEXP)

    time.sleep(2)

