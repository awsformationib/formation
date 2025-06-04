import argparse
import logging
import pathlib
import os

PATHLOG = pathlib.Path("../logs")
PATHEXP = pathlib.Path("../exports")
LEVEL = logging.WARNING

def init():
    global PATHEXP,PATHLOG,LEVEL

    # ce que je peux attendre de la ligne de commance
    parser = argparse.ArgumentParser(
        prog='AirOps',
        description='Gere une compagnie aerienne')
    parser.add_argument('-l', '--logs')
    parser.add_argument('-e', '--exports')
    parser.add_argument('-d', '--debug',  type=int)

    # analyse de la ligne de commande
    args = parser.parse_args()

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

