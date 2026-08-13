# Nand2Tetris

Implementation of the Nand2Tetris course projects: building a computer from
a single NAND gate up through logic gates, arithmetic, memory, and machine
language.

## Status

| Stage | Description                  | Status      |
|-------|-------------------------------|-------------|
| 01    | Logic Gates                   | Complete    |
| 02    | Arithmetic / ALU              | Complete    |
| 03    | Sequential Logic (Registers, RAM) | Complete |
| 04    | Machine Language               | In progress |
| 05    | CPU                            | Not started |
| 06    | Assembler                      | Not started |
| 07+   | VM, Compiler, OS                | Not started |

## Structure

```
projects/
├── 01-logic-gates/         Basic gates: And, Or, Not, Xor, Mux, DMux (and 16-bit / multi-way variants)
├── 02-arithmetic/          HalfAdder, FullAdder, Add16, Inc16, ALU
├── 03-sequential-logic/    Bit, Register, RAM8, RAM64
└── 04-Machine-Language/    Hack assembly programs (Mult.asm, Fill.asm)
```

Each chip has three files:
- `.hdl` — the implementation
- `.tst` — the test script
- `.cmp` — the expected output, used to verify correctness

## Tools

- HDL (Hardware Description Language) — used to define each chip
- Nand2Tetris Hardware Simulator — runs the `.tst` scripts against each `.hdl` file
- Hack Assembly — used from Stage 04 onward

## Running tests

Open the relevant `.tst` file in the Hardware Simulator and run it. A pass
means the chip's output matches the `.cmp` file exactly.

## Current work

Stage 04 (Machine Language) has just started. `Mult.asm` and `Fill.asm` are
the first two assembly programs — multiplication via repeated addition, and
screen fill on keypress.

## Roadmap

- Finish Stage 04 (Machine Language)
- Build the CPU (Stage 05)
- Build the Assembler (Stage 06)
- Continue toward the VM translator +  compiler and OS