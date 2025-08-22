class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers is None:
            return 0
        delimiter = ","
        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(",")
        total = 0
        for p in parts:
            p = p.strip()
            if p == "":
                continue
            total += int(p)
        return total