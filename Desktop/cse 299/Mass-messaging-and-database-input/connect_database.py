import sqlite3
import cv2
import pytesseract
import pandas as pd


# Connect to the database
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Create the table
c.execute("CREATE TABLE new(articles TEXT)")

# Get the image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert the image to text
text = pytesseract.image_to_string(img)
articles = [text]
print(articles)

# Convert the list to a CSV file
df = pd.DataFrame(articles)
df.to_csv('file.csv', index=False)

no_of_lines = len(articles)

# Inserting the articles into the database
c.execute("INSERT INTO news VALUES(?)", (articles))
conn.commit()

# Close the connection
conn.close()
c.close()

# Close the windows of CV2
cv2.waitKey(0)
cv2.destroyAllWindows()
