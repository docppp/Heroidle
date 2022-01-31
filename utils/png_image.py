import imghdr
import os
import struct


def get_png_image_size(file_name: str) -> tuple[int, int]:
    with open(file_name, 'rb') as file_handle:
        head = file_handle.read(24)
        if len(head) != 24:
            raise ValueError(f"{file_name} is not png image")
        if imghdr.what(file_name) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                raise ValueError(f"{file_name} is not png image")
            width, height = struct.unpack('>ii', head[16:24])
            return width, height
        raise ValueError(f"{file_name} is not png image")


def get_png_dir_size(dir_path: str, ignore_size_mismatch=False) -> tuple[int, int]:
    x, y = get_png_image_size(dir_path + os.sep + os.listdir(dir_path)[0])
    for file_name in os.listdir(dir_path):
        width, height = get_png_image_size(dir_path + os.sep + file_name)
        if (x, y) != (width, height) and not ignore_size_mismatch:
            raise ValueError(f"Png at {dir_path} do not match in size."
                             f"{(x, y)} != {(width, height)}")
    return x, y
