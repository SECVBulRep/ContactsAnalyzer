from web_api.dto.process_request import ProcessRequest

class LLMService:
    def process(self, request: ProcessRequest) -> str:

        return f"Processed with {request.model}: {request.prompt}"
