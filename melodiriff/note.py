from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Note:
    number: int
    octave: int
    duration: int

    note_values: ClassVar = {
        "C": 1,
        "Db": 2,
        "D": 3,
        "Eb": 4,
        "E": 5,
        "F": 6,
        "Gb": 7,
        "G": 8,
        "Ab": 9,
        "A": 10,
        "Bb": 11,
        "B": 12
    }

    note_number_to_name: ClassVar = {v: k for k, v in note_values.items()}
