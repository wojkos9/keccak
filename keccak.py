
def pad_data(data: list[int]) -> list[int]:
    return data #TODO

def sha3_256_enc(data: bytes):
    r = 256
    l = 6
    padded = pad_data(data)

if __name__ == "__main__":
    msg = "abcd"
    data = msg.encode('ascii')
    print(data)

# data:
# 1, 1, 0
# padding:
# 1, 1, 0, 1, 0, 0, ..., 1 x r=256