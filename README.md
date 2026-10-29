<div align="center">

<img src="assets/profile-banner.png" alt="mikey-7x — embedded systems, tooling, Linux on mobile" width="100%">

<br>

<a href="https://github.com/mikey-7x?tab=repositories"><img src="https://img.shields.io/badge/repositories-33-2f3640?style=flat-square&labelColor=0f1114&logo=github&logoColor=white" alt="Repositories"></a>
<img src="https://img.shields.io/badge/focus-embedded%20%C2%B7%20tooling%20%C2%B7%20Linux%20on%20mobile-3c4043?style=flat-square&labelColor=0f1114" alt="Focus">
<img src="https://img.shields.io/badge/licence-non--commercial%20%C2%B7%20strict-b3261e?style=flat-square&labelColor=0f1114" alt="Licence">

<h1>mikey-7x</h1>

<p><b>Firmware, compilers and instruments — built, measured, documented.</b></p>

<p><code>POWERED BY [mikey:hexoid-sys]</code></p>

</div>

---

## About

I work at the boundary between electronics and software: measurement hardware, the firmware
that drives it, and the tooling that builds it — often on an Android phone instead of a
desktop.

My background is **Electronics and Communication**, and most of what I publish grew out of a
bench problem that needed solving: a frequency counter for a transmitter circuit, a
biological-signal front-end, a compiler that turns a phone into a build station, a driver
safety system, a VLSI toolchain running under Termux.

Every project here follows the same rules: state what the hardware really does, state what it
cannot do, publish the checks, and put the licence in plain language.

<div align="center">

<img src="assets/powered-by-mikey-hexoid-sys.png" alt="POWERED BY [mikey:hexoid-sys]" width="460">

</div>

## `[mikey:hexoid-sys]` — the engineering identity

`[mikey:hexoid-sys]` is the name that ties this work together: the build toolchain, the
firmware, the instrument projects and the documentation conventions.

| Layer | What it means in practice |
| --- | --- |
| **Build** | A universal cross-compilation engine that installs its own toolchains and compiles for 105 board entries from Termux or Linux |
| **Firmware** | Bare-metal and Arduino-core code for STM32, AVR, ESP32, RP2040, 8051 and iCE40 FPGA targets |
| **Instruments** | Measurement front-ends, counters, generators and decoders with their calculations published |
| **Documentation** | Limits, safety rules, checksums and machine-checked repository self-tests |
| **Identity** | The exact line `POWERED BY [mikey:hexoid-sys]` and the silver mark used across the account |

## Featured projects

<table>
<tr>
<td width="50%" valign="top">

### ⚙️ [mikey:hexoid v5.0.0](https://github.com/mikey-7x/mikey-hexoid-v5.0.0)

Universal embedded cross-compilation engine for Android (Termux) and Linux. 105 board
entries, AVR/STM32/ESP32/RP2040/8051 SDCC flows, iCE40 FPGA synthesis with nextPNR, plus a
library manager — all from a terminal menu.

`Bash` · `Python` · `Arduino CLI 0.35.3` · `Yosys/nextPNR` · `SDCC`

</td>
<td width="50%" valign="top">

### 🧠 [Project Synapse v1](https://github.com/mikey-7x/Project-Synapse-v1-official-Real-Time-Brainwave-Decoder-with-Android)

Single-channel EEG / subvocal-EMG acquisition chain: INA128 front-end, 16-bit ADS1115 at
140 Hz, framed Bluetooth link, Trinx segmentation, DTW matching and CNN-LSTM/GRU decoders.
Experimental prototype — not a medical device.

`Electronics` · `Signal processing` · `DTW` · `TensorFlow`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📡 [298.666 MHz frequency counter](https://github.com/mikey-7x/298.666mhz-frequency-counter-using-stm32f103c8t6-and-vhf-uhf-fm-transmitter-circuit)

STM32F103C8T6 counter and bench frequency generator with a VHF/UHF FM transmitter test
circuit. Timer-chaining measurement, OLED interface, compiled artifacts and measured results
included.

`STM32` · `Arduino/STM32duino` · `SSD1306` · `RF`

</td>
<td width="50%" valign="top">

### 🖥️ Linux on Android

Termux-first tooling: VLSI studio, ARM64 studio, OpenROAD, CLI installers and utilities for
running desktop-class workflows on a phone.

`Termux` · `PRoot` · `Arch Linux` · `X11`

</td>
</tr>
</table>

**[View all 33 repositories →](https://github.com/mikey-7x?tab=repositories)**

## Toolchain

<div align="center">

<img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash">
<img src="https://img.shields.io/badge/Verilog-8A2BE2?style=flat-square&logo=v&logoColor=white" alt="Verilog">
<img src="https://img.shields.io/badge/STM32-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white" alt="STM32">
<img src="https://img.shields.io/badge/AVR-A5C43D?style=flat-square&logo=arduino&logoColor=white" alt="AVR">
<img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" alt="ESP32">
<img src="https://img.shields.io/badge/RP2040-A22846?style=flat-square&logo=raspberrypi&logoColor=white" alt="RP2040">
<br>
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
<img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=gnometerminal&logoColor=white" alt="Termux">
<img src="https://img.shields.io/badge/Arch-1793D1?style=flat-square&logo=archlinux&logoColor=white" alt="Arch">
<img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/Yosys-1B4D3E?style=flat-square&logo=verilog&logoColor=white" alt="Yosys">
<img src="https://img.shields.io/badge/SDCC-6B7280?style=flat-square&logo=gnu&logoColor=white" alt="SDCC">
<img src="https://img.shields.io/badge/KiCad-314CB0?style=flat-square&logo=kicad&logoColor=white" alt="KiCad">
<img src="https://img.shields.io/badge/LTspice-900000?style=flat-square&logo=analogdevices&logoColor=white" alt="LTspice">
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">

</div>

## How I work

```text
1 · problem       a bench measurement or a workflow that does not exist yet
2 · hardware      circuit, gains, filters, timing budget — calculated, not guessed
3 · firmware      smallest correct loop, microsecond pacing, explicit framing
4 · tooling       reproducible build path, pinned versions, scripted install
5 · evidence      measured numbers, checksums, and a self-check that runs in CI
6 · honesty       limits, safety rules and licence stated in the repository
```

## Selected work

| Area | Repositories |
| --- | --- |
| **Instruments & measurement** | [298.666 MHz counter](https://github.com/mikey-7x/298.666mhz-frequency-counter-using-stm32f103c8t6-and-vhf-uhf-fm-transmitter-circuit) · [FL meter](https://github.com/mikey-7x/FL-meter) · [4-bit synchronous BCD counter](https://github.com/mikey-7x/4-Bit-Synchronous-BCD-Counter) · [WL indicator](https://github.com/mikey-7x/WL-indicator) |
| **Biosignals** | [Project Synapse v1](https://github.com/mikey-7x/Project-Synapse-v1-official-Real-Time-Brainwave-Decoder-with-Android) · [Project Synapse (original)](https://github.com/mikey-7x/Project-Synapse-Real-Time-Brainwave-Decoder-with-Android) |
| **Compilers & tooling** | [mikey:hexoid v5.0.0](https://github.com/mikey-7x/mikey-hexoid-v5.0.0) · [latex-to-pdf](https://github.com/mikey-7x/latex-to-pdf) · [aider-termux-installer](https://github.com/mikey-7x/aider-termux-installer) · [Arch-Claude-CLI](https://github.com/mikey-7x/Arch-Claude-CLI) |
| **VLSI & EDA on Android** | [Termux-VLSI-Studio](https://github.com/mikey-7x/Termux-VLSI-Studio) · [OpenROAD-on-Android](https://github.com/mikey-7x/OpenROAD-on-Android) · [Watari-ARM64-Studio](https://github.com/mikey-7x/Watari-ARM64-Studio) |
| **Linux on mobile** | [Termux-projects](https://github.com/mikey-7x/Termux-projects) · [About-Termux](https://github.com/mikey-7x/About-Termux) · [Linux](https://github.com/mikey-7x/Linux) · [Headless-firefox](https://github.com/mikey-7x/Headless-firefox) |
| **Automotive & safety** | [DSS4 driver safety system](https://github.com/mikey-7x/DSS4-Driver-Safety-System) · [DSS driver safety system](https://github.com/mikey-7x/DSS-driver-safety-system) · [Homepulse](https://github.com/mikey-7x/Homepulse-Microbaot) |
| **Power & analog** | [TMCD tripolar MOSFET class-D amplifier](https://github.com/mikey-7x/TMCD-Amplifier-Tripolar-MOSFET-Class-D-Amplifier) · [Solar street-light driver teardown](https://github.com/mikey-7x/Solar-Street-Light-DC-LED-Driver) · [LTspice Library AutoSync](https://github.com/mikey-7x/LTspice-Library-AutoSync-HID-Blue-Pill-Implementation-) |
| **Industrial tooling** | [MicroWIN V4 / Win11 bypass](https://github.com/mikey-7x/MicroWIN-V4-Win11-Bypass) |
| **Security research** | [pf15](https://github.com/mikey-7x/pf15-penetration-fast-15) · [ngrok in Termux](https://github.com/mikey-7x/ngrok-how-to-use-ngrok-in-termux) |
| **Learning & archives** | [Applied Electronics Archive](https://github.com/mikey-7x/Applied-Electronics-Archive) · [Tensorflow in Android](https://github.com/mikey-7x/Tensorflow-in-Android) · [RTOD-yv8](https://github.com/mikey-7x/RTOD-yv8) |

## What I am building next

- **`[mikey-7x:xfce4]`** — hardware-accelerated Linux desktop on Android, packaged so a phone
  becomes a usable workstation.
- Wider board coverage and reproducible toolchain pinning in **mikey:hexoid**.
- Better instrumentation for **Project Synapse**: more channels, proper anti-alias margin and
  session-wise evaluation.

## Working with this account

- **Issues first.** Every repository has templates; a bug report with the platform, version
  and the first error line gets answered fastest.
- **Reproducibility matters.** Pin versions, publish commands, include checksums.
- **No medical, certified or guaranteed claims.** Where a project is experimental, it says so
  on the front page and in the licence.

## Licence and credit

Projects on this account are published under the **mikey-7x Strict Personal & Educational Use
Licence**: free for personal, hobbyist and educational use with attribution. Commercial,
industrial and clinical use require a separate signed written licence. Each repository
carries its own `LICENSE` file — read it before building.

If you reuse or adapt anything, keep this credit with the work:

```text
Created by mikey-7x
POWERED BY [mikey:hexoid-sys]
Copyright © 2026 mikey-7x. All rights reserved.
GitHub: https://github.com/mikey-7x
```

<div align="center">

<img src="assets/mikey-hexoid-sys-mark.png" alt="mikey:hexoid-sys" width="128">

**`POWERED BY [mikey:hexoid-sys]`**

Copyright © 2026 mikey-7x. All rights reserved.

[Repositories](https://github.com/mikey-7x?tab=repositories) ·
[YouTube](https://youtube.com/@mikey-7x) ·
[Blog](https://rtod-yv8.blogspot.com/?m=1)

<sub>Published under a non-commercial, source-available licence. No affiliation with or
endorsement by any vendor named above.</sub>

</div>
