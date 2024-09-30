from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.file_manager import FileManager

router = APIRouter()


@router.get("/static/{file_name}")
async def get_static_file(file_name: str):
    file_manager = FileManager()  # Obtenir l'instance unique de FileManager
    file_path = file_manager.get_file_path(file_name)

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(file_path.open("rb"), media_type="image/png")
