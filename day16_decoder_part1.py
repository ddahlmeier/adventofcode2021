#!/usr/bin/env python


"""--- Day 16: Packet Decoder ---"""


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

version_sum = 0


def decode_packet(bits):
    global version_sum
    print("decode packet ", bits)
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    print("version ", version)
    version_sum += version
    print("type id", type_id)
    offset = 0    
    if type_id == 4:
        literal, offset = decode_literal(bits[6:])
    else:
        offset = decode_operator(bits[6:])
    return offset+6


def decode_literal(bits):
    literal = ""
    for start in range(0, len(bits), 5):
        group = bits[start:start+5]
        keep_reading = True if group[0]=='1' else False
        literal += group[1:]
        if not keep_reading:
            break
    return (int(literal, 2), start+5)


def decode_operator(bits):
    length_type_id = int(bits[0],2)

    if length_type_id == 0:
        packet_length = int(bits[1:16], 2)
        offset = 16
        while offset < 16+packet_length:
            bits_read = decode_packet(bits[offset:16+packet_length])
            offset += bits_read
    elif length_type_id == 1:
        number_packets = int(bits[1:12], 2)
        offset = 12
        for _ in range(number_packets):
            bits_read = decode_packet(bits[offset:])
            offset += bits_read
    else:
        raise("Unknown length type {}", length_type_id)
    return offset

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day16_decoder_part1.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        bits = parse_bits(fin)
    decode_packet(bits)
    print(version_sum)