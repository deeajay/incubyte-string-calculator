class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers is None:
            return 0
        # Handle custom delimiters
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_end = numbers.index("\n")
            delimiter = numbers[2:delimiter_end]
            numbers = numbers[delimiter_end + 1:]
        
        numbers = numbers.replace("\n", delimiter)
        
        parts = numbers.split(delimiter)
        total = 0
        negatives = []

        for p in parts:
            p= 0 if p==''else  int(p)
            if p < 0:
                negatives.append(p)
            else:
                total += p

        if negatives:
            raise ValueError("Negative numbers not allowed: " + ", ".join(map(str, negatives)))
        
        return total