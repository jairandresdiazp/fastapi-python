from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, Any, List
T = TypeVar('T')

class Response(BaseModel, Generic[T]):
  data: Optional[T] = None
  success: bool
  error: Optional[List[str]] = None

  def __init__(self,success: bool, data: Optional[T] = None, error: Optional[List[str]] = None):
    super().__init__(success=success, data=data, error=error)
    self.success = success
    self.data = data
    self.error = error