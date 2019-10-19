class Shop:
    def __init__(self,address,open_at,close_at,min_price_euro,max_price_euro,walk_in_start_time,walk_in_length_time):
        self.address = address
        self.open_hour = open_at
        self.close_hour = close_at
        self.min_price = min_price_euro
        self.max_price = max_price_euro
        self.avg_price = (min_price_euro + max_price_euro) / 2
        self.walk_in_start_time = walk_in_start_time
        
     
