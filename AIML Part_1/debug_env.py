import os
import dotenv

print("cwd:", os.getcwd())
print("files:", sorted(os.listdir()))
print(".env path found by dotenv:", dotenv.find_dotenv())
print("GOOGLE_API_KEY from os.getenv():", os.getenv("GOOGLE_API_KEY"))
