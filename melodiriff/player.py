import time
import bitstring
import melodygen
import pygame

from melodiriff.melody_config import MelodyConfig
from melodiriff.note import Note


class Player:
    @staticmethod
    def play_note(note: Note, melody_config: MelodyConfig):
        if note.number == 0:
            pygame.time.wait(int(60 / melody_config.bpm * 1000))
            return
        pygame.mixer.init()
        pygame.mixer.music.load(f"../assets/notes/{Note.note_number_to_name[note.number]}{note.octave}.wav")
        pygame.mixer.music.play()
        #pygame.time.wait(int(60 / melody_config.bpm * note.duration * 1000))
        pygame.time.wait(int(60 / melody_config.bpm * 1000))
        pygame.mixer.music.stop()


if __name__ == '__main__':
    population = melodygen.MelodyGenerator.generate()
    melody_config = MelodyConfig(120)
    first_melody = melodygen.MelodyGenerator.decode_binary_melody(population[0])

    print("decoded melody", first_melody)

    for note in first_melody:
        print("playing", note)
        Player.play_note(note, melody_config)

    time.sleep(20)
