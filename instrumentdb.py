from instrument import Instrument


class InstrumentDb:

    default_delimiter = "|"  # class level, not associated with self, but is with cls

    def __init__(self, path="./data/local_instruments.txt"):
        self._path = path
        self._delimiter = default_delimiter
        self.instruments = []

    def load(self):
        self.instruments.clear()
        with open(self._path, "r") as file_in:
            for line in file_in:
                name, family, difficulty = line.strip().split(self._delimiter)
                instrument = Instrument(name, family)
                instrument.difficulty = difficulty
                self.instruments.append(instrument)

    def save(self):

        self.instruments.sort(key=lambda inst: inst.name)

        with open(self._path, "w") as file_out:
            for instrument in self.instruments:
                line = f"{instrument.name}|{instrument.family}|{instrument.difficulty}\n"
                file_out.write(line)

    @classmethod
    def get_default_delimiter(cls):
        return cls.default_delimiter


# ----------------

def main():

    delimiter = InstrumentDb.get_default_delimiter()

    db = InstrumentDb()

    db.load()

    bongo = Instrument("bongo", "percussion")
    bongo.difficulty = 3
    db.instruments.append(bongo)

    db.save()


if __name__ == "__main__":
    main()
