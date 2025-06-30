def calculate_chunk_start_end(
    chunk_id: int,
    num_chunks: int,
    data_length: int,
    pilot_num_docs: int = 20,
    pilot: bool = False,
    verbose: bool = False,
):
    """
    Calculate startpoint and endpoint for a chunk of data to process.

    Parameters:
        chunk_id (int): The chunk index (e.g. from SLURM array task id).
        num_chunks (int): The total number of chunks.
        data_length (int): Total number of documents in the data.
        pilot_num_docs (int): Number of documents to process in pilot mode.
        pilot (bool): If True, always return (0, min(pilot_num_docs, data_length)).
        verbose (bool): If True, print debug information.

    Returns:
        (startpoint, endpoint): Tuple of indices for slicing.
        If startpoint >= data_length, returns (None, None).
    """
    if pilot:
        startpoint = 0
        endpoint = min(pilot_num_docs, data_length)
        if verbose:
            print(
                f"[chunking] pilot mode: startpoint=0, "
                f"endpoint=min({pilot_num_docs}, {data_length}) = {endpoint}"
            )
        return startpoint, endpoint

    # Divide the data into num_chunks chunks as evenly as possible
    chunk_size = (data_length + num_chunks - 1) // num_chunks  # ceil division

    startpoint = chunk_id * chunk_size
    endpoint = min(startpoint + chunk_size, data_length)

    if verbose:
        print(
            f"[chunking] chunk_id={chunk_id}, num_chunks={num_chunks}, data_length={data_length}, "
            f"chunk_size={chunk_size} => startpoint={startpoint}, endpoint={endpoint}"
        )

    if startpoint >= data_length:
        if verbose:
            print(
                f"[chunking] startpoint ({startpoint}) >= data_length ({data_length}): returning (None, None)"
            )
        return None, None
    return startpoint, endpoint

