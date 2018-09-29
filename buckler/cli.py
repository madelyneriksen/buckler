"""Command line interface for Buckler, a password manager for python."""


import os
from getpass import getpass
import click
import pyperclip
import buckler


def get_key() -> bytes:
    """Get the user's key from the input prompt.

    Returns:
        key: The user's key for encryption.
    """
    while True:
        passwd_first = getpass()
        passwd_second = getpass("Retype Password:")
        if passwd_first == passwd_second:  # pylint: disable=no-else-return
            return passwd_first.encode()
        else:
            click.secho("Passwords don't match!", color='red')


@click.group()
def main():
    """Buckler is a command line password manager written in python.

    Passwords are stored in files on the system, allowing you to sync them up
    to a cloud provider or share them across computers easily. All you need
    is Buckler installed on the target system.
    """
    pass


@main.command()
@click.argument("name")
@click.option("--length", default=24, type=int)
@click.option("--directory", type=str)
def create(name, length, directory):
    """Create and save an encypted password to the filesystem.

    The created password is copied to your clipboard for convenience.
    Passwords will be stored in '.buckler/' in your home folder.
    """
    key = get_key()
    try:
        if directory:
            passwd = buckler.create_password(key, name, length, directory)
        else:
            passwd = buckler.create_password(key, name, length)
        pyperclip.copy(passwd)
        click.secho(("Password for {name} saved and copied to the clipboard!"
                     .format(name=name)), fg='green')
    except ValueError:
        click.secho("The given password doesn't match the current password.",
                    fg='red')


@main.command()
@click.option("--directory", type=str)
def show(directory):
    """List all the current passwords you have saved."""
    if not directory:
        directory = buckler.BUCKLER_DIR
    files = [x for x in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, x))]
    files.remove('.token')
    if files:
        click.secho("Here are your saved password names:", fg="blue")
        for file in files:
            click.secho(file, fg="green")
    else:
        click.secho("You have no saved passwords.", fg="red")


@main.command()
@click.argument("name")
@click.option("--directory", type=str)
def get(name, directory):
    """Get a password that's saved in the filesystem."""
    key = get_key()
    try:
        if directory:
            passwd = buckler.read_password(key, name, directory)
        else:
            passwd = buckler.read_password(key, name)
        pyperclip.copy(passwd)
        click.secho("Password for {} copied to clipboard!".format(name),
                    fg="green")
    except ValueError:
        click.secho("The given password doesn't match the current password",
                    fg='red')
    except FileNotFoundError:
        click.secho("There's no password with the name {}".format(name),
                    fg="red")


if __name__ == "__main__":
    main()
