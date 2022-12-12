from pprint import pprint

pprint([{"bin": str(bin(i)), "dec": i, "hex": str(hex(i)), "oct": str(oct(i))} for i in range(16)])
