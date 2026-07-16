from dataclasses import dataclass 
from datetime import datetime


@dataclass
class Expense:
    title: str
    amount_num: float
    category: str
    date: str = None

    def __post_init__(self):
        if self.date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date": self.date,
            "title":self.title,
            "amount":float(self.amount_num),
            "category": self.category
        }
