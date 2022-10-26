"""Console script for planparser."""

import sys

import click


@click.command()
def main():
    """Console script for planparser."""
    click.echo("Replace this message by putting your code into " "planparser.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
