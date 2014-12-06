def safe_input(prompt):
    try:
        return raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None

if __name__ == '__main__':
    print safe_input("enter a number between 1 and 10: ")
