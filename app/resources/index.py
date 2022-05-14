from fastapi import APIRouter

def init(app):
    router = APIRouter(
        tags=["Index"]
    )

    @router.get("/", response_model=dict)
    def index():
        return {"Message", "Hello EuReciclo"}
    
    app.include_router(router)

    return app