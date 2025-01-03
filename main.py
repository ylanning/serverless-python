from fastapi import FastAPIfrom sqlmodel import Field, Session, SQLModel, create_engine, selectfrom config import settingsfrom src.env import configimport osMODE = config("MODE", cast=str, default="Testing")class Hero(SQLModel, table=True):    id: int | None = Field(default=None, primary_key=True)    name: str = Field(index=True)    secret_name: str    age: int | None = Field(default=None, index=True)engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))def create_db_and_tables():    SQLModel.metadata.create_all(engine)app = FastAPI()port = int(os.environ.get("PORT", 8080))app.add_event_handler("startup", create_db_and_tables)@app.get("/")def hello():    return {"Hello": "World", "mode": MODE}@app.post("/heroes/")def create_hero(hero: Hero):    with Session(engine) as session:        session.add(hero)        session.commit()        session.refresh(hero)        return hero@app.get("/heroes/")def read_heroes():    with Session(engine) as session:        heroes = session.exec(select(Hero)).all()        return heroesif __name__ == "__main__":    app.run(host='0.0.0.0', port=port)