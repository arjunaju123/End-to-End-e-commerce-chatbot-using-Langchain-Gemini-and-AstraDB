from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

print(GOOGLE_API_KEY)
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",transport='rest')
print("embeddings is",embeddings)
vector = embeddings.embed_query("hello, world!")
print(vector[:5])