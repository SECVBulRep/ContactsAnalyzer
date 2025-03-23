import asyncio

from services.chatgpt_service import call_chatgpt
from services.yandexgpt_service import call_yandexgpt
from web_api.dto.process_request import ProcessRequest
from web_api.services.deepseek_service import call_deepseek


class LLMService:
    async def processAsync(self, request: ProcessRequest) -> str:

        if request.llm_type == "deepseek":
            return await asyncio.to_thread(call_deepseek,request)

        if request.llm_type == "chatgpt":
            return await asyncio.to_thread(call_chatgpt, request)

        if request.llm_type == "yandexgpt":
            return await asyncio.to_thread(call_yandexgpt, request)



        count = len(request.display_names)
        return f"LLM: {request.llm_type} — {count} display names processed"
