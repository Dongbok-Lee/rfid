import read

data = read.read_token()
data2 = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqaW5naTY0NjJAZ21haWwuY29tIiwicm9sZSI6IlJPTEVfVVNFUiIsImlkIjoyNywiaXNzIjoiU1NtYXJ0T2ZmaWNlIiwiaWF0IjoxNzMxOTU2NTM3LCJleHAiOjE3MzMyNTI1Mzd9.j1ZmkUMG6dwM4IJzbu41qIPIlOFldTniraU5_E0BITY"

print(data == data2)

print(len(data.strip()))
print(len(data2))

