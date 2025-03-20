import ctypes
import sys
from pathlib import Path


def get_lib_ext() -> str:
    if sys.platform.startswith("linux"):
        return "so"
    elif sys.platform == "darwin":
        return "dylib"
    elif sys.platform.startswith("win"):
        return "dll"
    else:
        raise RuntimeError("Unsupported platform")


# Path to the shared library within this package.
lib_path = (
    Path(__file__).parent.joinpath("_go", f"html-to-markdown.{get_lib_ext()}").resolve()
)
assert lib_path.exists(), f"Library not found at {lib_path}"
lib = ctypes.CDLL(str(lib_path))

lib.ConvertHTMLToMarkdown.argtypes = [ctypes.c_char_p]
lib.ConvertHTMLToMarkdown.restype = ctypes.c_char_p


def html_to_markdown(html: str) -> str:
    res: bytes = lib.ConvertHTMLToMarkdown(html.encode("utf-8"))
    return res.decode("utf-8")
