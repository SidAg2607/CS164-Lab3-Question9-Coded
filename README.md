# CS164-Lab3-Question9-Coded
This code works on the algorithm in the question 9 of Lab 3 of CS164 course.

For this code:
rgb(aaa, bbb, ccc)
aaa - 1st part of rgb color code
bbb - 2nd part of rgb color code
ccc - 3rd part of rgb color code

This code is also available through repl.it if anyone would like to try it directly. Link: https://repl.it/@sa3724/Question9-Lab3#main.py

Question:
We're going to manipulate the binary numbers that describe the colors. The numbers are generally taken to be unsigned, but just for fun, we're going to treat them as signed numbers. Then after negating them, we'll treat the resulting bit patterns as unsigned numbers and display the resulting colors.

What we've been doing is looking at them as hexadecimal values like #FFFFFF or as base-10 RGB values. Let's look more into the binary. The reason we have 256 shades of colors is because that fits very nicely with a power of 2. This means, it's much easier to represent colors in binary. Let's look at plain red. Plain red has a hex value of #FF0000 and an RGB value of (255, 0, 0). Red, as a binary RGB value is (11111111, 00000000, 00000000). As we learned in class, there is a variety of ways to represent binary numbers. Right now, we are using an unsigned approach. What if we took a signed approach?

Let's take all our values and negate them using sign magnitude. 11111111 would become 01111111 which is now 127. 00000000 would become 10000000 which is now -0, or just normal 0. However, RGB values only take unsigned numbers. If we interpret our signed 10000000 and interpret it as unsigned, it's 128. Our new RGB value for negative red is now (127, 128, 128).

Let's do the same thing with one's complement! 11111111 would become 00000000 which is 0. 00000000 would become 11111111 which is -0. Since RGB doesn't take negative values, we'll just interpret this as unsigned and use 255. So now the RGB value for one's complement negative red is (0, 255, 255).

Finally, let's do this all again with two's complement. 11111111 will become 00000001 which is 1. 00000000 will become 00000000 which is 0. Negative red in two's complement is now (1,0,0). I made a table below of the colors.

                                   | Unsigned | Sign Magnitude | One's Complement | Two's Complement|
                                   |  255,0,0 |   127,128,128	|    0,255,255	   |      1,0,0     |
