from dataclasses import dataclass 
from datetime import datetime


@dataclass
class Expense:
    title: str
    amount: float
    category: str
    date: str = None