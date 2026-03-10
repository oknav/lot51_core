from adoption.adoption_tuning import _AdoptionSimData
from display_snippet_tuning import _PickerDisplaySnippet
from interactions.utils.tunable import TunableContinuation
import services
from sims4.resources import Types
from sims4.tuning.tunable import (
    TunableInterval,
    TunableReference,
    TunableTuple,
    TunableVariant,
)


class InteractionPickerVariant(TunableVariant):
    def __init__(self, *args, statistic_pack_safe=False, **kwargs):
        (super().__init__)(
            args,
            display_snippets=_PickerDisplaySnippet.TunableFactory(
                description="\n                Display snippet available to select.\n                "
            ),
            continuations=TunableContinuation(),
            picker_entries=TunableTuple(
                count=TunableInterval(
                    description="\n                    Define the number of Sims that must match the specified\n                    creation data. The lower bound is the minimum required\n                    number. The upper bound is the ideal number.\n                    ",
                    tunable_type=int,
                    default_lower=1,
                    default_upper=2,
                    minimum=1,
                ),
                creation_data=(_AdoptionSimData.TunableFactory()),
            ),
            timed_aspirations=TunableReference(
                manager=(services.get_instance_manager(Types.ASPIRATION)),
                class_restrictions="TimedAspiration",
                pack_safe=True,
            ),
            loot_on_picker_selection=TunableReference(
                manager=(services.get_instance_manager(Types.ACTION)),
                class_restrictions=("LootActions",),
            ),
            **kwargs,
        )
