<div align="center">

<img src="assets/profile-banner.png" alt="mikey-7x — POWERED BY [mikey:hexoid-sys]" width="100%">

<br>

<a href="https://github.com/mikey-7x?tab=repositories"><img src="https://img.shields.io/badge/repositories-33-2f3640?style=flat-square&labelColor=0f1114&logo=github&logoColor=white" alt="Repositories"></a>
<img src="https://img.shields.io/badge/brand-POWERED%20BY%20%5Bmikey%3Ahexoid--sys%5D-2f3640?style=flat-square&labelColor=0f1114" alt="Brand">
<img src="https://img.shields.io/badge/focus-Vulkan%20on%20Android-3c4043?style=flat-square&labelColor=0f1114" alt="Focus">
<img src="https://img.shields.io/badge/target-Snapdragon%208%20Gen%203-3c4043?style=flat-square&labelColor=0f1114" alt="Target">
<img src="https://img.shields.io/badge/licence-personal%20%26%20educational%20%C2%B7%20strict-b3261e?style=flat-square&labelColor=0f1114" alt="Licence">

<h1>mikey-7x</h1>

<p><b>Architect · software developer · hardware developer</b><br>
Vulkan capabilities on Android phones — drivers, runtimes and the compatibility layers above them.</p>

<p><code>POWERED BY [mikey:hexoid-sys]</code> — the brand of this owner repository and of three
projects only.</p>

</div>

---

## About

I work on the layer between a phone's silicon and the software people want to run on it:
**graphics and compute drivers, the runtimes that talk to them, and the compatibility layers
that carry Windows and Linux applications onto Android.**

The development target is a **Snapdragon 8 Gen 3** platform: **Adreno 750** GPU, **Hexagon**
NPU and Kryo CPU, with **Vulkan** as the API of record through **Turnip** and **Mesa**, and
**glibc** and **bionic** as the two C libraries the same kernel has to satisfy.

Everything here is **active engineering work, described as such** — not certified results, not
benchmark claims. Where a number appears, the method behind it is published with it.

<div align="center">

<a href="assets/introduction-poster.pdf"><img src="assets/introduction-poster.png" alt="POWERED BY [mikey:hexoid-sys] — owner repository poster: the brand, the three powered projects, the platform stack and the method" width="660"></a>

<b>Owner repository poster</b> — the brand and its exact scope, the three powered projects,
the six-layer platform and the method.<br>
<a href="assets/introduction-poster.png">PNG</a> ·
<a href="assets/introduction-poster.pdf">PDF (A2, print)</a>

</div>

## The brand — `POWERED BY [mikey:hexoid-sys]`

<div align="center">

<img src="assets/powered-by-mikey-hexoid-sys.png" alt="POWERED BY [mikey:hexoid-sys]" width="420">

</div>

`POWERED BY [mikey:hexoid-sys]` is the mark of **this owner repository** and of the **three
projects listed below — and nothing else**. It is deliberately narrow: the mark is a statement
that a project carries a complete engineering build, so it is only applied where that is true.

**A repository carries the mark only when all four conditions hold:**

| # | Condition | What it means |
| --- | --- | --- |
| 1 | **Documented architecture** | the system's assumptions, layers and refusals are written down |
| 2 | **Measured or checkable results** | a number is published together with the method that produced it |
| 3 | **Reproducible build path** | pinned versions, a scripted install, published checksums |
| 4 | **Explicit limits and licence** | limits, safety rules and licence in plain language |

**Applied to:** flagship instruments · compiler and toolchain work · biosignal acquisition
chains.

**Not applied to:** utilities, one-liners, experiments, studies and archives — including any
repository that does not meet all four conditions. Those are published on their own terms and
are listed under [Other work](#other-work) without the mark.

## Powered projects

<table>
<tr>
<td width="50%" valign="top">

### mikey:hexoid v5.0.0

Universal embedded cross-compilation engine for Android (Termux) and Linux. 105 board
entries, Arduino CLI 0.35.3 pinned, SDCC for 8051 and STM8, iCE40 synthesis on the OSS CAD
Suite, and a library manager — driven from a numbered terminal menu, without an IDE.

`Bash` · `Python` · `Arduino CLI 0.35.3` · `SDCC` · `iCE40 / OSS CAD Suite`

**[Repository →](https://github.com/mikey-7x/mikey-hexoid-v5.0.0)**

</td>
<td width="50%" valign="top">

### 298.666 MHz frequency counter

STM32F103C8T6 counter on a TIM3:TIM2 32-bit hardware count, asynchronous ETR/8 input, a TI1F
cross-check at and below 40 MHz, 100 ms and 250 ms gates, and an SSD1306 display over I2C.
Companion exact-step generator and a VHF/UHF transmitter test circuit.

`STM32F103C8T6` · `STM32duino` · `SSD1306 I2C` · `TIM2 ETR / TI1F` · `2N2222`

**[Repository →](https://github.com/mikey-7x/298.666mhz-frequency-counter-using-stm32f103c8t6-and-vhf-uhf-fm-transmitter-circuit)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Project Synapse v1

Single-channel EEG and subvocal-EMG acquisition chain: INA128 front-end at G = 501, ADS1115
16-bit conversion at 140 Hz, a framed HC-05 link, Trinx segmentation, DTW matching and
CNN-LSTM / CNN-GRU decoders. An experimental study — not a medical device.

`INA128` · `ADS1115 16-bit` · `140 Hz` · `HC-05` · `Trinx / DTW` · `TensorFlow`

**[Repository →](https://github.com/mikey-7x/Project-Synapse-v1-official-Real-Time-Brainwave-Decoder-with-Android)**

</td>
<td width="50%" valign="top">

### Why only three

Because these are the three repositories that meet every condition at once: a written
architecture, results that can be checked, a reproducible build, and an explicit licence.

There is no plan to extend the mark for the sake of coverage. A repository either meets the
four conditions or it does not.

</td>
</tr>
</table>

## Platform — the stack I work in

| Layer | What it is | Where I work |
| --- | --- | --- |
| **Workloads** | Windows, Linux and Android applications | Win32 / Win64 binaries, ELF (glibc), Android (bionic, ART) |
| **Compatibility & runtime** | layers that translate one world into another | Wine + WoW64, Box64, Termux · PRoot |
| **Graphics & compute APIs** | what applications are written against | Vulkan, OpenGL / GLES, OpenCL |
| **Mesa user space** | the drivers behind those APIs | Turnip (Vulkan, Adreno), Zink (OpenGL → Vulkan), rusticl (OpenCL) |
| **Kernel & libc** | what the drivers stand on | Linux kernel DRM / MSM, scheduler, memory management, glibc vs bionic |
| **Silicon** | the hardware being addressed | Adreno 750 GPU, Hexagon NPU / DSP, Kryo CPU, Snapdragon 8 Gen 3 |

### Work areas

- **Vulkan on Adreno** — Turnip feature exposure, extension support and validation; version and
  profile work against what the hardware can hold; memory model, synchronisation and cache
  behaviour before throughput.
- **Mesa user space** — Zink (OpenGL on Vulkan), rusticl (OpenCL on Mesa), Gallium state
  trackers, shader caches, and isolating a driver fault down to a single call.
- **Kernel and hardware acceleration** — DRM / MSM power, scheduling and buffer handling;
  Adreno 750 and Hexagon utilisation and offload; where acceleration is real and where it
  silently falls back.
- **Platform and compatibility** — Termux and PRoot as the build and run environment, Box64 for
  x86_64 binaries, Wine + WoW64 for 32-bit Windows software in a 64-bit container, and X11 /
  Wayland sessions on a phone display.

## Method

```text
1 · problem       a workload that does not run, or a bench measurement that does not exist
2 · architecture  which layer owns the job, what each layer may assume, where it will fail
3 · drivers       Vulkan / OpenGL / OpenCL paths — correctness before speed, validation on device
4 · hardware      silicon limits, board bring-up, power and thermal budget — calculated, not guessed
5 · tooling       reproducible build path, pinned versions, scripted install
6 · evidence      measured numbers, checksums, and a self-check that runs on every push
7 · honesty       limits, safety rules and licence stated in the repository
```

## Toolchain and platform

<div align="center">

<img src="https://img.shields.io/badge/Vulkan-A41E22?style=flat-square&logo=vulkan&logoColor=white" alt="Vulkan">
<img src="https://img.shields.io/badge/Mesa-1F6F8B?style=flat-square" alt="Mesa">
<img src="https://img.shields.io/badge/Turnip-Adreno%20Vulkan-2f3640?style=flat-square" alt="Turnip">
<img src="https://img.shields.io/badge/Zink-GL%20on%20Vulkan-2f3640?style=flat-square" alt="Zink">
<img src="https://img.shields.io/badge/rusticl-OpenCL-2f3640?style=flat-square" alt="rusticl">
<img src="https://img.shields.io/badge/OpenGL%20%2F%20GLES-5586A4?style=flat-square&logo=opengl&logoColor=white" alt="OpenGL">
<img src="https://img.shields.io/badge/Wine%20%2B%20WoW64-7A1F1F?style=flat-square&logo=wine&logoColor=white" alt="Wine + WoW64">
<img src="https://img.shields.io/badge/Box64-4B5563?style=flat-square" alt="Box64">
<br>
<img src="https://img.shields.io/badge/Linux%20kernel-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux kernel">
<img src="https://img.shields.io/badge/DRM%20%2F%20MSM-2b3138?style=flat-square" alt="DRM / MSM">
<img src="https://img.shields.io/badge/glibc-A81D33?style=flat-square" alt="glibc">
<img src="https://img.shields.io/badge/bionic-3DDC84?style=flat-square" alt="bionic">
<img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=gnometerminal&logoColor=white" alt="Termux">
<img src="https://img.shields.io/badge/PRoot-2b3138?style=flat-square" alt="PRoot">
<br>
<img src="https://img.shields.io/badge/Snapdragon%208%20Gen%203-C8102E?style=flat-square&logo=qualcomm&logoColor=white" alt="Snapdragon 8 Gen 3">
<img src="https://img.shields.io/badge/Adreno%20750-C8102E?style=flat-square" alt="Adreno 750">
<img src="https://img.shields.io/badge/Hexagon%20NPU-C8102E?style=flat-square" alt="Hexagon NPU">
<img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash">
<br>
<img src="https://img.shields.io/badge/STM32-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white" alt="STM32">
<img src="https://img.shields.io/badge/AVR-A5C43D?style=flat-square&logo=arduino&logoColor=white" alt="AVR">
<img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" alt="ESP32">
<img src="https://img.shields.io/badge/RP2040-A22846?style=flat-square&logo=raspberrypi&logoColor=white" alt="RP2040">
<img src="https://img.shields.io/badge/Verilog-8A2BE2?style=flat-square&logo=v&logoColor=white" alt="Verilog">
<img src="https://img.shields.io/badge/Yosys-1B4D3E?style=flat-square&logo=verilog&logoColor=white" alt="Yosys">
<img src="https://img.shields.io/badge/KiCad-314CB0?style=flat-square&logo=kicad&logoColor=white" alt="KiCad">
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">

</div>

## Other work — no brand

These repositories are published on their own terms as utilities, experiments, studies and
archives. **They do not carry `POWERED BY [mikey:hexoid-sys]`.**

| Area | Repositories |
| --- | --- |
| **Graphics, drivers & compute** | [Termux-VLSI-Studio](https://github.com/mikey-7x/Termux-VLSI-Studio) · [Watari-ARM64-Studio](https://github.com/mikey-7x/Watari-ARM64-Studio) · [OpenROAD-on-Android](https://github.com/mikey-7x/OpenROAD-on-Android) |
| **Linux on Android** | [Termux-projects](https://github.com/mikey-7x/Termux-projects) · [About-Termux](https://github.com/mikey-7x/About-Termux) · [Linux](https://github.com/mikey-7x/Linux) · [Headless-firefox](https://github.com/mikey-7x/Headless-firefox) |
| **Compilers & tooling** | [latex-to-pdf](https://github.com/mikey-7x/latex-to-pdf) · [aider-termux-installer](https://github.com/mikey-7x/aider-termux-installer) · [Arch-Claude-CLI](https://github.com/mikey-7x/Arch-Claude-CLI) |
| **Instruments & measurement** | [FL meter](https://github.com/mikey-7x/FL-meter) · [4-bit synchronous BCD counter](https://github.com/mikey-7x/4-Bit-Synchronous-BCD-Counter) · [WL indicator](https://github.com/mikey-7x/WL-indicator) |
| **Biosignals** | [Project Synapse (original)](https://github.com/mikey-7x/Project-Synapse-Real-Time-Brainwave-Decoder-with-Android) |
| **Automotive & safety** | [DSS4 driver safety system](https://github.com/mikey-7x/DSS4-Driver-Safety-System) · [DSS driver safety system](https://github.com/mikey-7x/DSS-driver-safety-system) · [Homepulse](https://github.com/mikey-7x/Homepulse-Microbaot) |
| **Power & analog** | [TMCD tripolar MOSFET class-D amplifier](https://github.com/mikey-7x/TMCD-Amplifier-Tripolar-MOSFET-Class-D-Amplifier) · [Solar street-light driver teardown](https://github.com/mikey-7x/Solar-Street-Light-DC-LED-Driver) · [LTspice Library AutoSync](https://github.com/mikey-7x/LTspice-Library-AutoSync-HID-Blue-Pill-Implementation-) |
| **Industrial tooling** | [MicroWIN V4 / Win11 bypass](https://github.com/mikey-7x/MicroWIN-V4-Win11-Bypass) |
| **Security research** | [pf15](https://github.com/mikey-7x/pf15-penetration-fast-15) · [ngrok in Termux](https://github.com/mikey-7x/ngrok-how-to-use-ngrok-in-termux) |
| **Learning & archives** | [Applied Electronics Archive](https://github.com/mikey-7x/Applied-Electronics-Archive) · [Tensorflow in Android](https://github.com/mikey-7x/Tensorflow-in-Android) · [RTOD-yv8](https://github.com/mikey-7x/RTOD-yv8) |

**[View all 33 repositories →](https://github.com/mikey-7x?tab=repositories)**

## Working with this account

- **Issues first.** A bug report with the platform, the version and the first error line gets
  answered fastest.
- **Reproducibility matters.** Pin versions, publish commands, include checksums.
- **No medical, certified or guaranteed claims.** Where a project is experimental, it says so
  on the front page and in the licence.

## Contact

| | |
| --- | --- |
| **Email** | [chauhanyogesh9825@gmail.com](mailto:chauhanyogesh9825@gmail.com) |
| **GitHub** | [github.com/mikey-7x](https://github.com/mikey-7x) |
| **YouTube** | [youtube.com/@mikey-7x](https://youtube.com/@mikey-7x) |
| **Blog** | [rtod-yv8.blogspot.com](https://rtod-yv8.blogspot.com/?m=1) |
| **LinkedIn** | [linkedin.com/in/yogesh-r-chauhan-780005417](https://www.linkedin.com/in/yogesh-r-chauhan-780005417) |

## Licence and credit

Projects on this account are published under the **mikey-7x Strict Personal & Educational Use
Licence**: free for personal, hobbyist and educational use with attribution. Commercial,
industrial and clinical use require a separate signed written licence. Each repository carries
its own `LICENSE` file — read it before building.

If you reuse or adapt anything, keep this credit with the work:

```text
Created by mikey-7x
POWERED BY [mikey:hexoid-sys]        (owner repository and the three powered projects only)
Copyright © 2026 mikey-7x. All rights reserved.
GitHub:  https://github.com/mikey-7x
Email:   chauhanyogesh9825@gmail.com
```

<div align="center">

<img src="assets/mikey-hexoid-sys-mark.png" alt="mikey:hexoid-sys" width="120">

**`POWERED BY [mikey:hexoid-sys]`**

Copyright © 2026 mikey-7x. All rights reserved.

[Repositories](https://github.com/mikey-7x?tab=repositories) ·
[YouTube](https://youtube.com/@mikey-7x) ·
[Blog](https://rtod-yv8.blogspot.com/?m=1) ·
[LinkedIn](https://www.linkedin.com/in/yogesh-r-chauhan-780005417) ·
[Email](mailto:chauhanyogesh9825@gmail.com)

<sub>Published under a non-commercial, source-available licence. No affiliation with or
endorsement by any vendor named above. All technical statements describe areas of active
work; they are not benchmark results or certifications.</sub>

</div>
