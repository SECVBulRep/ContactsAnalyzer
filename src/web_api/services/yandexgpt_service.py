
from dto.process_request import ProcessRequest

from yandex_cloud_ml_sdk import YCloudML

sdk = YCloudML(
    folder_id="", auth=""
)


def call_yandexgpt(request: ProcessRequest) -> str:

    names_text: str = " | ".join(request.display_names)

    text = ("Телефонный номер в справочниках записан как: " + names_text +
            ".Помоги придумать как мне его записать у себя списках контактов."+
            "Ответ не должен содержать рассуждения. Мне нужно просто название и все.");
    print(text)


    model = sdk.models.completions("yandexgpt", model_version="rc")
    model = model.configure(temperature=0.3)
    result = model.run(
        [
            {"role": "system", "text": "Ты анализатор текста."},
            {
                "role": "user",
                "text": text,
            },
        ]
    )

    return result.text

