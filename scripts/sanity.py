from yiutils.chunking import calculate_chunk_start_end
from yiutils.failsafe import failsafe
from yiutils.project_utils import find_project_root


def sanity_check_chunking():
    data_length = 7000
    pilot = False
    array_length = 30
    pilot_num_docs = 100

    for task_id in range(array_length):
        startpoint, endpoint = calculate_chunk_start_end(
            chunk_id=task_id,
            num_chunks=array_length,
            data_length=data_length,
            pilot_num_docs=pilot_num_docs,
            pilot=pilot,
            verbose=True,
        )
        print(
            f"Task ID {task_id}: startpoint={startpoint}, endpoint={endpoint}"
        )


def sanity_check_find_root():
    root = find_project_root(anchor_file="environment.yml")
    print(root)


@failsafe
def divide_with_failsafe(a, b):
    """Example function demonstrating failsafe decorator usage."""
    return a / b


@failsafe(silent=True)
def risky_operation(data):
    """Example of failsafe with silent error handling."""
    if not data:
        raise ValueError("Data cannot be empty")
    return len(data) * 2


def sanity_check_failsafe():
    """Demonstrate various uses of the failsafe decorator."""
    # ==== Successful operation ====
    # expect: Success: 5.0, error: True, context: None
    result, error, context = divide_with_failsafe(10, 2)
    print(f"Success: {result}, error: {error}, context: {context}")

    # ==== Failed operation with warning ====
    # expect: Failure: None, error: ZeroDivisionError, context: {'a': 10, 'b': 0}
    result, error, context = divide_with_failsafe(10, 0)
    print(
        f"Failure: {result}, error: {type(error).__name__}, context: {context}"
    )

    # ==== Silent failure ====
    # expect: Silent failure: None, error: ValueError, context: {'data': ''}
    result, error, context = risky_operation("")
    print(
        f"Silent failure: {result}, error: {type(error).__name__}, context: {context}"
    )

    # ==== Silent success ====
    # expect: Silent success: 8, error: True, context: None
    result, error, context = risky_operation("test")
    print(f"Silent success: {result}, error: {error}, context: {context}")


def main():
    print("Running sanity checks...")

    print("Finding project root...")
    sanity_check_find_root()

    print("Checking chunking calculations...")
    sanity_check_chunking()

    print("Testing failsafe decorator...")
    sanity_check_failsafe()


if __name__ == "__main__":
    main()
