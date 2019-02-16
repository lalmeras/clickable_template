#! /bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function

import logging

import click

import clickable.utils
import clickable.coloredlogs


# bootstrap logging system
clickable.coloredlogs.bootstrap()
logger = logging.getLogger('stdout.clickable')


# name consistently with pyproject.toml entrypoint
@click.group()
@click.pass_context
def main(ctx):
    """
    Deployment or development tasks
    """
    clickable.utils.load_config(ctx, __name__, __file__, 'clickables.yml')


@main.command()
@click.argument("suffix", "-s")
def hello(suffix):
    logger.info("Hello world {}".format(suffix))
