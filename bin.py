with open("myfile", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        byte = f.read(1)


# in 3.8
with open("myfile", "rb") as f:
    while (byte := f.read(1)):
        # Do stuff with byte.


# https://www.devdungeon.com/content/working-binary-data-python
