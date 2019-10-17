from instrument import Instrument


class InstrumentDb:

    def __init__(self, path="./data/local_instruments.txt"):
        self._path = path
        self._delimiter = "|"
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


# ----------------

def main():
    db = InstrumentDb()

    db.load()

    bongo = Instrument("bongo", "percussion")
    bongo.difficulty = 3
    db.instruments.append(bongo)

    db.save()


if __name__ == "__main__":
    main()
