import re


def main(str):
    str_spl = str.split('<:')
    d = {}
    for i in range(1, len(str_spl)):
        exr = r'\s*decl\s*([^)]*)\s*<-\s*([^)]*)\;'
        matches = re.findall(exr, str_spl[i])
        d[matches[0][0].strip()] = int(matches[0][1])
    return d
