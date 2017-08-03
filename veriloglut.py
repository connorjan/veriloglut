#!/usr/bin/env python

import argparse
import os
import sys

def error(message, exitCode=1):
    print >> sys.stderr, "error: {}".format(message)
    sys.exit(exitCode)

def warning(message):
    print >> sys.stderr, "warning: {}".format(message)

def readInput(file, radix):
    """
    Reads an input file of values and returns a list of python integers
    """
    lines = [line.strip() for line in file.readlines()]
    values = []

    if radix == "bin":
        radixInt = 2
    elif radix == "dec":
        radixInt = 10
    elif radix == "hex":
        radixInt = 16
    else:
        return None

    lineCount = 1
    for line in lines:
        try:
            converted = int(line, radixInt)
        except Exception as e:
            error("invalid value \"{}\" on line {} for radix {}"
                    .format(line, lineCount, radix), 1)

        values.append(converted)
        lineCount += 1

    return values

def createLUT(moduleName, values, valueWidth, selWidth, writeDFT, comments=[]):
    out = ""
    
    # Write any comment headers
    if comments:
        for comment in comments:
            out += "// {}\n".format(comment)
        out += "\n"
    
    # Write the module header
    out += "module {} (\n".format(moduleName)
    out += "  input[{}:0] sel,\n".format(selWidth-1)
    out += "  output reg[{}:0] val".format(valueWidth-1)
    if writeDFT:
        out += ",\n"
        out += "\n"
        out += "  // DFT ports\n"
        out += "  input reset,\n"
        out += "  input clk,\n"
        out += "  input scan_en,\n"
        out += "  input scan_in0,\n"
        out += "  input test_mode,\n"
        out += "  output scan_out0\n"
    else:
        out += "\n"
    out += ");\n"
    out += "\n"
    
    # Write the always block header
    out += "always @(sel) begin\n"
    out += "  case(sel)\n"

    # Write the LUT contents
    padding = len(str(len(values)))
    for i in range(len(values)):
        out += "    {:<{padding}} : val[{}:0] = {}'h{:x};\n".format(i,
                        valueWidth-1, valueWidth, values[i], padding=padding)

    # Write closing statements
    out += "  endcase\n"
    out += "end // always @(sel) begin\n"
    out += "\n"
    out += "endmodule // {}\n".format(moduleName)

    return out

def main(args):
    if not os.path.isfile(args.hexfile):
        error("cannot find file: {}".format(args.hexfile))
    else:
        with open(args.hexfile, "rb") as file:
            values = readInput(file, args.radix)

        if not values:
            error("did not find any values in {}".format(args.hexfile))

        # The largest width needed to represent the values in the input
        widthNeeded = sorted(values)[-1].bit_length()
        
        if args.width is not None and args.width < widthNeeded:
            warning("You specified a width of {} bits, but the largest value of"
                    " the input requires {} bits to be represented and will"
                    " be truncated".format(args.width, widthNeeded))
        
        elif args.width is not None and args.width > widthNeeded:
            warning("You specified a width of {} bits, but the largest value of"
                    " the input only requires {} bits to be represented. The"
                    " LUT will be unnecessarily big"
                    .format(args.width, widthNeeded))

        # Set the width of the value
        if args.width is not None:
            valueWidth = args.width
        else:
            valueWidth = widthNeeded

        # Set the width of the select line
        selWidth = (len(values)-1).bit_length()

        # Get the module name
        if args.name is not None:
            moduleName = args.name
        else:
            moduleName = os.path.splitext(os.path.basename(args.hexfile))[0]

        module = createLUT(moduleName, values, valueWidth, selWidth, args.dft,
                           comments=["automatically generated from {}"
                                        .format(args.hexfile),
                                     "$ {}".format(" ".join(sys.argv))])

        if args.output:
            # write the output to a file
            with open(args.output, "wb") as outputFile:
                outputFile.write(module)
        else:
            # write the output to stdout
            sys.stdout.write(module)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a look-up-table in"
                                                  " Verilog from a hex file")
    parser.add_argument("-dft", required=False, action="store_true",
                        help="If specified the synopsys DFT ports will"
                             " be added")
    parser.add_argument("-n", "--name", required=False, metavar="name",
                        type=str, help="The name of the Verilog module."
                                       " (default: the name of the input file)")
    parser.add_argument("-o", "--output", required=False, metavar="output",
                        type=str, help="The path to the output Verilog file"
                                       " (default: stdout)")
    parser.add_argument("-r", "--radix", required=False, metavar="radix",
                        type=str, choices=["bin","dec","hex"], default="dec",
                        help="The radix of the input file values."
                             " Choices: bin, dec, hex (default: %(default)s)")
    parser.add_argument("-w", "--width", required=False, metavar="width",
                        type=int, help="Force define the width of the LUT"
                                       " values in bits. If not set it will"
                                       " automatically be set to the width of"
                                       " the largest value of the input")
    parser.add_argument("hexfile", metavar="hexfile", type=str,
                        help="The path to the input HEX file")
    args = parser.parse_args()

    main(args)
