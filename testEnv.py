from csvEditor import addToCSV, createCSV

createCSV()
print("CSV file created successfully.")
addToCSV(agentID=1, role="Test Role1", message="This is a test message.", similarity=0.95)
addToCSV(agentID=2, role="Test Role2", message="This is a test message.", similarity=0.95)
addToCSV(agentID=3, role="Test Role3", message="This is a test message.", similarity=0.95)
addToCSV(agentID=4, role="Test Role4", message="This is a test message.", similarity=0.95)
addToCSV(agentID=5, role="Test Role5", message="This is a test message.", similarity=0.95)