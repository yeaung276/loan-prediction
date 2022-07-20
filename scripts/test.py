import subprocess


def test() -> None:
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    subprocess.run(["python", "-u", "-m", "unittest", "discover"])

if __name__ == '__main__':
    test()