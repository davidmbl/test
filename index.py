from pathlib import Path

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

schema = Path('test.sql').read_text()
llm = OpenAI(temperature=0.9,openai_api_key="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")
print(schema)
db = SQLDatabase.from_uri("mysql+pymysql://sail:password@localhost:3306/forum")

db_chain = SQLDatabaseChain(return_direct=True,llm=llm,database=db, verbose=True)
db_chain.run("how can i increase profit?")
