from dataclasses import dataclass
from typing import List, Optional, Tuple

from flaxlight.types.blockchain_format.program import Program
from flaxlight.types.blockchain_format.sized_bytes import bytes32
from flaxlight.wallet.lineage_proof import LineageProof
from flaxlight.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CCInfo(Streamable):
    limitations_program_hash: bytes32
    my_genesis_checker: Optional[Program]  # this is the program
    lineage_proofs: List[Tuple[bytes32, Optional[LineageProof]]]  # {coin.name(): lineage_proof}
