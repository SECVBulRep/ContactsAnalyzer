from fastapi import APIRouter, Depends

from web_api.dto.process_request import ProcessRequest
from web_api.dto.process_response import ProcessResponse
from web_api.services.llm_service import LLMService

router = APIRouter()

@router.post("/process", response_model=ProcessResponse)
async def process_llm(request: ProcessRequest, service: LLMService = Depends()):
    result = await service.processAsync(request)
    return ProcessResponse(output=result)

@router.post("/llm-list")
def process_llm():
    return "ok"
