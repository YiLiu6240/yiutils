from yiutils.project_utils import find_project_root


def main():
    root = find_project_root(anchor_file="environment.yml")
    print(root)


if __name__ == "__main__":
    main()
