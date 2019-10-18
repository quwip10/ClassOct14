
class Instrument:

    def __init__(self, name, family):
        self.name = name
        self.family = family
        self._difficulty = 3

    def summarize(self):
        summary = "Instrument: " + self.name + "\n"
        summary += "Family: " + self.family + "\n"
        summary += "Difficulty: " + str(self._difficulty) + "\n"
        return summary

    # Property

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        value = int(value)
        if value < 1 or value > 5:
            raise ValueError("difficulty must be between 1 and 5")

        self._difficulty = value

    def __str__(self):
        return f"Instrument ({self.name})"


class StringInstrument(Instrument):

    def __init__(self, name):
        super().__init__(name, "string")


def main():
    # used for testing the Instrument class
    flute = Instrument("flute", "woodwind")
    flute.difficulty = 5
    print(flute.difficulty)

    drum = Instrument("drum set", "percussion")
    drum.difficulty = 1

    print(drum.difficulty)


if __name__ == "__main__":
    main()
