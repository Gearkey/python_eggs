import re

def main():
    input = open("./_note/input.md", mode="r", encoding="utf-8")
    output = open("./_note/output.md", mode="w", encoding="utf-8")

    text = input.read()
    text = re.sub(r"\[(.*?)\]\((.*?)\) ?", r"\1（\2）", text)
    text = re.sub(r"## (.*)", r"【\1】", text)

    text = text.replace("\n", "\r\n")
    text = text.replace("\r\n\r\n", "\r\n---\r\n")
    text = text.replace("\\", "")

    output.write(text)
    print(text)

if __name__ == "__main__":
    main()