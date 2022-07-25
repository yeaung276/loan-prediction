import subprocess


def build() -> None:
    """
    Build the app using docker
    """
    subprocess.run(
        [
            "sudo",
            "docker",
            "build",
            "--no-cache",
            "--build-arg",
            "port=8080",
            "-t",
            "loan-prediction",
            ".",
        ]
    )


if __name__ == "__main__":
    build()
