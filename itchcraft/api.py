"""The primary module in itchcraft."""

import usb.core  # type: ignore
import usb.util  # type: ignore

from .errors import CliError
from .heat_it import HeatItDevice
from .logging import get_logger

logger = get_logger(__name__)


# pylint: disable=too-few-public-methods
class Api:
    """Tech demo for interfacing with heat-based USB insect bite healers"""

    def start(self) -> None:  # pylint: disable=no-self-use
        """Activates (i.e. heats up) a connected USB bite healer for
        demonstration purposes.
        """

        logger.warning('This app is only a tech demo')
        logger.warning('and NOT for medical use.')
        logger.warning('The app is NOT SAFE to use')
        logger.warning('for treating insect bites.')

        logger.info('Searching for bite healer')
        dev: usb.core.Device = usb.core.find(
            idVendor=0x32F9, idProduct=0xFCBA
        )

        if not dev:
            raise CliError('USB device not found')

        logger.info(
            'Found `%s` bite healer, S/N: %s',
            dev.product,
            dev.serial_number,
        )

        dev.set_configuration()
        config = dev.get_active_configuration()
        interface = config[(0, 0)]
        endpoint_out = usb.util.find_descriptor(
            interface,
            custom_match=_match_out,
        )
        endpoint_in = usb.util.find_descriptor(
            interface,
            custom_match=_match_in,
        )

        if not endpoint_out or not endpoint_in:
            raise CliError('Unable to access USB endpoint')

        heatit = HeatItDevice(dev, endpoint_out, endpoint_in)

        heatit.self_test()
        logger.debug('Response: %s', heatit.preheat().hex(' '))

        logger.info('Device now preheating.')
        logger.info('Watch the LED closely.')
        logger.info('It will blink purple, then stop')
        logger.info('and light up blue.')

        logger.warning('While using this app, your')
        logger.warning('bite healer is NOT SAFE for')
        logger.warning('use on human skin.')

        logger.info('Once the LED turns green,')
        logger.info('the tech demo has completed.')


def _match_in(device: usb.core.Device) -> bool:
    address = device.bEndpointAddress
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_IN
    )


def _match_out(device: usb.core.Device) -> bool:
    address = device.bEndpointAddress
    return bool(
        usb.util.endpoint_direction(address) == usb.util.ENDPOINT_OUT
    )
