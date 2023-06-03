#!/usr/bin/env python3
import atheris
import sys

from dissect.cobaltstrike.c2profile import C2Profile
from dissect.cobaltstrike import xordecode
from lark import UnexpectedCharacters, UnexpectedToken


with atheris.instrument_imports(include=['dissect.cobaltstrike']):
    from dissect.cobaltstrike.beacon import BeaconConfig


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    choice = fdp.ConsumeIntInRange(0, 2)
    try:
        if choice == 0:
            BeaconConfig.from_bytes(fdp.ConsumeRemainingBytes())
        elif choice == 1:
            C2Profile.from_text(fdp.ConsumeRemainingString())
    except (ValueError, UnexpectedCharacters, UnexpectedToken):
        return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()