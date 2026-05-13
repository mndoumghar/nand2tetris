
# 🧠 Nand2Tetris — From NAND to a Fully Working Computer

> Building a complete computer system from first principles — starting from a single NAND gate and ending with a functional CPU & architecture.

---

## ⚡ Overview

This repository contains my implementation of the **Nand2Tetris** course projects.
The goal is to progressively construct a full computer system, starting from basic logic gates and moving all the way up to CPU design and memory systems.

Everything is built from scratch using **Hardware Description Language (HDL)**.

---

## 🏗️ System Architecture Progression

```
NAND Gate
   ↓
Logic Gates (AND, OR, NOT, XOR)
   ↓
Arithmetic Circuits (Adders, ALU)
   ↓
Sequential Logic (Registers, Memory)
   ↓
CPU (Control + Data Path)
   ↓
Computer System
   ↓
Operating System (Future stage)
```

---

## 📁 Repository Structure

```
projects/
├── 01-logic-gates/
│   ├── Basic Gates (AND, AND16, OR16, OR8Way, Not16, OR, NOT, XOR)
│   ├── Multi-bit Gates => (MUX, MUX16, MUX8Way16)
│   └── Multiplexers & Demultiplexers => (DMUX, DMUX4Way, DMUX8Way)
│
├── 02-arithmetic/
│   ├── HalfAdder / FullAdder
│   ├── (Add16, Inc16)
│   ├── Incrementer (Inc16)
│   └── ALU (Arithmetic Logic Unit)
│
```

---

## 🧩 Project Breakdown

### 🔹 01 — Logic Gates

Built using only NAND as a primitive gate.

* AND / OR / NOT / XOR
* Mux / DMux
* 16-bit variants
* Multi-way selectors

### 🔹 02 — Arithmetic Logic Unit (ALU)

Core computational unit of the CPU:

* Half Adder / Full Adder design
* 16-bit addition
* Incrementer (Inc16)
* Full ALU supporting:

  * Addition
  * Bitwise AND
  * Zero / Negation control logic

---

## 🛠 Tech Stack

* **HDL (Hardware Description Language)** — chip design
* **Hardware Simulator** — testbench execution
* **Binary logic simulation**

---

## 📊 Progress Tracker

* [x] 01 — Logic Gates
* [x] 02 — Arithmetic / ALU
---

## 🎯 Key Concepts Learned

* Boolean algebra from first principles
* Combinational vs sequential logic
* Hardware abstraction layers
* CPU datapath design
* Low-level computation model

---

## 🧠 Big Picture

This project is basically:

> “Rebuilding modern computing from zero knowledge — only NAND.”

---

## 🚀 Future Work 

* Complete CPU design
* Build RAM + memory hierarchy
* Implement machine language
* Move toward OS-level abstraction

---

##  Notes

All chips are implemented and tested manually using HDL simulation scripts provided by the course.

---

##  Optional Upgrades

* Add CI pipeline for HDL testing
* Include CPU architecture diagrams
* Add simulation screenshots/GIFs
* Modular docs per project stage
