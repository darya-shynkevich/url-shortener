from fastapi import HTTPException, APIRouter
from starlette.responses import RedirectResponse

from config import config
from web.serializers import URLShortenRequest, URLShortenResponse

from fastapi import FastAPI

from web.redis_client import RedisClient
from web.services import ShortenerService

app = FastAPI()

redis_client = RedisClient()

shortener_service = ShortenerService()

router = APIRouter()


@router.post("/shorten")
async def shorten_url(request: URLShortenRequest) -> URLShortenResponse:
    short_key = shortener_service.shorten_random()
    await redis_client.set(short_key, request.url)
    return URLShortenResponse(short_url=shortener_service.get_short_url(short_key))


@router.get("/{short_key}")
async def redirect_to_url(short_key: str):
    original_url = await redis_client.get(short_key)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)


app.include_router(router, prefix=config.prefix)
