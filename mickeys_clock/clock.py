def render(self, surface):
        surface.blit(self.bg, (0, 0))
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        now = datetime.datetime.now()
        
        seconds = now.second
        minutes = now.minute
        hours = now.hour % 12  

        sec_angle = - (seconds * 6) 
        min_angle = - (minutes * 6 + seconds * 0.1) 
        hour_angle = - (hours * 30 + minutes * 0.5) 

        min_pivot = (self.min_hand_orig.get_width() // 2, self.min_hand_orig.get_height() - 20)
        sec_pivot = (self.sec_hand_orig.get_width() // 2, self.sec_hand_orig.get_height() - 20)

        self.blit_rotate_pivot(surface, self.sec_hand_orig, self.center, sec_pivot, hour_angle)
        
        self.blit_rotate_pivot(surface, self.min_hand_orig, self.center, min_pivot, min_angle)
