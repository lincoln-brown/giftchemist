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
            print("Error, Unable to Find user at this time.", e)


def findcoupon(couponcode):
      try:
        cur = connect_cursor_db()
        query='SELECT CoupId,Creation_date,Expiration_date,Value,Redemed FROM Coupon WHERE Coupon.CoupId LIKE %s LIMIT 30'
        cur.execute(query,("%{}%".format(couponcode),))
        coupons = cur.fetchall()
        return coupons
      except Exception as e:
            print("Error,Unable to Fetch Coupons at this time.", e)

def redeemcoupon(Userid,couponId):
      try:
        print(Userid,couponId)
        cur = connect_cursor_db()
        cur.callproc( "Redeem",(couponId,Userid))
        results =cur.fetchone()
        return results
      except Exception as e:
        print("Error, Unable to Redeem Coupon at this time.", e)

def LastCouponcode():
    try:
        cur = connect_cursor_db()
        query='select count(CoupId) from Coupon'
        cur.execute(query)
        CoupId = cur.fetchone()
       ## print(int(CoupId['count(CoupId)']))
        return int(CoupId['count(CoupId)'])
    except Exception as e:
        print("Error Unable to fetch last Coupon ID.", e)
def NextUserid():
    try:
        cur = connect_cursor_db()
        query='select count(UserId) from Users'
        cur.execute(query)
        UserId = cur.fetchone()
       ## print(int(CoupId['count(CoupId)']))
        return "UID"+ str(int(UserId['count(UserId)'])+1)
    except Exception as e:
        print("Error Unable to fetch next User ID.", e)


def addcoupon(coupon):
    try:    
        cur = connect_cursor_db()
        cur.execute('insert into Coupon values (%s, %s,%s,%s,%s)',
        (coupon["Code"], coupon["Creation_date"],coupon["Expiration_date"],coupon["Value"],"false"))
        connect_commit_db()
        return "True"
    except cur.IntegrityError as e:
        print("something went wrong",e)
        return "Duplicate_entry"
    except Exception as e :
         print("something went wrong",e)
         return False


def addnewuser(User):
      try:
        cur = connect_cursor_db()
        cur.callproc( "Adduser",(User["First_Name"],User["Last_Name"],User["UserId"],User["Username"],User["Password"]))
        results =cur.fetchone()
        return results
      except Exception as e:
        print("Error, Unable to Add New user at this time.", e)
    





      
    