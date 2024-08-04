# Itchcraft

Itchcraft is a technology demonstration for Linux-based smartphones
to interface with commercial USB bite-healers that work by locally
heating up human skin.

Itchcraft is meant for studying and as a proof of concept.  
It is **not safe to use for treating insect bites** on human skin, nor
for any other medical or therapeutical purpose.

Itchcraft supports Linux and is meant to be used on Linux-based
smartphones such as the [Librem 5](https://en.wikipedia.org/wiki/Librem_5).

## IMPORTANT SAFETY NOTICE – READ BEFORE USE

Here’s the **tl;dr**:

1. **Itchcraft is not meant for treating insect bites on human skin.**

2. **Using a bite healer causes pain, no matter which software you use.**

3. **Improper use of bite healers may cause minor burns.**

The long form:

Heat-based bite healers **heat up your skin**. That’s just how they
work. Using your bite healer will cause a short burst of heat-induced
pain. That burst of pain is necessary for your bite healer to work
effectively.

The purpose of Itchcraft is to study and demonstrate how a Linux-based
frontend that interfaces with bite healers might work. Unlike original
Android and iOS apps provided by bite healer vendors, Itchcraft only
serves to demonstrate a possible way how Linux-based smartphones might
interface with commercial bite healers.

In other words: Itchcraft is just a tech demo meant for studying and as
a proof of concept. Itchcraft is not intended, and not safe to use, for
treating insect bites or for any other medical or therapeutical purpose.

While using Itchcraft with a USB bite healer connected, I recommend that
you keep the bite healer away from human skin at all times.

## General safety advice on using bite healers

This section contains basic safety information for bite healers in
general.

Even though Itchcraft is **not meant to be used to drive bite healers**
on human skin, this section may still be very relevant for you. For
example, you might accidentally touch your bite healer while choosing to
experiment with Itchcraft, so it’s important to keep the following rules
in mind no matter what.

Please understand that there can always be bugs, especially in niche
software like Itchcraft, whose user base is tiny. Despite all efforts,
Itchcraft is essentially an untested technology demo that interfaces
with a USB bite healer for research and demonstrational purposes.  
I recommend that you keep that in mind, and that you consider the risk
vs. benefit trade-offs involved in experimenting.

When using any bite healer, I recommend that you start with the lowest
settings. That’s the Child setting, with the option for sensitive
skin enabled, and the duration set to the shortest possible.

If you use a particular bite healer for the first time:
stick with the lowest settings.

If you’re connecting any app (including Itchcraft) to your bite healer
for the first time:
stick with the lowest settings.

If you’re unsure whether the stronger settings are ok for you:
stick with the lowest settings.

If the affected area of your skin is particularly sensitive:
stick with the lowest settings.

If you know you’re particularly sensitive to skin irritation:
stick with the lowest settings.

If your treatment is not successful: you may want to wait several
minutes before you re-apply your bite healer to the same skin area.
Re-apply using the lowest settings.

Your bite healer comes with important safety and usage instructions by
the manufacturer. I strongly urge you to read and follow those original
instructions, no matter if you use Itchcraft or the manufacturer’s
original app for any purpose.

If you use Itchcraft or your bite healer improperly, you may experience
minor burn.

## Overview

### About bite healers

**Insect bite healers**, also called **heat sticks**, **heat pens**,
or **thermal sticks**, are small portable devices that allow you to
treat insect bites using heat.

For more info, see the article
[Heat pen](https://en.wikipedia.org/wiki/Heat_pen) on Wikipedia.

### USB form factor

Bite healers are typically battery-powered, but they also exist as
small USB sticks that are typically powered by a smartphone. That
form factor allows bite healers to be much smaller than their
counterparts which have a built-in battery.

### What Itchcraft can do for you

Itchcraft is a technology demo. As such, it is meant for studying,
research, and just to see how Linux and USB bite healers work together.

If you own a USB bite healer and a Linux smartphone, Itchcraft may be
interesting to you for those purposes.

### What Itchcraft is not

- Itchcraft is not affiliated with, nor endorsed by, any manufacturer
  of bite healers.

- Itchcraft is not the missing Linux app for your bite healer.  
  It is not an alternative to the vendor’s original app for treatment
  purposes, even though vendors typically only support Android or iOS
  and not Linux.

- Itchcraft is not meant for use to treat insect bites.  
  In fact, Itchcraft is not intended for any medical or therapeutical
  purpose whatsoever.

- Itchcraft is not meant to be used on human skin.

## Features

At the moment, Itchcraft offers the following features:

- Activate a technical demonstration of your insect bite healer
  using the command line

- Choose a duration: short, medium, or long

- Choose a generation: child or adult

- Choose a skin sensitivity level: regular skin or sensitive skin

- Show a list of connected bite healers

A graphical front-end is planned.

## System requirements

To use Itchcraft, you need:

- a Linux-based smartphone with a working USB;

- and a USB bite healer that Itchcraft supports (see next section
  for details).

## Supported USB bite healers

Currently, Itchcraft supports only a single bite healer model, the
[heat it](https://just-heat-it.co.uk/)® by the German manufacturer
Kamedi GmbH. I am not affiliated with Kamedi but I’m personally very
satisfied with their products.

All trademarks mentioned are the property of their respective owners.

## Installation

### Installing from PyPI

To install Itchcraft from PyPI, open a shell and run:

```shell
pip install itchcraft
```

If that doesn’t work, try:

```shell
python3 -m pip install itchcraft
```

### Installing from the AUR

Direct your favorite
[AUR helper](https://wiki.archlinux.org/title/AUR_helpers) to the
`itchcraft` package.

## Usage

```shell
itchcraft COMMAND
```

See [`USAGE.md`](https://github.com/claui/itchcraft/blob/main/USAGE.md)
or `man itchcraft` for details.

## Contributing to Itchcraft

See [`CONTRIBUTING.md`](https://github.com/claui/itchcraft/blob/main/CONTRIBUTING.md).

## Frequently asked questions

### Is Itchcraft safe to use for treating insect bites?

**tl;dr** No, Itchcraft is not safe to use for any medical purpose.

Itchcraft is just a tech demo. I strongly discourage you from ever using
it for any medical purpose. In particular, it is not safe to use for
treating insect bites nor any other use on human skin.

### Why is Itchcraft not safe to use for insect bite treatment?

**tl;dr** Approval too costly. Requirements not met. Not a project goal.

If you experiment with Itchcraft with bite healers on human skin despite
the recommendations not to do so, you may get the superficial impression
that Itchcraft does the same thing as the original vendor-provided apps.

Even if your observation were correct, you must understand that
Itchcraft hasn’t been developed with the same level of quality assurance
as the original apps. Itchcraft doesn’t have the necessary government
approval for medical devices in any country of the world. This means
that Itchcraft is not safe for medical or therapeutical use on human
skin, despite your observations that Itchcraft may usually do the same
thing as the vendor’s apps do. Lastly, treating insect bites is not a
goal of the Itchcraft project.

### Will Itchcraft ever be safe to use for treating insect bites?

**tl;dr** Most likely, it won’t.

Obtaining the necessary approval for medical devices is prohibitively
costly and difficult in most legislations, especially for non-commercial
products.

As a project mainly intended for studying and as a tech demo, Itchcraft
doesn’t have any formal software development, quality assurance or
quality control process that would be required for approval as a medical
device.

In a nutshell, Itchcraft is unlikely to ever evolve into an app for
treating insect bites or for any other medical or therapeutical use.

## Legal notice

This document includes some general information and safety advice about
bite healers. However, that information is not intended as medical advice.
For medical advice, you should always consult a doctor. If you’re unsure
whether you can safely use a bite healer, consult with a healthcare
professional before using Itchcraft or any bite healer.

See also section 8 of the [LICENSE](LICENSE):

> Limitation of Liability. In no event and under no legal theory,
> whether in tort (including negligence), contract, or otherwise,
> unless required by applicable law (such as deliberate and grossly
> negligent acts) or agreed to in writing, shall any Contributor be
> liable to You for damages, including any direct, indirect, special,
> incidental, or consequential damages of any character arising as a
> result of this License or out of the use or inability to use the
> Work (including but not limited to damages for loss of goodwill,
> work stoppage, computer failure or malfunction, or any and all
> other commercial damages or losses), even if such Contributor
> has been advised of the possibility of such damages.

Itchcraft is not affiliated with, nor endorsed by, any manufacturer of
bite healers.

Particularly, Itchcraft is not affiliated with, nor endorsed by,
Kamedi GmbH.

All trademarks mentioned are the property of their respective owners.

## License

Copyright (c) 2024 Claudia Pellegrino

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).
