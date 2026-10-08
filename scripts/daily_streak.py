from datetime import date


def main() -> None:
    print(f"Daily streak check-in: {date.today().isoformat()}")


if __name__ == "__main__":
    main()
