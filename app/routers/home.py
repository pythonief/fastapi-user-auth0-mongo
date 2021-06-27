from fastapi import APIRouter

router = APIRouter(
    tags=['Home']
)


@router.get('/')
def home():
    return {
        'message': 'Hello World'
    }
