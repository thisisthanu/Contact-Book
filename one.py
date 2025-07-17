import mysql.connector

class AddressBook:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2255",
            database="minichallenge"
        )
        self.cursor = self.conn.cursor()

    def add_contact(self, c_name, phone, email, address):
        try:
            query = """
                INSERT INTO my_contacts (C_Name, Phone, Email, Address)
                VALUES (%s, %s, %s, %s)
            """
            values = (c_name, phone, email, address)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("✅ Contact added successfully!")
        except mysql.connector.Error as err:
            print("❌ Error in adding the contact:", err)

    def remove_contact(self, contact_id):
        try:
            self.cursor.execute("SELECT * FROM my_contacts WHERE id=%s", (contact_id,))
            result = self.cursor.fetchone()

            if result is None:
                print(f"⚠️ Contact with ID {contact_id} not found.")
                return

            self.cursor.execute("DELETE FROM my_contacts WHERE id=%s", (contact_id,))
            self.conn.commit()
            print(f"🗑️ Contact with ID {contact_id} deleted successfully!")
        except mysql.connector.Error as err:
            print("❌ Error deleting contact:", err)

    def update_contact(self, contact_id, new_values):
        try:
            self.cursor.execute("SELECT * FROM my_contacts WHERE id=%s", (contact_id,))
            result = self.cursor.fetchone()

            if result is None:
                print(f"⚠️ Contact with ID {contact_id} does not exist.")
                return

            query = """
                UPDATE my_contacts
                SET C_Name=%s, Phone=%s, Email=%s, Address=%s
                WHERE id=%s
            """
            values = (
                new_values.get('C_Name'),
                new_values.get('Phone'),
                new_values.get('Email'),
                new_values.get('Address'),
                contact_id
            )

            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"✅ Contact with ID {contact_id} updated successfully!")
        except mysql.connector.Error as err:
            print("❌ Error updating the contact:", err)

    def view_contacts(self):
        try:
            self.cursor.execute("SELECT * FROM my_contacts")
            rows = self.cursor.fetchall()

            if not rows:
                print("📭 No Contacts Found.")
                return

            print("\n📒 All Contacts:")
            print("-" * 90)
            print(f"{'ID':<5}{'Name':<20}{'Phone':<20}{'Email':<20}{'Address':<20}")
            print("-" * 90)

            for row in rows:
                contact_id, name, phone, email, address = row
                print(f"{contact_id:<5}{name:<20}{phone:<20}{email:<20}{address:<20}")

            print("-" * 90)
        except mysql.connector.Error as err:
            print("❌ Error retrieving contacts:", err)

    def search_contact(self, search_term):
        try:
            query = """
                SELECT * FROM my_contacts
                WHERE C_Name LIKE %s
                OR Phone LIKE %s
                OR Email LIKE %s
                OR Address LIKE %s
            """
            wildcard_term = f"%{search_term}%"
            values = (wildcard_term, wildcard_term, wildcard_term, wildcard_term)

            self.cursor.execute(query, values)
            results = self.cursor.fetchall()

            if not results:
                print(f"\n🔍 No contacts found matching '{search_term}'")
                return

            print(f"\n🔍 Search Results for '{search_term}':")
            print("-" * 90)
            print(f"{'ID':<5}{'Name':<20}{'Phone':<20}{'Email':<20}{'Address':<20}")
            print("-" * 90)

            for row in results:
                contact_id, name, phone, email, address = row
                print(f"{contact_id:<5}{name:<20}{phone:<20}{email:<20}{address:<20}")

            print("-" * 90)

        except mysql.connector.Error as err:
            print("❌ Error searching contacts:", err)

    def close(self):
        self.cursor.close()
        self.conn.close()

book = AddressBook()

# TC‑1
book.remove_contact(2)
# TC‑5
book.view_contacts()

# …continue through the list…

book.close()
