from lot51_core.tunables.base_injection import BaseTunableInjection

import services
from sims4.tuning.tunable import TunableList, TunableReference
from sims4.tuning.tunable_base import GroupNames
from services import get_instance_manager
from sims4.resources import Types
from situations.situation_goal import TunableSituationGoalPreTestSet
from situations.situation_goal_targeted_sim import TunableTargetedSimTestSet
from lot51_core import logger
from lot51_core.utils.injection import inject_list


class TunableSituationGoalInjection(BaseTunableInjection):
    FACTORY_TUNABLES = {
        "situation_goal": TunableReference(manager=get_instance_manager(Types.SITUATION_GOAL), pack_safe=True),
        "_goal_loot_list": TunableList(description="\n            A list of pre-defined loot actions that will applied to every\n            sim in the situation when this situation goal is completed.\n             \n            Do not use this loot list in an attempt to undo changes made by\n            the RoleStates to the sim. For example, do not attempt\n            to remove buffs or commodities added by the RoleState.\n            ",
            tunable=(TunableReference(manager=(services.get_instance_manager(Types.ACTION)),
            class_restrictions=("SituationGoalLootActions", )))), 
        "_pre_tests": TunableSituationGoalPreTestSet(description="\n            A set of tests on the player sim and environment that all must\n            pass for the goal to be given to the player. e.g. Player Sim\n            has cooking skill level 7.\n            ",
            tuning_group=(GroupNames.TESTS)),
       "_target_tests": TunableTargetedSimTestSet(description="\n                A set of tests that a sim must to be a target of this goal.\n                ",
            tuning_group=(GroupNames.TESTS)), 
    }

    __slots__ = ("situation_goal", "_goal_loot_list", "_pre_tests", "_target_tests")

    def inject(self):
        if self.situation_goal is None:
            logger.warning("Failed to inject, situation_goal not found")
            return

        inject_list(self.situation_goal, "_goal_loot_list", self._goal_loot_list, debug=True)
        inject_list(self.situation_goal, "_pre_tests", self._pre_tests, debug=True)
        inject_list(self.situation_goal, "_target_tests", self._target_tests, debug=True)