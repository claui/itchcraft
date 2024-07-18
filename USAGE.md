<!-- markdownlint-configure-file { "MD041": { "level": 1 } } -->

# Safety notice

1. **Using a bite healer will cause pain.**

2. **Improper use of your bite healer may cause minor burns.**

3. **Take the same precautions as with the manufacturer’s original app.**

# Synopsis

```shell
itchcraft COMMAND
```

# Commands

`COMMAND` is one of the following:

`treat`
: Treats your insect bite using a connected USB bite healer.

# Treatment

## Treatment method guided by LED color (recommended)

Your bite healer has a built-in LED, whose color tells you if it’s safe
to apply the bite healer to your skin. After invoking Itchcraft, look
closely at the built-in LED to figure out when to start and stop
applying the bite healer to your skin.

Follow these steps:

1. Connect the bite healer to the USB port of your smartphone.

2. Confirm that the built-in LED is pulsating (either **red** or
   **green**.)

3. Run the `itchcraft treat` command from a shell.

4. Wait until the built-in LED turns **purple**. It will also blink
   rapidly. Do not apply the bite healer to your skin yet.  
   This phase should take only a couple of seconds until the bite healer
   has reached its target temperature for treatment.  
   Do not worry if you notice the CLI exiting back to the shell at this
   point. Your bite healer will perform the treatment on its own.

5. As soon as the built-in LED turns **blue** and no longer blinks,
   apply the bite healer immediately by pressing it firmly against the
   affected area of your skin.

6. Keep pressing as long as the built-in LED stays blue. This should
   take a couple of seconds.

7. Once the LED turns back to a pulsating **green**, remove the bite
   healer from your skin immediately.

## Method for people with color vision deficiencies

If you find yourself unable to discern the different colors on the LED
built into your bite healer, follow these steps to achieve the same
result:

1. Connect the bite healer to the USB port of your smartphone.

2. Confirm that the built-in LED is pulsating.

3. Run the `itchcraft treat` command from a shell.

4. Wait until the built-in LED starts blinking rapidly.
   Do not apply the bite healer to your skin yet.  
   This phase should take only a couple of seconds until the bite healer
   has reached its target temperature for treatment.
   Do not worry if you notice the CLI exiting back to the shell at this
   point. Your bite healer will perform the treatment on its own.

5. As soon as the built-in LED stays lit and no longer blinks, apply the
   bite healer immediately by pressing it firmly against the affected
   area of your skin.

6. Keep pressing as long as the built-in LED stays lit. This should take
   a couple of seconds.

7. Once the LED starts pulsating and no longer stays lit, remove the
   bite healer from your skin immediately.
