from fastapi import APIRouter, HTTPException, status, Response, Query,BackgroundTasks
from fastapi.templating import Jinja2Templates

from shared.dependcices.dependcices import conn_dep,redis_dep,lang_dep
from shared.errors.auth_errors import UserNameError, EmailError, PasswordError, TokenError
from shared.errors.users_errors import UsersError
from shared.errors.db_errors import DbError
from users.services.Auth.login_servives import LoginServices
from users.services.Auth.register_services import RegisterServices
from users.shemas.auth_schemas import RegisterSchema, LoginSchema, LoginGoogle

router = APIRouter(prefix="/api/v1", tags=["User_Auth"])
templates = Jinja2Templates(directory="templates")

# register
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(register_schemas : RegisterSchema,redis:redis_dep,connection:conn_dep,lang:lang_dep,background_task:BackgroundTasks):
    try :
        services = RegisterServices(connection=connection,redis=redis,language=lang)
        result =await services.register(user_name=register_schemas.user_name,email=register_schemas.email,password=register_schemas.password,template=templates,background_task=background_task)
        return result
    except UserNameError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except EmailError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except UsersError as error:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=str(error))
    except DbError as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="error in servers")

# login

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(login_schemas : LoginSchema,response:Response,redis:redis_dep,connection:conn_dep,lang:lang_dep):
    try :
        services = LoginServices(connection=connection,redis=redis,language=lang,response=response)
        result = await services.login(email=login_schemas.email,password=login_schemas.password)
        return result
    except EmailError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except PasswordError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except UsersError as error:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=str(error))
    except DbError as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    # except Exception as error:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))

@router.post("/google-login", status_code=status.HTTP_200_OK)
async def google_login(response:Response,login_google : LoginGoogle ,redis:redis_dep,connection:conn_dep,lang:lang_dep):
    try :
        services =LoginServices(connection=connection,redis=redis,language=lang,response=response)
        result = await  services.login_with_google(token=login_google.token)
        return result
    except EmailError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except TokenError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(error))
    except UsersError as error:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=str(error))
    except DbError as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    # except Exception as error:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    
@router.get("/verify_account")
async def verify_link(redis:redis_dep,connection:conn_dep,lang:lang_dep,token=Query(...)):
    try :
        services = RegisterServices(connection=connection, redis=redis, language=lang)
        result =  await services.verify_account(token=token)
        return result
    except EmailError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(error))
    except UsersError as error:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,detail=str(error))
    except DbError as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(error))




    

