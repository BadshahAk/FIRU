
# Copyright (C) 2024 by 𓆩𔘓𓆪 𝐕⊶𝐈⊶𝐊⊶𝐑⊶𝐀⊶𝐍⊶𝐓 𓆩𔘓𓆪 Github-@vicky0604hello, 
# < https://github.com/vicky0404hello >.
# <https://github.com/vicky0604hello/DCxMUSIC >
# All rights reserved.

import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Directories Updated.")
