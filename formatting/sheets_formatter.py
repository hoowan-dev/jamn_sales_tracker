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
        if squarespaceStr == "Ride With Me":
            return ItemType.RideWithMeTee
        elif squarespaceStr == "Ringer Tee":
            return ItemType.RingerTee
        elif squarespaceStr == "Musical Strawberries":
            return ItemType.StrawberriesTee
        elif squarespaceStr == "Sticker":
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
        # TODO - implement
        return squarespaceStr

def formatDate(dateStr, transactionPlatform):
    if transactionPlatform == TransactionPlatform.Squarespace:
        # TODO - implement
        return dateStr
    elif transactionPlatform == TransactionPlatform.Square:
        dt = datetime.strptime(dateStr[:10], "%Y-%m-%d")
        return f"{dt.day}{dt.strftime('%b%Y')}"
    else:
        return dateStr

def generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments = ""):
    # format is as follows:
    # Transaction Date, Transation Platform, T-Shirt Type, Size, Retail Price, Earnings, Comments
    # 15Jan2026, Square (Card), Ringer Tee, Small (S), Retail Price, Earnings, Comments
    return [date, transaction_platform.toString(), t_shirt_type.toString(), size.toString(), retail_price, earnings, comments]
