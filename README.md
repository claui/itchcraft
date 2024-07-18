# Itchcraft

Itchcraft is an alternative front-end program for commercial USB
bite-healers which work by locally heating up human skin.

Itchcraft supports Linux and is meant to be used on Linux-based
smartphones such as the [Librem 5](https://en.wikipedia.org/wiki/Librem_5).

## IMPORTANT SAFETY NOTICE – READ BEFORE USE

Here’s the **tl;dr**:

1. **Using a bite healer will cause pain.**

2. **Improper use of your bite healer may cause minor burns.**

3. **Take the same precautions as with the manufacturer’s original app.**

The long form:

Heat-based bite healers **heat up your skin**. That’s just how they
work. Using your bite healer will cause a short burst of heat-induced
pain. That burst of pain is necessary for your bite healer to work
effectively.

Itchcraft is an alternative front-end for your bite healer. If you use
Itchcraft with your bite healer, then your bite healer should do, at most,
the same things as if you were using the original manufacturer’s app.
That’s because the original app is also just a front-end, which talks
to your bite healer. It basically just tells the bite healer which
settings the app’s user has chosen. The actual treatment logic is inside
your bite healer. Itchcraft doesn’t override or modify any safety
features of your bite healer.

With that being said, there can always be bugs, especially in niche
software like Itchcraft, whose user base is tiny. Despite all efforts,
Itchcraft is still essentially a largely untested and unauthorized
control system for a medical(-ish) device. I therefore recommend that
you treat it as such, and that you consider the risk vs. benefit
trade-offs involved.

If you choose to try out Itchcraft, I recommend that you start with the
lowest settings. That’s the Child setting, with the option for sensitive
skin enabled, and the duration set to the shortest possible.

If you use a particular bite healer for the first time:
stick with the lowest settings.

If you’re unsure about using Itchcraft (rather than the original app)
with your bite healer:
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
the manufacturer. Remember that Itchcraft controls your bite healer just
like the original app does. Therefore, I strongly urge you to read and
follow those original instructions, no matter if you use Itchcraft or
the manufacturer’s original app.

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

If you own a USB bite healer and a Linux smartphone, you’ll likely need
an alternative to the vendor’s app, because vendors typically only
support Android or iOS but not Linux.

Itchcraft is the missing Linux app for your bite healer.

## Features

At the moment, Itchcraft offers only a single feature:

- Treat your insect bite with the lowest and safest setting:
  the setting for children with sensitive skin and the shortest possible
  duration.

More features, including a graphical front-end and stronger settings,
are planned.

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
