from project import mysql


def connect_cursor_db():
    return mysql.connection.cursor()
def connect_commit_db():
    return mysql.connection.commit() 


def getuser(username):
      try:
        cur = connect_cursor_db()
        cur.execute('SELECT UserId, Username,Password FROM Access WHERE Username = %s',(username,))
        account = cur.fetchone()
        return account
      except Exception as e:
            print("something went wrong", e)


def findcoupon(couponcode):
      try:
        cur = connect_cursor_db()
        query='SELECT CoupId,Creation_date,Expiration_date,Value,Redemed FROM Coupon WHERE Coupon.CoupId LIKE %s LIMIT 15'
        cur.execute(query,("%{}%".format(couponcode),))
        coupons = cur.fetchall()
        return coupons
      except Exception as e:
            print("something went wrong", e)

def redeemcoupon(Userid,couponId):
      print(Userid,couponId)
      cur = connect_cursor_db()
      cur.callproc( "Redeem",(couponId,Userid))
      results =cur.fetchone()
      return results

    