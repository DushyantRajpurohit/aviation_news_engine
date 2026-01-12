import sqlite3

# Connect to the database
conn = sqlite3.connect('demo_data.db')
c = conn.cursor()

# Get the last 5 entries
c.execute("SELECT id, heading, image_path FROM articles ORDER BY id DESC LIMIT 5")
rows = c.fetchall()

print("\n--- LATEST DATABASE ENTRIES ---")
print(f"{'ID':<5} | {'Image Saved?':<15} | {'Heading'}")
print("-" * 60)

for row in rows:
    img_status = "✅ Yes" if "demo_images" in row[2] else "❌ No"
    print(f"{row[0]:<5} | {img_status:<15} | {row[1]}")

conn.close()