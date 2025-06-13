from fastapi import APIRouter

router = APIRouter()

# Import and include individual route modules
# (Create these files in the future as your app grows)
# Example: from . import users, games, payments, admin

# router.include_router(users.router, prefix="/users", tags=["users"])
# router.include_router(games.router, prefix="/games", tags=["games"])
# router.include_router(payments.router, prefix="/payments", tags=["payments"])
# router.include_router(admin.router, prefix="/admin", tags=["admin"])

@router.get("/")
async def root():
    return {"message": "Vino Bingo Backend is running!"}
