from slugify import slugify

from app.db.errors import EntityDoesNotExist
from app.db.repositories.items import ItemsRepository
from app.models.domain.items import Item
from app.models.domain.users import User
import requests
import os

async def check_item_exists(items_repo: ItemsRepository, slug: str) -> bool:
    try:
        await items_repo.get_item_by_slug(slug=slug)
    except EntityDoesNotExist:
        return False

    return True


def get_slug_for_item(title: str) -> str:
    return slugify(title)


def check_user_can_modify_item(item: Item, user: User) -> bool:
    return item.seller.username == user.username

async def get_image_for_item(title: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model":"dall-e-2",
        "prompt": title,
        "n": 1,
        "quality":"standard",
        "size": "256x256"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.data