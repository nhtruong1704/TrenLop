import struct


def uint16uint32uint8(x, start):
    size = struct.unpack("> H", x[start: start + 2])[0]
    add = struct.unpack("> I", x[start + 2: start + 6])[0]
    a = struct.unpack("> " + "B" * size, x[add: add + 1 * size])
    return list(a)

def uint32uint16uint32(x, start):
    size = struct.unpack("> I", x[start: start + 4])[0]
    add = struct.unpack("> H", x[start + 4: start + 6])[0]
    a = struct.unpack("> " + "I" * size, x[add: add + 4 * size])
    return list(a)

def addressD(x, start):
    return struct.unpack("> I", x[start:start+4])[0]


def addressE(x, start):
    return struct.unpack("> H", x[start:start+2])[0]

def E(x, start):
    return {
        'E1': [struct.unpack('> q', x[start:start + 8])[0],
               struct.unpack('> q', x[start + 8:start + 16])[0]],
        'E2': struct.unpack("> H", x[start + 16:start + 18])[0],
        'E3': struct.unpack("> Q", x[start + 18:start + 26])[0],
        'E4': struct.unpack("> q", x[start + 26:start + 34])[0],
        'E5': uint32uint16uint32(x, start + 34),
        'E6': struct.unpack("> h", x[start + 40:start + 42])[0]
    }

def D(x, start):
    return {
        'D1': struct.unpack("> B", x[start:start + 1])[0],
        'D2': struct.unpack("> B", x[start + 1:start + 2])[0]
    }


def C(x, start):
    size = struct.unpack("> I", x[start + 2: start + 6])[0]
    add = struct.unpack("> I", x[start + 6: start + 10])[0]
    return {
        'C1': struct.unpack("> H", x[start:start + 2])[0],
        'C2': [D(x, addressD(x, add + j * 4)) for j in range(0, size)],
        'C3':  E(x, addressE(x, start + 10)),
        'C4': struct.unpack("> Q", x[start + 12:start + 20])[0],
        'C5': struct.unpack("> b", x[start + 20:start + 21])[0]
    }


def B(x, start):
    return {
        'B1': struct.unpack("> q", x[start:start + 8])[0],
        'B2': struct.unpack("> h", x[start + 8:start + 10])[0],
        'B3': struct.unpack("> h", x[start + 10:start + 12])[0],
        'B4': C(x, start + 12),
        'B5': uint16uint32uint8(x, start + 33),
        'B6': struct.unpack("> d", x[start + 39:start + 47])[0],
    }


def A(x, start):
    return {
        'A1': struct.unpack('> B', x[start + 1:start + 2])[0],
        'A2': B(x, start + 2),
        'A3': struct.unpack("> d", x[start + 49:start + 57])[0],
        'A4': struct.unpack("> f", x[start + 57:start + 61])[0]
    }


def main(x):
    return A(x, 4)


print(main(b'\xbaMFJRd\x8b\x05\x05\x12\xdc\xe0\x93\xcaL\xabcFC\x8f\x00\x00\x00\x04'
           b"\x00\x00\x00I\x00e\x138\x8e\x9c\xdfR\xbb\x8e\x03\x00\x02\x00\x00\x00"
           b"\x8f\xbf\xd2\xac\x81\xee\x85\x870?\xc5H\xc3@B\x03\xf0\xbd\xb8o"
           b"\xf8\xfd\xc2\x13\xce\x90\x13\r\x00\x00\x00\x00A\x00\x00\x00C\x00\x00\x00"
           b'E\x00\x00\x00G\xa1W\x9b\xbb$\'?\x1eL3k\xb0\x97\xef\xe7\xa6\x18#}\\a\xb1\xfc'
           b"\x90\xb6\x8d\xcc\xbe\x9c\x19\xd7\xbd@\xd0\xeb%]\tx\xb6^K\xf8XW,\x00"
           b"\x00\x00\x03\x00Y\xb2\xb0\rz"))

print(main(b"\xbaMFJR\xd9\xa3\x97\x178`X\\\xb5w\xcc\x10b\xb4\xdb\x00\x00\x00\x03"
           b"\x00\x00\x00G\x00_v\x05a\xe5\x9d\x8fF\xc1U\x00\x03\x00\x00\x00\x89?\xea4"
           b"<\xd4\x8d\xa3\x14\xbf\xe5w\xba\x1a{D\x18\xbe\xaf\xf4\xcc\xb1\xe8\xfd0xF\x00"
           b"\x00\x00A\x00\x00\x00C\x00\x00\x00E\x9dJ\xa6\xe5\x83\xeb\xff\xfbM"
           b"\xc3q\xf6\xb6\xd1\x0e\xae\"MO\x81\x84\xcc\xb4\xc3K\x80o\xf5\xc9\xe6\x13u\xa0"
           b"\xc7m\xf2\xfbj\x98E_I+\xfa\x0bo\x00\x00\x00\x03\x00S\x84\xd2XP\xee"))

