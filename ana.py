#!/usr/bin/env python3

import typer
from rich import print
from typing_extensions import Annotated
from typing import Optional

import base64


app = typer.Typer(no_args_is_help=True)

@app.command()
def main(hash: Annotated[str, typer.Argument()], debug: bool = True):
    """
    Analyzes a hash to see what it is!
    Could be md5 or base64 or whatever!

    Can
    """
    global DEBUG
    DEBUG = debug
    hash_matchs = []

    if DEBUG:
        print("[bold red]DEBugging Alert![/bold red]")
        print(f"For the Hash: {hash}")
    # print(f"Hash looks to be one of: {hash_matchs}")
    is_base64(hash)


    typer.Exit()

def is_base64(test_str):
    if DEBUG:
        print(f"    Checking for base 64")
    try:
        decoded = base64.b64decode(test_str)
        print(f"Decoded: {decoded}")
    except:
        print(f"    not base64")


if __name__ == "__main__":
    app()
