def read_molecule(reader):
    """(file open for reading) -> list or NoneType

    Read a single molecule from reader and return it, or return None to signal =
    end of file. The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    """

    line = reader.readline()
    if not line:
        return None
    key, name = line.split()

    molecule = [name]
    reading = True

    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, name, atom_type, x, y, z = line.split()
            molecule.append([atom_type, x, y, z])

        return molecule

