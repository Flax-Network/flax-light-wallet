from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "flaxlight_harvester flaxlight_timelord_launcher flaxlight_timelord flaxlight_farmer flaxlight_full_node flaxlight_wallet".split(),
    "node": "flaxlight_full_node".split(),
    "harvester": "flaxlight_harvester".split(),
    "farmer": "flaxlight_harvester flaxlight_farmer flaxlight_full_node flaxlight_wallet".split(),
    "farmer-no-wallet": "flaxlight_harvester flaxlight_farmer flaxlight_full_node".split(),
    "farmer-only": "flaxlight_farmer".split(),
    "timelord": "flaxlight_timelord_launcher flaxlight_timelord flaxlight_full_node".split(),
    "timelord-only": "flaxlight_timelord".split(),
    "timelord-launcher-only": "flaxlight_timelord_launcher".split(),
    "wallet": "flaxlight_wallet flaxlight_full_node".split(),
    "wallet-only": "flaxlight_wallet".split(),
    "introducer": "flaxlight_introducer".split(),
    "simulator": "flaxlight_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
