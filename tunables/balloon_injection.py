import services
from balloon.balloon_variant import BalloonVariant
from sims4.resources import Types
from sims4.tuning.tunable import (
    TunableList,
    TunableReference,
)

from lot51_core import logger
from lot51_core.tunables.base_injection import BaseTunableInjection
from lot51_core.utils.injection import inject_list


class TunableBalloonInjection(BaseTunableInjection):
    FACTORY_TUNABLES = {
        "balloon": TunableReference(
            manager=services.get_instance_manager(Types.BALLOON)
        ),
        "balloons": TunableList(
            description="\n             The list of possible balloons.\n             ",
            tunable=(BalloonVariant.TunableFactory(balloon_type=None)),
        ),
    }
    __slots__ = ("balloon", "balloons")

    def inject(self):
        if self.balloon is None:
            logger.warning("Failed to inject, balloon not found")
            return

        inject_list(self.balloon, "balloons", self.balloons, debug=True)
