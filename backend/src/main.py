from fastapi import FastAPI
import uvicorn
from user.router import router as users_router
from auth.router import router as auth_router

app = FastAPI(
    title="NEXT_social_net_api"
)

app.include_router(users_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run('main:app',port=5555, reload=True)
    
    
    
