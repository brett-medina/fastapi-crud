from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime

DB_FILE = 'db.sqlite3' #just a file
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)

class TrackModel(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	title: str
	artist: str
	duration: float
	last_play: datetime

def create_tables():
	SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
	# creates the table if this file is run independently, as a script
	create_tables()