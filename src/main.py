import input, model
def main():
    script = input.InputManager().read_file(4) # 1~4
    gpt = model.ModelManager()

    if(gpt.is_cooking_script(script)):
        data = gpt.preprocessing_data(script)
        res = gpt.get_summary(data)
        print(res)
    else:
        print("요리 스크립트가 아닙니다.")


if __name__ == "__main__":
    main()