"""Entry for make.fun news-image-20261120.

Copies the pre-rendered poster (image.png, shipped in this repository)
to /output/entry.png. Standard library only, no network, deterministic:
every run writes the same bytes as image.png.
"""

import hashlib
import os
import shutil
import struct

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def sha256_of(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("image.png not found next to main.py")
    with open(src, "rb") as f:
        header = f.read(33)
    if header[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise ValueError("image.png is not a PNG file")
    # IHDR chunk: width and height are the first 8 bytes after the
    # 8-byte magic + 4-byte length + 4-byte chunk type.
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            "image.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_hash = sha256_of(src)
    dst_hash = sha256_of(dst)
    assert src_hash == dst_hash, "output differs from image.png"
    assert os.path.getsize(src) == os.path.getsize(dst), "size mismatch"
    print("source sha256: " + src_hash)
    print("sha256: " + dst_hash)
    print("Wrote " + dst + " (" + str(os.path.getsize(dst)) + " bytes)")


if __name__ == "__main__":
    main()
