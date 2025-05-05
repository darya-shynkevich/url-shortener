from fastapi import HTTPException
from starlette.responses import RedirectResponse

from app import app, shortener_service, redis_client
from web.serializers import URLShortenRequest, URLShortenResponse


@app.post("/shorten")
async def shorten_url(request: URLShortenRequest) -> URLShortenResponse:
    short_key = shortener_service.shorten_random()
    await redis_client.set(short_key, request.url)
    return URLShortenResponse(short_url=shortener_service.get_short_url(short_key))


@app.get("/{short_key}")
async def redirect_to_url(short_key: str):
    original_url = await redis_client.get(short_key)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)
