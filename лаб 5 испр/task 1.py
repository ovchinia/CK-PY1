from pprint import pprint

def dic(i):
    return {"bin": str(bin(i)), "dec": i, "hex": str(hex(i)), "oct": str(oct(i))}

pprint([dic(i) for i in range(16)])
