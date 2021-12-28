#!/usr/bin/env python


"""--- Day 16: Packet Decoder ---"""

from operator import mul
from functools import reduce
import sys

def parse_bits(fin):
    hex2binary = {'0': '0000', 
    '1': '0001',
    '2': '0010',
    '3': '0011', 
    '4': '0100',
    '5': '0101', 
    '6': '0110',
    '7': '0111',
    '8': '1000', 
    '9': '1001',
    'A': '1010', 
    'B': '1011', 
    'C': '1100', 
    'D': '1101',
    'E': '1110', 
    'F': '1111'}
    return ''.join((hex2binary[symbol] for symbol in fin.readline().strip()))



def decode_packet(bits):
    print("decode packet ", bits)
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    print("version ", version)
    print("type id", type_id)
    if type_id == 4:
        value, offset = decode_literal(bits[6:])
    else:
        value, offset = decode_operator(bits[6:])
        if type_id == 0:
            value = sum(value)
        elif type_id == 1:
            value = reduce(mul, value, 1)
        elif type_id == 2:
            value = min(value)
        elif type_id == 3:
            value = max(value)
        elif type_id == 5:
            value = 1 if value[0] > value[1] else 0
        elif type_id == 6:
            value = 1 if value[0] < value[1] else 0
        elif type_id == 7:
            value = 1 if value[0] == value[1] else 0
        else:
            raise("Unknown type id {}", type_id)
    return value, offset+6


def decode_literal(bits):
    literal = ""
    for start in range(0, len(bits), 5):
        group = bits[start:start+5]
        keep_reading = True if group[0]=='1' else False
        literal += group[1:]
        if not keep_reading:
            break
    return int(literal, 2), start+5


def decode_operator(bits):
    length_type_id = int(bits[0],2)
    values = []
    if length_type_id == 0:
        packet_length = int(bits[1:16], 2)
        offset = 16
        while offset < 16+packet_length:
            value, bits_read = decode_packet(bits[offset:16+packet_length])
            values.append(value)
            offset += bits_read
    elif length_type_id == 1:
        number_packets = int(bits[1:12], 2)
        offset = 12
        for _ in range(number_packets):
            value, bits_read = decode_packet(bits[offset:])
            values.append(value)
            offset += bits_read
    else:
        raise("Unknown length type {}", length_type_id)
    return values, offset


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day16_decoder_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        bits = parse_bits(fin)
    value, _ = decode_packet(bits)
    print(value)