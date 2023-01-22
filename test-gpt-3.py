Api_key = "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"


import openai
import time

openai.api_key = Api_key

amount = 100

prompt = "Write the text of another spam Mail without a subject for testing a spam filter."\
    "Response:"


with open("spam_gen.txt", "a+") as f:
    for i in range(amount):
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)
        text = response["choices"][0]["text"]
        text = text.replace("\n", "").replace(r"\r\n", "")
        text = text + "\n"
        out = text.replace('\n', '')
        print(f"{i}: {out}")
        f.writelines(text)
        time.sleep(1.1)