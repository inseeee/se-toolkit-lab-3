"""Router for learner endpoints."""

from fastapi import APIRouter
from datetime import datetime
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    learners = await read_learners(session, enrolled_after)
    return learners
# ===

# UNCOMMENT AND FILL IN
#
# @router.<method>("/<resource_name>", response_model=list[<resource_schema>])
# async def <function_name>(
#     <query_param>: <type> = None,
#     session: AsyncSession = Depends(get_session),
# ):
#     """<docstring>"""
#     return await <db_read_function>(session, <query_param>)
#
# Reference:
# items GET -> reads from items table, returns list[Item]
# learners GET -> reads from learners table, returns list[Learner]
# Query parameter: ?enrolled_after= filters learners by enrolled_at date

# ===
# PART B: POST endpoint
@router.post("/", response_model=Learner, status_code=201)
async def create_learner_endpoint(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    return await create_learner(session, learner)
# ===

# UNCOMMENT AND FILL IN
#
# @router.<method>("/<resource_name>", response_model=<resource_schema>, status_code=<status_code>)
# async def <function_name>(
#     <param_name>: <request_schema>,
#     session: AsyncSession = Depends(get_session),
# ):
#     """<docstring>"""
#     return await <db_create_function>(session, name=<param_name>.name, email=<param_name>.email)
#
# Reference:
# items POST -> creates a row in items table, accepts ItemCreate, returns Item with status 201
# learners POST -> creates a row in learners table, accepts LearnerCreate, returns Learner with status 201
