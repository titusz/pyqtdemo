#!/usr/bin/python3
from glob import glob
import os

from PyQt5.uic import compileUi


HERE = os.path.abspath(os.path.dirname(__file__))


def build_ui():
    for uifile in glob(os.path.join(HERE, "src/main/python/tutorial/ui/*.ui")):
        pyfile = os.path.splitext(uifile)[0] + ".py"
        print(uifile)
        pyfile = open(pyfile, "wt", encoding="utf-8")
        uifile = open(uifile, "rt", encoding="utf-8")
        compileUi(uifile, pyfile, from_imports=True)


if __name__ == '__main__':
    build_ui()
