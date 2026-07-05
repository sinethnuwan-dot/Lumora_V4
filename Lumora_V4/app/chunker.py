from math import ceil


def chunk_symbols(
    symbols: list[str],
    chunk_size: int,
) -> list[list[str]]:
    """
    Split symbols into chunks.

    Example:

    530 symbols
    chunk_size = 10

    Result:
    [
        [10],
        [10],
        ...
    ]
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    chunks = []

    for i in range(0, len(symbols), chunk_size):
        chunks.append(
            symbols[i:i + chunk_size]
        )

    return chunks


if __name__ == "__main__":

    symbols = [f"COIN{i}" for i in range(1, 31)]

    result = chunk_symbols(
        symbols,
        10,
    )

    print(result)

    print()

    print(f"Chunks : {len(result)}")

    print(f"Total Symbols : {sum(len(x) for x in result)}")