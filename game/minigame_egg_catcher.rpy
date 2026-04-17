init python:
    import random
    import pygame
    from renpy.text.text import Text

    class EggCatcherCDD(renpy.Displayable):
        def __init__(self, total_eggs=10, spawn_interval=1.0,
                    egg_start_speed=150.0, egg_acceleration=100.0, **kwargs):
            super(EggCatcherCDD, self).__init__(**kwargs)
            
            self.width = 1920
            self.height = 1080
            
            self.egg_start_speed = egg_start_speed
            self.egg_acceleration = egg_acceleration
            
            self.p_w, self.p_h = 150, 150
            self.p_x = self.width / 2 - self.p_w / 2
            self.p_y = self.height - self.p_h
            self.p_speed = 2400.0
            
            self.total_eggs = total_eggs
            self.spawn_interval = spawn_interval
            self.spawn_timer = 0.0
            self.eggs_spawned = 0
            self.eggs_processed = 0
            self.active_eggs = []
            self.e_w, self.e_h = 40, 48
            
            self.bg_img = renpy.displayable("images/minigames/bg_eggs.png")
            self.basket_img = renpy.displayable("images/minigames/basket.png")
            self.egg_imgs = [renpy.displayable(f"images/minigames/egg{i}.png") for i in range(1, 16)]
            
            self.score = 0
            self.keys_down = set()
            self.last_st = 0
            self.finished = False
            
        def spawn_egg(self):
            speed = self.egg_start_speed + (self.eggs_spawned * self.egg_acceleration)
            chosen_idx = random.randrange(15)
            
            self.active_eggs.append({
                'x': random.randint(0, self.width - self.e_w),
                'y': -self.e_h,
                'speed': speed,
                'img_idx': chosen_idx
            })
            self.eggs_spawned += 1
            self.spawn_timer = 0.0

        def render(self, width, height, st, at):
            if self.last_st == 0:
                self.last_st = st

            dt = st - self.last_st
            self.last_st = st
            dt = min(dt, 0.05)

            # Логика игры
            if not self.finished:
                if self.eggs_spawned < self.total_eggs:
                    self.spawn_timer += dt
                    if self.spawn_timer >= self.spawn_interval:
                        self.spawn_egg()

                if pygame.K_LEFT in self.keys_down:
                    self.p_x -= self.p_speed * dt
                if pygame.K_RIGHT in self.keys_down:
                    self.p_x += self.p_speed * dt
                self.p_x = max(0, min(self.width - self.p_w, self.p_x))

                to_remove = []
                for i, egg in enumerate(self.active_eggs):
                    egg['y'] += egg['speed'] * dt

                    if (egg['y'] + self.e_h > self.p_y and
                        egg['x'] + self.e_w > self.p_x and
                        egg['x'] < self.p_x + self.p_w):
                        self.score += 1
                        to_remove.append(i)
                    elif egg['y'] > self.height:
                        self.score -= 1
                        to_remove.append(i)

                for i in reversed(to_remove):
                    self.active_eggs.pop(i)
                    self.eggs_processed += 1

                if self.eggs_processed >= self.total_eggs and not self.active_eggs:
                    self.finished = True
                    store.egg_catcher_done = True
                    store.egg_catcher_score = self.score

            # Отрисовка без кэширования 
            render = renpy.Render(self.width, self.height)
            
            render.blit(renpy.render(self.bg_img, self.width, self.height, st, at), (0, 0))
            render.blit(renpy.render(self.basket_img, self.p_w, self.p_h, st, at), (int(self.p_x), int(self.p_y)))
            
            for egg in self.active_eggs:
                egg_r = renpy.render(self.egg_imgs[egg['img_idx']], self.e_w, self.e_h, st, at)
                render.blit(egg_r, (int(egg['x']), int(egg['y'])))
            
            ui_text = Text(f"Score: {self.score} | Eggs: {self.eggs_processed}/{self.total_eggs}", 
                            size=22, color="#000000", outlines=[(2, "#ffffff", 0, 0)])
            render.blit(renpy.render(ui_text, self.width, self.height, st, at), (10, 10))

            if not self.finished:
                renpy.redraw(self, 1.0 / 60.0)
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                self.keys_down.add(ev.key)
                if ev.key == pygame.K_ESCAPE:
                    store.egg_catcher_done = True
                    store.egg_catcher_score = self.score
                    self.finished = True
            elif ev.type == pygame.KEYUP:
                self.keys_down.discard(ev.key)
            return None

        def visit(self):
            return [self.bg_img, self.basket_img] + self.egg_imgs