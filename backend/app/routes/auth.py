# apps/backend/src/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..services.auth import (
    authenticate_user,
    create_user,
    create_access_token
)
from ..schemas.user import (
    UserCreate,
    UserResponse,
    TokenResponse,
    AccessCodeVerification
)
from ..models.user import User

router = APIRouter()

# Valid access codes (replace with database or more secure method in production)
VALID_ACCESS_CODES = ["VENTRY2024", "EXCLUSIVE"]

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    """
    User signup endpoint
    """
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    return create_user(db, user)

@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    User login endpoint
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Create access token
    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/verify-access-code")
def verify_access_code(
    access_code: AccessCodeVerification,
    db: Session = Depends(get_db)
):
    """
    Verify access code for invite-only signup
    """
    if access_code.access_code in VALID_ACCESS_CODES:
        return {"status": "approved"}

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid access code"
    )
