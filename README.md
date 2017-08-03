# Create Verilog LUTs from text files

This tool will create a Verilog module representing a look up table from a text
file of numbers.

It will automatically use the smallest required widths for the
input and output ports based on the largest value in the input file as well as
the number of values in the input. If a width is specified, warnings will be
printed to stdout if the width is smaller or larger than it needs to be.

## Help Text

```
usage: veriloglut.py [-h] [-dft] [-n name] [-o output] [-r radix] [-w width]
                     hexfile

Create a look-up-table in Verilog from a hex file

positional arguments:
  hexfile               The path to the input HEX file

optional arguments:
  -h, --help            show this help message and exit
  -dft                  If specified the synopsys DFT ports will be added
  -n name, --name name  The name of the Verilog module. (default: the name of
                        the input file)
  -o output, --output output
                        The path to the output Verilog file (default: stdout)
  -r radix, --radix radix
                        The radix of the input file values. Choices: bin, dec,
                        hex (default: dec)
  -w width, --width width
                        Force define the width of the LUT values in bits. If
                        not set it will automatically be set to the width of
                        the largest value of the input
```

## Example

Input file: `myLookupTable.txt`

```
140737219920510
140737220966017
140737222005428
140737223038790
140737224066150
140737225087554
140737226103048
140737227112678
140737228116489
140737229114526
140737230106832
140737231093451
140737232074428
140737233049804
140737234019623
140737234983925
140737235942755
140737236896151
140737237844157
140737238786811
140737239724155
140737240656227
140737241583069
140737242504718
140737243421213
140737244332593
140737245238896
140737246140159
140737247036419
140737247927715
140737248814081
140737249695555
```

Run command: `$ ./veriloglut.py -o myLookupTable.v myLookupTable.txt`

Output file: `myLookupTable.v`

```verilog
// automatically generated from myLookupTable.txt
// $ ./veriloglut.py -o myLookupTable.v myLookupTable.txt

module myLookupTable (
  input[4:0] sel,
  output reg[46:0] val
);

always @(sel) begin
  case(sel)
    0  : val[46:0] = 47'h7ffff000027e;
    1  : val[46:0] = 47'h7ffff00ff681;
    2  : val[46:0] = 47'h7ffff01fd2b4;
    3  : val[46:0] = 47'h7ffff02f9746;
    4  : val[46:0] = 47'h7ffff03f4466;
    5  : val[46:0] = 47'h7ffff04eda42;
    6  : val[46:0] = 47'h7ffff05e5908;
    7  : val[46:0] = 47'h7ffff06dc0e6;
    8  : val[46:0] = 47'h7ffff07d1209;
    9  : val[46:0] = 47'h7ffff08c4c9e;
    10 : val[46:0] = 47'h7ffff09b70d0;
    11 : val[46:0] = 47'h7ffff0aa7ecb;
    12 : val[46:0] = 47'h7ffff0b976bc;
    13 : val[46:0] = 47'h7ffff0c858cc;
    14 : val[46:0] = 47'h7ffff0d72527;
    15 : val[46:0] = 47'h7ffff0e5dbf5;
    16 : val[46:0] = 47'h7ffff0f47d63;
    17 : val[46:0] = 47'h7ffff1030997;
    18 : val[46:0] = 47'h7ffff11180bd;
    19 : val[46:0] = 47'h7ffff11fe2fb;
    20 : val[46:0] = 47'h7ffff12e307b;
    21 : val[46:0] = 47'h7ffff13c6963;
    22 : val[46:0] = 47'h7ffff14a8ddd;
    23 : val[46:0] = 47'h7ffff1589e0e;
    24 : val[46:0] = 47'h7ffff1669a1d;
    25 : val[46:0] = 47'h7ffff1748231;
    26 : val[46:0] = 47'h7ffff1825670;
    27 : val[46:0] = 47'h7ffff19016ff;
    28 : val[46:0] = 47'h7ffff19dc403;
    29 : val[46:0] = 47'h7ffff1ab5da3;
    30 : val[46:0] = 47'h7ffff1b8e401;
    31 : val[46:0] = 47'h7ffff1c65743;
  endcase
end // always @(sel) begin

endmodule // myLookupTable
```

If the `-dft` flag is specified then the module ports will include the following in addition to the default ports:

```verilog
// DFT ports
input reset,
input clk,
input scan_en,
input scan_in0,
input test_mode,
output scan_out0
```
