__author__ = 'misha'

size = 2


def read(cpu, param):
    return cpu.memory.read(param), 0


def write(cpu, param, value):
    cpu.memory.write(param, value)


def print(param):
    return "{0:#06x}".format(param)