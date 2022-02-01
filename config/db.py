from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root@127.0.0.1:3307/test')
meta = MetaData()
conn = engine.connect()
