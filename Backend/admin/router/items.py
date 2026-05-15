from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File,Form
from admin.services.manager_items import ManagerItems

from shared.dependcices.dependcices import conn_dep, redis_dep, lang_dep
from shared.dependcices.securite_decode_token import decode_token
from shared.errors.admin_errors import AdminError
from shared.errors.db_errors import DbError
from shared.errors.items_errors import ItemsError
from shared.errors.uploads_errors import UploadsError

router = APIRouter(prefix="/api/v1/admin/items", tags=["Admin-items"])

@router.post("/",status_code=status.HTTP_201_CREATED)
async def add_items(connection : conn_dep,redis:redis_dep,lang:lang_dep,payload = Depends(decode_token),title: str = Form(...),
    author: str = Form(...),
    synopsis: str = Form(...),
    category_id: int = Form(...),
    language: str = Form(...),
    year: int = Form(...),
    pages: int = Form(...),
    genres: str = Form(...,description="action, drama, fantasy"),
    image_url: UploadFile = File(...),
    file_url: UploadFile = File(...), ):
    try :
        services = ManagerItems(connection=connection, redis=redis, lang=lang)
        result = await services.add_items(
            title=title,
            author=author,
            synopsis=synopsis,
            category_id=category_id,
            language=language,
            year=year,
            pages=pages,
            genres=genres,
            image=image_url,
            file_url=file_url,
            payload=payload)
        return result
    except AdminError as e :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))
    except UploadsError as e :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    except ItemsError as e :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in server")

