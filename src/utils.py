"""Utility functions."""
import os
import logging


def setup_log(filename: str):
    """Set logging format."""
    logging.basicConfig(
        # filename='pg_pro.log',
        level=logging.DEBUG,
        format=f'%(asctime)s | {os.path.basename(filename)} | %(levelname)s | %(message)s')
