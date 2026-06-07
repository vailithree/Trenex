import subprocess
import pathlib

srcpath = pathlib.Path("src")
kernelsrcpath = pathlib.Path(srcpath / "kernel")
bootsrcpath = pathlib.Path(srcpath / "bootstuff")
programssrcpath = pathlib.Path(srcpath / "programs")
buildpath = pathlib.Path("bin")
