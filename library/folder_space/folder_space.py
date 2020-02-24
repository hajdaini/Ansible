#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *
import subprocess

size_conversion = { "k": 1024, "m": pow(1024,2), "g": pow(1024,3), "t": pow(1024,4), "p": pow(1024,5) }


def checkSizeAndUnit(module, space_unit, space):
    if space_unit not in 'kmgtp':
        module.fail_json(msg="Bad size specification for unit {}".format(space_unit) )
    if not space.isdigit():
        module.fail_json(msg="Bad value for {}, must be an integer".format(space))


def getSizeAndUnit(module, size):
    space_unit, space = size[-1].lower(), size[0:-1]
    checkSizeAndUnit(module, space_unit, space)
    return space_unit, int(space)


def convertToByte(space_unit, space):
    global size_conversion
    return int(space * size_conversion[space_unit])


def convertByteToOriginal(space_unit, space):
    global size_conversion
    return round(space / float(size_conversion[space_unit]), 2)


def getWantedSpace(module, size):
    space_unit, space_wanted = getSizeAndUnit(module, size) 
    return convertToByte(space_unit, space_wanted)


def getAvailableSpace(module, path):
    try:
        statvfs = os.statvfs(path)
        return int(statvfs.f_bavail * statvfs.f_frsize)
    except OSError as e:
        module.fail_json(msg="{}".format(e))


def CheckSizeAvailability(module, path, size):
    space_available = getAvailableSpace(module, path)
    space_wanted = getWantedSpace(module, size)
    space_unit, _ = getSizeAndUnit(module, size)
    space_available_converted = convertByteToOriginal(space_unit, space_available)

    if space_available < space_wanted:
        module.fail_json(msg="Not enough space available on {} (found = {}{}, need = {})".format(path, space_available_converted, space_unit, size))


def main():
    fields = {
        "path": {"required": True, "type": "str" },
        "size": {"required": True, "type": "str" }
    }
    module = AnsibleModule(argument_spec=fields)
    path = module.params['path']
    size = module.params['size']
    CheckSizeAvailability(module, path, size)

    response = {"result" : "You have enough space :)"}
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
