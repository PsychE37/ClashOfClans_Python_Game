class Entity:
    def __init__(self,pos_x,pos_y,height,width,damage,health):
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.height = height
        self.width = width
        self.damage = damage
        self.max_health = health
        self.cur_health = health
        self.destroyed = False
        self.flying = False
        
    def make(self):
        pass
    
    def set_on_canvas(self):
        pass