<!-- markdownlint-configure-file { "MD041": { "level": 1 } } -->

# Safety notice

1. **Itchcraft is not meant for treating insect bites on human skin.**

2. **Using a bite healer causes pain, no matter which software you use.**

3. **Improper use of bite healers may cause minor burns.**

# Synopsis

```shell
itchcraft COMMAND
```

# Commands

`COMMAND` is one of the following:

`info`
: Shows a list of USB bite healers that are connected to the host.

`start`
: Activates (i.e. heats up) a connected USB bite healer for
: demonstration purposes.

# Flags

The `info` command does not support any flags.

The `start` command supports the following flags:

## `-d`, `--duration=DURATION`

The duration of the demonstration.

One of `short`, `medium`, or `long`.

The default is `short`, the safest setting.

## `-g`, `--generation=GENERATION`

Whether the demonstration corresponds to treating an adult or a child.

One of the values `child` or `adult`.

The default is `child`, the safer setting of the two.

## `-s`, `--skin_sensitivity=SKIN_SENSITIVITY`

Whether the tech demo caters to regular or particularly sensitive skin.

One of the values `regular` or `sensitive`.

The default is `sensitive`, the safer setting of the two.

# Environment

Itchcraft supports the following environment variable:

`DEBUG`
: If set to a non-zero value, causes Itchcraft to enable debug-level
: logging. Also decreases some retry counters and prints stack traces
: for errors where it normally wouldn’t.

# Monitoring the bite healer’s state once activated

## Monitoring the state by observing the LED color (recommended)

Your bite healer has a built-in LED, whose color tells you when the
ceramic end of your bite healer is currently heating up, when it has
finished heating up, and when it reverts to its default idle state.

To start the technical demonstration, follow these steps:

1. Connect the bite healer to the USB port of your smartphone.

2. Confirm that the built-in LED is pulsating (either **red** or
   **green**.)

3. Run the `itchcraft start` command from a shell.

4. Wait until the built-in LED turns **purple**. It will also blink
   rapidly. The bite healer is now heating up.  
   This phase should take only a couple of seconds until the bite healer
   has reached its target temperature.  
   If you were using the original vendor-provided app instead of this
   demonstration, then the heating-up phase would mean that your bite
   healer is not yet ready for use.  
   Do not worry if you notice the CLI exiting back to the shell at this
   point. Your bite healer will perform the rest of the demonstration
   on its own.

5. As soon as the built-in LED turns **blue** and no longer blinks,
   the bite healer has reached its target temperature.  
   If you were using the original vendor-provided app instead of this
   demonstration, this phase would mean that your bite healer is ready
   to use on the affected area of your skin.  
   It is recommended that you do not let your bite healer come in
   contact with human skin while using Itchcraft.

6. If you were using the original vendor-provided app instead of
   Itchcraft, you’d be pressing your bite healer against the affected
   area of your skin as long as its LED shows a blue light.  
   **Do not let your bite healer touch human skin while using Itchcraft.**

7. Once the LED turns back to a pulsating **green**, your bite healer
   has reverted to its idle state.  
   If you were using the original vendor-provided app instead of
   Itchcraft, you’d be removing your bite healer from your skin at this
   point.  
   Your bite healer is now ready for another demonstration.

## Monitoring the state if you have color vision deficiencies

If you find yourself unable to discern the different colors on the LED
built into your bite healer, follow these steps to achieve the same
result:

1. Connect the bite healer to the USB port of your smartphone.

2. Confirm that the built-in LED is pulsating.

3. Run the `itchcraft start` command from a shell.

4. Wait until the built-in LED starts blinking rapidly. The bite healer
   is now heating up.  
   This phase should take only a couple of seconds until the bite healer
   has reached its target temperature.  
   If you were using the original vendor-provided app instead of this
   demonstration, then the heating-up phase would mean that your bite
   healer is not yet ready for use.  
   Do not worry if you notice the CLI exiting back to the shell at this
   point. Your bite healer will perform the rest of the demonstration
   on its own.

5. As soon as the built-in LED stays lit and no longer blinks, the bite
   healer has reached its target temperature.  
   If you were using the original vendor-provided app instead of this
   demonstration, this phase would mean that your bite healer is ready
   to use on the affected area of your skin.  
   It is recommended that you do not let your bite healer come in
   contact with human skin while using Itchcraft.

6. If you were using the original vendor-provided app instead of
   Itchcraft, you’d be pressing your bite healer against the affected
   area of your skin as long as its LED shows a non-blinking,
   non-pulsating light.  
   **Do not let your bite healer touch human skin while using Itchcraft.**

7. Once the LED starts pulsating and no longer stays lit, your bite healer
   has reverted to its idle state.  
   If you were using the original vendor-provided app instead of
   Itchcraft, you’d be removing your bite healer from your skin at this
   point.  
   Your bite healer is now ready for another demonstration.
