from slugify import slugify

from app.db.errors import EntityDoesNotExist
from app.db.repositories.items import ItemsRepository
from app.models.domain.items import Item
from app.models.domain.users import User
from openai import OpenAI, OpenAIError

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

    client = OpenAI()
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=title,
            size="256x256",
            quality="standard",
            n=1,
        )
    except OpenAIError as e:
        print(e.http_status)
        print(e.error)
    print(response.data[0].url)
    return response.data[0].url
