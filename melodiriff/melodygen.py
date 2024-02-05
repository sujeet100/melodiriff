import random
import note

from bitstring import BitArray, pack


class MelodyGenerator:

    @staticmethod
    def generate():
        # 4 bars - 4 beats / bar - 4 subdivisions / beat = 64
        # Note(12) - Octave (0-3) - how long (1-8)
        # Note(4bits)-Octave(3 bits)-Duration(4bits) (all 0 is pause)
        # chromosome length = (4 + 2 + 4) * 64 = 640 (10 bits per subdivision)

        tempo = 80  # 80 bpm (beats per minute)

        # population =
        population = list(map(lambda x: MelodyGenerator.__get_four_bar_melody(), range(0, 1)))
        return population

    @staticmethod
    def __get_four_bar_melody():
        melody: BitArray = BitArray()
        for i in range(0, 64):
            z = MelodyGenerator.__get_note()
            melody += z
        return melody

    @staticmethod
    def __get_note() -> BitArray:
        note_number = random.randrange(1, 12, 1)
        binary_note = BitArray(f"uint4={note_number}")
        octave = random.randrange(0, 3, 1)
        octave_bitarray = BitArray(f"uint2={octave}")
        duration = random.randrange(1, 8, 1)
        duration_bitarray = BitArray(f"uint4={duration}")
        binary_note.append(octave_bitarray)
        binary_note.append(duration_bitarray)
        print(note_number, octave, duration)
        pause = BitArray(f"uint10=0")
        return pause if bool(random.getrandbits(1)) else binary_note

    @staticmethod
    def decode_binary_melody(bits: BitArray):
        print(bits)
        decoded_melody = list()
        for i in range(0, len(bits), 10):
            note_number, octave, duration = bits[i:i + 10].unpack('uint4, uint2, uint4')
            decoded_melody.append(note.Note(note_number, octave + 1, duration))
        return decoded_melody
