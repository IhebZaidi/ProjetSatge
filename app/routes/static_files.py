from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pathlib import Path

router = APIRouter()

plot_dir = Path("plots")

@router.get("/static/{file_name}")
async def get_static_file(file_name: str):
    file_path = plot_dir / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return StreamingResponse(file_path.open("rb"), media_type="image/png")
