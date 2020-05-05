# -*- coding:utf-8 -*-
# author：huawei

import base64
UTF8 = "utf-8"


def decode(text):
    return str(base64.b64decode(text), UTF8)


def encode(text):
    return str(base64.b64encode(text.encode(UTF8)), UTF8)


if __name__ == "__main__":
    d = "test"
    d = encode(d)
    print(d)
    d = decode(d)
    print(d)