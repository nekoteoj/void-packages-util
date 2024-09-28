import subprocess


def main():
    packages = []
    with open("./install.list", "r") as f:
        packages = f.read().split()

    print("Update repository")
    subprocess.run(["git", "pull", "origin", "master"])

    print("Update bootstrap")
    subprocess.run(["./xbps-src", "bootstrap-update"])

    for package in packages:
        print(f"Building {package}")
        subprocess.run(["./xbps-src", "pkg", package])


if __name__ == "__main__":
    main()
