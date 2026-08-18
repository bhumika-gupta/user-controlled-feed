try:
    from fastapi import FastAPI  # type: ignore
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
def get_health():
    return {"status": "healthy"}