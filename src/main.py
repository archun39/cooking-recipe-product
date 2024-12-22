import input, model
def main():
    script = input.InputManager().read_file(1)
    gpt = model.ModelManager()
    res = gpt.get_summary(script)

    print(res)

if __name__ == "__main__":
    main()