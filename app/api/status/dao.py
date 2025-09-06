from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import text


async def check_availability(session: AsyncSession) -> bool:
    try:
        result = await session.execute(text("SELECT 1"))
        return result.scalar_one() == 1
    except Exception as e:
        print(f"Database connection error: {e}")
        return False
