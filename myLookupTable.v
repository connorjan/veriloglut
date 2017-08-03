// automatically generated from myLookupTable.txt
// $ ./veriloglut.py -o myLookupTable.v myLookupTable.txt -dft

module myLookupTable (
  input[4:0] sel,
  output reg[46:0] val,

  // DFT ports
  input reset,
  input clk,
  input scan_en,
  input scan_in0,
  input test_mode,
  output scan_out0
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
