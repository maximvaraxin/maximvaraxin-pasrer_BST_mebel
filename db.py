import sqlite3

class Furniture_db():

   def __init__(self, db_file):
      self.conn = sqlite3.connect(db_file)
      self.cursor = self.conn.cursor()

   def getProductName(self):
      result = self.cursor.execute("SELECT `name` FROM `product_details`")
      return result.fetchall()

   def getLink(self):
      result = self.cursor.execute("SELECT `web_id`, `web_link` FROM `catalog_web`")
      return result.fetchall()

   def getWebID(self, position):
      result = self.cursor.execute(f"SELECT `id` FROM `product_details` WHERE product_details.name = ?", position)
      return result.fetchone()

   def insertProductName(self, name):
      self.cursor.execute("INSERT INTO `product_details` (`name`) VALUES (?)", (name,))
      return self.conn.commit()

   def insertProductLinksDataBase(self, web_id, web_link ):
      self.cursor.execute("INSERT INTO `catalog_web` (`web_id`, `web_link`) VALUES (?,?)", (web_id, web_link,))
      return self.conn.commit()

   def upadteProductParamsDataBase(self, widht, heihgt, depth, matherial, status, id):
      self.cursor.execute("UPDATE `product_details` SET (`widht`, `heihgt`, `depth`,`matherial`,`status`) = (?, ?, ?, ?, ?) WHERE product_details.id = ?", (widht, heihgt, depth, matherial, status, id,))
      return self.conn.commit()

   def close(self):
      self.connection.close()