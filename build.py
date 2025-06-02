#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["jupyter-repo2docker"]
# ///
import subprocess

if __name__ == "__main__":
    subprocess.run(
        [
            "jupyter-repo2docker",
            "--no-run",
            "--image-name",
            "geojupyter/geojupyter:local",
            ".",
        ],
    )
