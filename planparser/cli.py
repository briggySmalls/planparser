"""Console script for planparser."""

import sys

import click

from planparser.planparser import PlanParser


@click.group()
@click.argument('filename', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, filename):
    ctx.ensure_object(dict)
    ctx.obj['result'] = PlanParser.parse(filename)


@cli.command()
@click.pass_context
def text(ctx):
    """Get the raw text from parsing the file"""
    click.echo(ctx.obj["result"].raw_string)
    return 0


@cli.command()
@click.pass_context
def matches(ctx):
    """Get the raw text from parsing the file"""
    click.echo(ctx.obj["result"].matches)
    return 0


@cli.command()
@click.pass_context
def numbers(ctx):
    """Get the raw text from parsing the file"""
    click.echo(ctx.obj["result"].numbers)
    return 0


@cli.command()
@click.pass_context
def area(ctx):
    """Get the raw text from parsing the file"""
    click.echo(ctx.obj["result"].area)
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
