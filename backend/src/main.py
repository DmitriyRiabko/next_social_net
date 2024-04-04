from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="NEXT_social_net_api"
)



if __name__ == "__main__":
    uvicorn.run('main:app',port=5555, reload=True)