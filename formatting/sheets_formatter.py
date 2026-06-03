from enum import Enum
from datetime import datetime

class TransactionPlatform(Enum):
    Cash = 1
    Venmo = 2
    Squarespace = 3
    Square = 4
    Check = 5
    NotApplicable = 6

    def toString(self):
        if self == TransactionPlatform.Cash:
            return "Cash"
        elif self == TransactionPlatform.Venmo:
            return "Venmo"
        elif self == TransactionPlatform.Squarespace:
            return "Squarespace (Website)"
        elif self == TransactionPlatform.Square:
            return "Square (Card)"
        elif self == TransactionPlatform.Check:
            return "Check"
        elif self == TransactionPlatform.NotApplicable:
            return "N/A"
        else:
            return "Unknown"
        
class ItemType(Enum):
    RideWithMeTee = 1
    RingerTee = 2
    StrawberriesTee = 3
    Sticker = 4
    Unknown = 5

    def toString(self):
        if self == ItemType.RideWithMeTee:
            return "Ride With Me"
        elif self == ItemType.RingerTee:
            return "Ringer Tee"
        elif self == ItemType.StrawberriesTee:
            return "Musical Strawberries"
        elif self == ItemType.Sticker:
            return "Sticker"
        else:
            return "Unknown"    
        
    def fromSquare(squareStr):
        if squareStr == "RIDE WITH ME TEE":
            return ItemType.RideWithMeTee
        elif squareStr == "RINGER TEE":
            return ItemType.RingerTee
        elif squareStr == "THE MUSIC BAND TEE":
            return ItemType.StrawberriesTee
        elif squareStr == "STICKER":
            return ItemType.Sticker
        else:
            return ItemType.Unknown

    def fromSquarespace(squarespaceStr):
        # TODO - implement
        if squarespaceStr == "JAMN RIde With Me Graphic Tee":
            return ItemType.RideWithMeTee
        elif squarespaceStr == "JAMN Strawberry Ringer Tee":
            return ItemType.RingerTee
        elif squarespaceStr == "JAMN Like Damn The Music Band Graphic Tee":
            return ItemType.StrawberriesTee
        elif squarespaceStr == "JAMN Sticker Pack":
            return ItemType.Sticker
        else:
            return ItemType.Unknown
        
class Size(Enum):
    ExtraSmall = 1
    Small = 2
    Medium = 3
    Large = 4
    ExtraLarge = 5
    ExtraExtraLarge = 6
    Unknown = 7

    def toString(self):
        if self == Size.ExtraSmall:
            return "Extra Small (XS)"
        elif self == Size.Small:
            return "Small (S)"
        elif self == Size.Medium:
            return "Medium (M)"
        elif self == Size.Large:
            return "Large (L)"
        elif self == Size.ExtraLarge:
            return "Extra Large (XL)"
        elif self == Size.ExtraExtraLarge:
            return "2x Extra Large (XXL)"
        else:
            return "Unknown"
        
    def fromSquare(squareStr):
        if squareStr == "Extra Small (XS)":
            return Size.ExtraSmall
        elif squareStr == "Small (S)":
            return Size.Small
        elif squareStr == "Medium (M)":
            return Size.Medium
        elif squareStr == "Large (L)":
            return Size.Large
        elif squareStr == "Extra Large (XL)":
            return Size.ExtraLarge
        elif squareStr == "2x Extra Large (XXL)":
            return Size.ExtraExtraLarge
        else:
            return Size.Unknown
    
    def fromSquarespace(squarespaceStr):
        if squarespaceStr == "XS":
            return Size.ExtraSmall
        elif squarespaceStr == "S":
            return Size.Small
        elif squarespaceStr == "M":
            return Size.Medium
        elif squarespaceStr == "L":
            return Size.Large
        elif squarespaceStr == "XL":
            return Size.ExtraLarge
        elif squarespaceStr == "XXL":
            return Size.ExtraExtraLarge
        else:
            return Size.Unknown



def formatDate(dateStr, transactionPlatform):
    if transactionPlatform == TransactionPlatform.Squarespace:
        dt = datetime.strptime(dateStr[:10], "%Y-%m-%d")
        return f"{dt.day}{dt.strftime('%b%Y')}"
    elif transactionPlatform == TransactionPlatform.Square:
        dt = datetime.strptime(dateStr[:10], "%Y-%m-%d")
        return f"{dt.day}{dt.strftime('%b%Y')}"
    else:
        return dateStr
    
def getEarnings(retailPrice, transactionPlatform):
    if transactionPlatform == TransactionPlatform.Squarespace:
        transactionFee = (retailPrice * .029) + 0.30
        return max(retailPrice - transactionFee, 0.00)
    elif transactionPlatform == TransactionPlatform.Square:
        transactionFee = (retailPrice * .026) + 0.15
        return max(retailPrice - transactionFee, 0.00)
    else:
        return retailPrice

def generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments = ""):
    # format is as follows:
    # Transaction Date, Transation Platform, T-Shirt Type, Size, Retail Price, Earnings, Comments
    # 15Jan2026, Square (Card), Ringer Tee, Small (S), 25.00, 24.43, Generated from Square API and jamn_sales_tracker
    return [date, transaction_platform.toString(), t_shirt_type.toString(), size.toString(), retail_price, earnings, comments]
