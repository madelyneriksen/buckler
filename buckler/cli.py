"""Command line interface for Buckler, a password manager for python."""


import click
import pyperclip
from buckler import encrypt


@click.group()
def main():
    """Buckler is a command line password manager written in python.

    Passwords are stored in files on the system, allowing you to sync them up
    to a cloud provider or share them across computers easily. All you need
    is Buckler installed on the target system.
    """
    pass


@main.command()
def create():
    """Create and save an encypted password to the filesystem.

    Passwords will be stored in .buckler/ in your home folder.
    """
    click.echo("Created password.")


@main.command()
def show():
    """List all the current passwords you have saved."""
    click.echo("No passwords here!")


@main.command()
def get():
    """Get a password that's saved in the filesystem."""
    click.echo("Grabbed your password!")


@main.command()
def rotate():
    """Rotate a password, swapping it for a new password."""
    click.echo("Rotated password.")


if __name__ == "__main__":
    main()
