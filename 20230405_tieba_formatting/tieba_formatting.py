import re

def main():
    input = open("./_note/input.md", mode="r", encoding='utf8')
    output = open("./_note/output.md", mode="w", encoding='utf8')

    text = input.read()
    text = text.replace("\n", "\n\r")
    text = text.replace("\n\r\n\r", "\n\r---\n\r")
    
    text = re.sub(r"\[(.*)\]\((.*)\)", r"\1（\2）", text)
    text = re.sub(r"## (.*)", r"【\1】", text)

    output.write(text)
    print(text)

if __name__ == "__main__":
    main()