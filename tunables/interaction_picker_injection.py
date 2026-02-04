from lot51_core.interactions.picker_interaction import InteractionPickerVariant
import services
from lot51_core import logger
from lot51_core.tunables.base_injection import BaseTunableInjection
from lot51_core.utils.injection import inject_list
from sims4.resources import Types
from sims4.tuning.tunable import (
    Tunable,
    TunableReference,
    TunableList,
)
from sims4.tuning.tunable_base import GroupNames


class TunablePickerInteractionInjection(BaseTunableInjection):
    FACTORY_TUNABLES = {
        "interaction": TunableReference(
            manager=(services.get_instance_manager(Types.INTERACTION))
        ),
        "target_list_name": Tunable(tunable_type=str, default="N/A"),
        "to_inject": TunableList(
            description="\n            The list of tunings to inject.\n            ",
            tunable=(InteractionPickerVariant(statistic_pack_safe=True)),
            unique_entries=True,
            tuning_group=(GroupNames.PICKERTUNING),
        ),
    }
    __slots__ = ("interaction", "target_list_name", "to_inject")

    @property
    def _target_list_name_valid(self):
        return bool(self.target_list_name) and self.target_list_name != "N/A"

    def inject(self):
        if self.interaction is None:
            logger.warning("Failed to inject, interaction not found")
            return
        if not self._target_list_name_valid:
            logger.warning("Failed to inject, target_list_name is invalid")
            return

        inject_list(self.interaction, self.target_list_name, self.to_inject, debug=True)
