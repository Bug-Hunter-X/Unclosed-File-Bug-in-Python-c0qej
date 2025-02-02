def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... process the file contents safely here ...
            for line in f:
                #Do something with the line
                print(line)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        