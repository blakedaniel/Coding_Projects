# instructions

1. The clock circuit ticks at a constant rate; each tick is called a cycle
2. The CPU has a single register, X, which starts with the value 1
3. 'addx V' takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)

4. 'noop' takes one cycle to complete. It has no other effect.
5. The sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite
6. You count the pixels on the CRT: 40 wide and 6 high
7. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39
8. the CRT draws a single pixel during each cycle.
9. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.)
