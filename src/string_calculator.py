import re
from typing import List


class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        if numbers is None:
            return 0
        
        delimiters: List[str] = [',', '\n']
        nums_str = numbers

        # custom delimiter syntax starts with //
        if nums_str.startswith("//"):
            try:
                delim_spec, nums_str = nums_str.split("\n", 1)
            except ValueError:
                raise ValueError("Custom delimiter specification is malformed")

            delim_body = delim_spec[2:]

            if delim_body.startswith("[") and "]" in delim_body:
                found = re.findall(r'\[([^]]+)\]', delim_body)
                if found:
                    delimiters = found
                else:
                    # fallback to whole body if regex fails
                    delimiters = [delim_body]
            else:
                # single-char or multi-char without brackets
                delimiters = [delim_body]

        # build split pattern from delimiters (escape special regex chars)
        if delimiters:
            pattern = '|'.join(re.escape(d) for d in delimiters)
        else:
            pattern = ','
        
        parts = re.split(pattern, nums_str)
        total = 0
        negatives = []

        for p in parts:
            p= 0 if p==''else  int(p)
            if p < 0:
                negatives.append(p)
            elif p > 1000:
                continue
            else:
                total += p

        if negatives:
            raise ValueError("Negative numbers not allowed: " + ", ".join(map(str, negatives)))
        
        return total