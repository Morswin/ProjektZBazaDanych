from sqlmodel import SQLModel, create_engine
# from models import *
import populate


if __name__ == "__main__":
    # The 2 lines below may need to be rewritten later to use python's os path join, but I am not sure how to combine it with SQLModel's local path thing for now.
    sqlite_file = "db.sqlite" 
    sqlite_url = f"sqlite:///db/{sqlite_file}"
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
    populate.populate(engine)

