"""
Run PyVISA-proxy server as service
"""
import argparse
import logging
import sys

from .ProxyServer import ProxyServer

LOGGER = logging.getLogger(__name__)


def parse_args(arguments):
    """Create input argument parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--port",
        type=int,
        dest="port",
        default=5000,
        help="Port for zmq localhost binding",
    )
    return parser.parse_args(arguments)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )
    args = parse_args(sys.argv[1:])
    with ProxyServer(args.port) as server:
        server.run()
