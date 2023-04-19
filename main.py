from pydantic import BaseModel

from lib import expose, run_server


class GetUserReq(BaseModel):
    count: int


@expose
def get_user(
        ctx: GetUserReq
) -> GetUserReq:
    # auth?
    return ctx


if __name__ == '__main__':
    run_server()
