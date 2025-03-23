from openai import OpenAI

from dto.process_request import ProcessRequest

client = OpenAI(
    api_key=""  # вынеси в .env
)


def call_chatgpt(request: ProcessRequest) -> str:

    names_text: str = " | ".join(request.display_names)

    text = ("Телефонный номер в справочниках записан как: " + names_text +
            ". Помоги придумать как мне его записать у себя списках контактов."+
            "Ответ не должен содержать рассуждения. Мне нужно просто название и все.");
    print(text)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты анализатор текста."},
            {"role": "user", "content": text},
        ],
        max_tokens=100,
        temperature=0.1,
        stream=False
    )
    return response.choices[0].message.content