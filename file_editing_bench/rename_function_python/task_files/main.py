from data_processor import p, load_json_file, save_json_file


def main():
    # Load input data
    input_data = [
        {"name": "john doe", "age": 30, "city": "new york"},
        {},  # Empty record to be filtered
        {"name": "jane smith", "age": 25, "city": "san francisco"},
    ]

    # Process the data
    processed_data = p(input_data)

    # Print results
    for record in processed_data:
        print(f"Processed record: {record}")


if __name__ == "__main__":
    main()