import input, model
def main():
    script = input.InputManager().read_file(4) # 1~4
    gpt = model.ModelManager()
    res = gpt.get_summary(script)
    print(res)


if __name__ == "__main__":
    main()