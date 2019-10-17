
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


def main():
    # used for testing the Instrument class
    i1 = Instrument("flute", "woodwind")
    i2 = Instrument("drum set", "percussion")

    print(i1.summarize())
    print(i2.summarize())


if __name__ == "__main__":
    main()
