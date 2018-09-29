"""Command line interface for Buckler, a password manager for python."""


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
