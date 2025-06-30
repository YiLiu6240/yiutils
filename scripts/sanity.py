from yiutils.chunking import calculate_chunk_start_end
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
        )
        print(f"Task ID {task_id}: startpoint={startpoint}, endpoint={endpoint}")


def sanity_check_find_root():
    root = find_project_root(anchor_file="environment.yml")
    print(root)


def main():
    print("Running sanity checks...")

    print("Finding project root...")
    sanity_check_find_root()

    print("Checking chunking calculations...")
    sanity_check_chunking()


if __name__ == "__main__":
    main()
