
from fastapi import APIRouter,Depends,HTTPException,status

from shared.dependcices.dependcices import conn_dep,redis_dep,lang_dep
from shared.dependcices.securite_decode_token import decode_token
from shared.errors.db_errors import DbError
from shared.errors.users_errors import UsersError
from users.services.profile.profile import ProfileService

router = APIRouter(prefix="/api/v1",tags=["users"])

@router.get("/me")
async def get_user_profile(connection: conn_dep,redis:redis_dep,lang:lang_dep,payload = Depends(decode_token)):
    try :
        services = ProfileService(connection=connection, redis=redis, lang=lang)
        email = payload.get("sub")
        result = await  services.get_user_profile(email=email)
        return result
    except UsersError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    except DbError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))