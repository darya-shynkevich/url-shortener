from pydantic import BaseModel, HttpUrl


class URLShortenRequest(BaseModel):
    url: str


class URLShortenResponse(BaseModel):
    short_url: HttpUrl
