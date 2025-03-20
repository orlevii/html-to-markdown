import subprocess
import sys


def get_lib_ext() -> str:
    if sys.platform.startswith("linux"):
        return "so"
    elif sys.platform == "darwin":
        return "dylib"
    elif sys.platform.startswith("win"):
        return "dll"
    else:
        raise RuntimeError("Unsupported platform")


def build_go_extension() -> None:
    """Compile the Go shared library"""

    subprocess.run(
        [
            "go",
            "build",
            "--buildmode=c-shared",
            "-o",
            f"html-to-markdown.{get_lib_ext()}",
            "html-to-markdown.go",
        ],
        check=True,
        cwd="./src/go_html_to_markdown/_go",
    )


def main() -> None:
    build_go_extension()
    print("Build complete!")


if __name__ == "__main__":
    main()
