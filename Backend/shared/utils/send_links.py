import os
import secrets
import resend
from dotenv import load_dotenv

load_dotenv(override=True)

async def send_link(email,title,redis,jinja2):
    resend.api_key = os.environ["RESEND_API_KEY"]
    token = secrets.token_urlsafe(64)
    await redis.set(f"auth:{title}:{token}",email,ex=600)
    # init resend
    tempalate = jinja2.get_template("send_link_template.html").render({
        "email": email,
        "verify_link":f"{os.getenv("SUBDOMAIN")}/api/v1/{title}?token={token}",
    })
    params: resend.Emails.SendParams = {
        "from": "noreply@rawyverse.xyz",
        "to": email,
        "subject": "Rawyverse",
        "html": tempalate,
    }
    resend.Emails.SendResponse = resend.Emails.send(params)