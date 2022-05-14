class HashErrors:
    m = [
        "Hash read successfully!",

        "No salt! Generating one...",
        "Empty salt! Generating one...",

        "No hash! Generating one...",
        "Empty hash! Generating one..."
    ]

    HASHE_SUCCESS = 0

    HASHE_NOSALT = 1
    HASHE_EMPTYSALT = 2

    # TODO:
    HASHE_NOHASH = 3
    HASHE_EMPTYHASH = 4

CFG_NOTFOUND = "Config file \"%s\" not found! Exiting..."
CFG_EMPTY = "It appears that your config file \"%s\" is empty! Exiting..."
