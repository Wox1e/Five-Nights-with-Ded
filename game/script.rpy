

# Определение персонажей игры.
define ded = Character('Дед Захар', color="#00b9d2")
define gg = Character("Матвей", color="#0526ab")
define fm = Character("Рыбак", color="#0526ab")

image bg bus_window_factory = "bus_window_factory.png"
image bg bus_window_village = "bus_window_village.png"
image bg bus_inside = "bus_inside.png"
image bg bus_stop = "bus_stop.png"
image bg black_bg = "black_bg.png"
image bg forest_trail = "forest_trail.png"
image bg lake = "lake.png"
image bg lake_fire = "lake_fire.png"
image bg school = "school.png"
image bg fishing_camp = "fishing_camp.png"
image bg farm = "farm.png"
image playground = "playground.png"


image ded stay = "ded.png"
image gg stay = "gg.png"

image house front = "house_front.png"
image house livingroom = "house_living_room.png"
image house medal box = "house_medal_box.png"

image wood chopping = "minigames/image.png"

transform stretch_to_screen:
    size (1920, 1080) # Точный размер


# Игра начинается здесь:
label start:
    stop music
    play sound "bus_long.ogg"
    scene bus_window_factory 
    "В окне показались трубы заводов - угрюмая, привычная реальность подоплёкой несостоявшейся молодежи и сотен коммерсантов"
    

    show gg stay

    gg "за час уже добрался до промзоны - совсем скоро я наконец покину Казань - город, в котором я пытался начать лучшую жизнь …"

    play sound "bus.ogg"

    scene bus_inside

    gg "Надеюсь меня никто не заметил"
    
    hide gg stay
    "Наконец покинув город, Матвей смог расслабиться и незаметно для себя задремал"

    scene black_bg

    ## Звук удара еблом
    
    show gg stay
    gg "Ай! Какого…"


    scene bus_inside

    gg "Точно, я же уехал с города… Главное отсидеться и начну новую жизнь"
    
    hide gg stay
    "За окном начали мелькать деревья загараживающие солнце, которые то и дело слепили из-за листвы. Качество дороги снижалось по мере продвижения к месту назначения…"    
    
    show gg stay
    gg "Надеюсь Ринат не догадается что это я украл деньги. Подозрительно конечно, что я заранее предупредил о том что уеду в другой город, но у них были большие надежды на меня, не скоро просекут фишку…"


    scene bus_window_village
    
    
    hide gg stay
    "За горизонтом виднеется поворот, пункт назначения близится"

    show gg stay
    gg "Опять со стариком ютится, от одной мысли об этом угрюмом хрыче тошно. Если б не отец… Сейчас бы жил как все."
    

    ## Звук торможения автобуса
    
    hide gg stay
    scene black_bg

    # Звуки шагов и уезжающего автобуса
    
    show gg stay
    gg "ну здравствуй, Епштейновка"

 
    scene bus_stop
 
    # Крутая музыка на фоне из 2006

    hide gg stay
    "Матвей слегка потянулся, когда автобус стало совсем не видно за горизонтом поднял свою сумку с земли и пошёл по с детства знакомой дороге."
    "Солнечный свет слепил глаза, на улице было жарко и душно из-за влаги, приносимой легким ветром с местной маленькой речушки по мере того, как он спускался вниз - к деревне"

    ## Картинку с дубом вставьте
    
    show gg stay
    gg " Аня… Да, местные мальчишки любили над нами подшучивать, сейчас она, наверное, учиться в каком-нибудь престижном универе"
    
    hide gg stay
    "Из деревни почти не доносилось звуков, за исключением еле слышимых ударов топора и периодическое мычание коров."

    "Зной. На улице никого не было видно."

    ## Тоже картинку сделайте какую-нить

    "Поравнявшись с первыми домами Матвей невольно остановился, засмотревшись на знакомые пейзажи: первый дом явно представлял из себя неплохое хозяйство - об этом свидетельствовала аккуратно скошенная трава перед домом, гуси и коза, стоявшая на привязи к столбу, да чуть ржавый трактор"
    "Картину удручали только выцвевшие покосившиеся ворота. "
    "Дом выглядел жилым, что нельзя сказать о соседних: покосившихся от времени, крыши которых давно провалились вовнутрь, а сады выглядели как одичавшие виноградники"

    ## Картинка развилки

    scene black_bg
    show gg stay
    gg "И куда же тут идти то… Надо подумать."
    
    
label choise1_loop:
    menu:
        "Озеро":
            jump lake
        "Школа":
            jump school
        "Рыбацкая беседка":
            jump fishing
        "Колхоз":
            jump farm
        "Детская площадка":
            jump playground
            
label lake:
    gg "Так… В той стороне вроде было озеро. Там сейчас наверное прохладно, схожу для начала туда."
    scene forest_trail
    hide gg stay
    "Летние лучи прорывались сквозь изумрудный лес, освещая тропу к озеру."
    "Чуть поодаль, среди деревьев виднелся старый домик местного лесничего. Покрытый мхом, с разбитым окном."
    show gg stay
    gg "Странно. Когда я уезжал новый лесник только поселился в этой избе."
    gg "Надо будет потом проверить что там случилось."
    gg "Но сначала к озеру…"
    scene lake
    gg "Неплохой вид. Всяко лучше грёбанной Казани с ее мелкими улочками."
    gg "Нда, вроде и глушь, но свои плюсы имеются."
    hide gg stay
    "На неровную от ветром поднятых волн поверхность голубого озера изредка опускались хищные птицы в попытках поймать добычу."
    "Другой берег выглядел неухоженным. То и неудивительно, с той стороны нет других деревень."
    "Солнце отражалось в воде и с удвоенной силой ослепляло, приятный для любых глаз вид."
    "Местная фауна тоже жила своей жизнью, звуки стрёкота насекомых раздавались эхом в голове, отчего казалось что они шумят не где-то в лесу, а в голове."
    scene lake_fire
    show gg stay
    gg " Видимо озеро пользуется популярностью у местных, кто-то из молодёжи кострище сделал."
    gg "Ладно, надо топать в другое место."
    hide gg stay
    jump choise1_loop
label school:
    hide gg stay
    scene school
    "Местная школа выделялась только тем, что была старше чем вся деревня."
    "Лишь в двух окнах горел свет, видимо это были те редкие её обитатели, учителя и директор, которые пили чай, вместо уроков, за неимением в ней учеников."
    show gg stay
    gg "Унылое местечко, здесь я рос, здесь научился курить, здесь же впервые узнал про понятия."
    gg "Учителя тоже те еще забулдыги, трудовик, помнится, трезвым вообще не появлялся."
    gg "И вот как я должен был вырасти пай-мальчиком в этом дерьме?"
    gg "Не буду здесь задерживаться, от одного вида тошнит."
    hide gg stay
    jump choise1_loop
label fishing:
    scene fishing_camp
    "Дорога к местной речке ничем не выделялась, в отличие от нее самой."
    "Сама по себе река не была сильно широкой, однако тянулась через всю длину деревни и уходила вдаль. Здесь излюбленная рыбацкая зона."
    "Чуть левее сидел рыбак, судя по надутой сумке - явно не местный."
    show gg stay left
    gg "Здаров, мужик. Есть клёв?"
    show fm right
    fm "В последнее время людей все меньше и меньше"
    fm "А оно, как грится, меньше народу - больше клёву."
    gg "Остроумно. Какие новости в деревне?"
    fm "Я сам не местный, точно не знаю. Но если подумать…"
    fm "Да как у всех других думаю, молодняк весь разъехался кто куда."
    fm "Старики-мразматики  про бесовщину всякую говорят. Чёрт его знает что там у них, сам проверь если хочешь."
    gg "Понятно что ничего непонятно. Бывай, мужик."
    hide gg stay
    jump choise1_loop
label farm:
    scene farm
    "Чуть дальше входа в деревню виднелся местный колхоз, давно никем не пользуемый. Туда даже юноши не бегали хулиганить видимо, не было видно никаких тропок."
    gg "Ну нет, через заросли я не потопаю, да и вряд ли там что-то интересное будет."
    hide gg stay
    jump choise1_loop
label playground:
    scene playground
    "Обычная детская площадка: турник, ржавая, еле крутящаяся карусель, да песочница с минимальным количеством песка."
    "В паре метров от основной площадки вход на корт"
    "Впрочем от корта там 2 рукодельные воротины, затерявшиеся в высоченной траве,  да выцветший забор."
    show gg stay
    gg "Помнится мы с местными пацанами здесь часто собирались, турник…"
    gg "Раньше мы его использовали только чтоб ковры выбивать, а если я…"
    
    # гг подходит к турнику, запрыгивает и делает пару подтягиваний
    gg "фух, мда, спорт явно не моё."
    
    # дальше не пишите, будем редачить
    
    # Походульки кончились, идём к деду
    
    scene house front
    show gg stay
    gg "А вот и дом старика. Да, давно я тут не был"
    gg "Сирень, которую мы сажали с бабкой-то совсем выросла"
    gg "Приехал бы на месяц раньше, может застал как она цветёт"
    gg "Учитывая как она выросла, аромат стоял бы на всю округу и весь двор"
    
    hide gg stay
    "Сам дом едва ли изменился за те 4 года"
    "Учитывая, что всё хозяйство держалось в руках Захара Ивановича - крепких, но уже ослабевающих, можно было простить и просевшие ворота, и местами облезлую краску на деревянном заборе"
    "Так или иначе дом выглядел гораздо лучше многих в этой деревне"
    "Только две вещи заметно бросались в глаза:"
    "После большого города он стал казаться приземистее и скромнеее что ли"
    "А ещё любимый бабушкин сад перед домом казался преступно заброшенным…"
    
    show gg stay
    gg "Так, ладно. Дед должен быть дома, ну-ка"
    
    # гг делает 3 попытки постучать в дверь, никто не открывает
    gg "Вот старый же, куда запропастился только?"
    gg "Ладно, обойду дом, может чего полезного найду"
    
    show gg stay
    gg "Первое впечатление о саде оказалось всё-таки немного ошибочным - он не был заброшен абсолютно"
    gg "Да, он не был настолько прилежно ухожен как раньше, но было видно, как кто-то продолжал за ним ухаживать"
    gg "Делал он это явно без чувства вкуса или какой-то самоотдачей, а скорее по инерции, но любовь, приложенная к делу всё-таки чувствовалась"
    
    gg "После того как бабка померла, сад представляет собой лишь тень прошлой красоты"
    gg "Не то чтобы он раньше был прям произведением искусства"
    gg "Но сейчас тем более"
    gg "а вот тут я любил играть…"
    gg "когда-то давно дед с отцом наметили какую-то стройку или ремонт, закупили песка и высыпали прямо здесь"
    gg "таким образом я и получил эту импровизированную песочницу"
    gg "как можно понять по оставшемуся песку - закончили они едва ли"
    gg "Так, и где там все-таки дед?"
    
    hide gg stay
    "За домом открылся вид на большое поле принадлежавшее хозяину дома. Половина была не засажено, а просто напросто заросшее"
    "На лавке, около стен бани, сидел дед и что-то ножом вырезал из дерева"
    "заслышав незаметно подкравшегося внука, он не успел было обрадоваться (слишком увлечен был делом), однако быстро опомнился и выжидающе, с удивлением и легкой радостью уставился на Матвея"
    
    show gg stay
    gg "Ну привет, дед."
    gg "Ты, смотрю, живой еще."
    
    hide gg stay
    "и тут волна разочарования и непонимания прокатилась в Захаре Ивановиче"
    "что-то было не то в любимом внуке"
    "с первого взгляда на него были заметны изменения"
    "только деду было непонятно какие именно они были и чем вызваны"
    
    show ded stay at center:
        xsize 1280 
        ysize 720

    ded "<цок> здравствуй, матвейка"
    ded "а маленький такой добрый, вежливый был. Проходи уж"
    
    show gg stay at right:
        xsize 800
        ysize 600
    gg "И без твоего разрешения прошел уже"
    gg "Я тут у тебя временно перекантуюсь, отдохну так сказать, в этой дыре Так что  я мешать не буду и ты не мешай, дальше своими делами старческими занимайся"
    
    show ded stay at left:
        xsize 800
        ysize 600

    ded "А я то уж думал, навестить пришел на старости лет, эх ты."
    ded "Ну проходи, комната сам знаешь где"
    
    show gg stay
    gg "ага, не забыл уж"
    
    hide gg stay
    "Матвей заходит в дом"
    
    scene house livingroom

    show gg stay
    gg "Надо же, вроде и времени сколько прошло, а тут все так же. Начиная от каждой вещички, заканчивая звуком крутящегося счётчика на стене"
    gg "даже отрывной календарь остался висеть тот же"
    gg "мда…"
    
    hide gg stay
    "действительно, комната казалась как будто законсервированной, в воздухе так и витало чувство ностальгии."
    "тут и черно-белые картины молодых бабушки с дедушкой и отец в детстве, ковёр на стене, старенькая добротная кровать на стальной сетке"
    gg "и непременный дедушкин кассетный радиоприемник"
    
    hide gg stay
    "только весь интерьер казался немного более пыльным, чем прежде, но картину это ни капли не омрачало"
    
    show gg stay
    gg "и какой же музыкой он себя развлекал тут?"
    gg "интересно, он ещё вообще рабочий?"
    # гг выключает радио
    gg "что ж, недурно"
    gg "у деда определенно есть музыкальный вкус"
    gg "сорокалетней выдержки"
    
    gg "ладно, надо б уже располагаться в этой комнате"
    gg "и желательно запрятать бы свою сумку подальше от старого"
    gg "например под кровать"
    
    hide gg stay
    "но при попытке спрятать что-то помешало багажу уместиться подальше под кроватью"
    "это была небольшая коробочка с чем-то звенящим внутри"
    
    scene house medal box

    gg "медали"
    gg "точно, дед же во время войны служил где-то на флоте"
    gg "а вообще странно, что он режил спрятать их здесь, в темноте и пыли подальше ото всех"
    gg "особенно его гордость: медали “За отвагу” и “Оборону ленинграда”"
    gg "были б у меня такие медали.."
    
    "дед заходит в комнату"
    
    scene house livingroom
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "музычку решил послушать?"
    


    "Захар Иванович незаметно прокрался в комнату, застав врасплох своего внука, так что Матвей даже чуть вздрогнул от неожиданности"
    gg "блин, не вовремя он конечно"
    gg "главное, чтоб он по моей реакции ничего не подумал и не начал задавать лишних вопросов"
    
    hide gg stay
    "отодвинув коробку с медалями в сторону и как можно скорее запихнув сумку подальше, Матвей наконец вылез из-под кровать, стараясь не показывать своим видом лёгкий испуг, что испытал секундой ранее"
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "Смотрю, ты быстро тут освоился. Пошли хоть чай попьешь, расскажешь как оно в городе-то"
    
    show gg stay at right:
        xsize 800
        ysize 600
    gg "Ладно,  дают - бери."
    
    hide gg stay
    "ну что, внучек, что тебя привело обратно к нам?"
    
    show gg stay
    gg "Эээ,  да то тут то там, проблем по мелочи нахватал, вот отдохнуть решил."
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "Ээх, всё и сразу никогда не получишь, не просто так ведь говорили тебе старики"
    
    show gg stay at right:
        xsize 800
        ysize 600
    gg "Да чтоб ты ещё понимал ….. старый."
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "Так, не ёрничай мне тут. А ну рассказывай, куда ввязался"
    
    show gg stay at right:
        xsize 800
        ysize 600
    gg "Хватит допытываться, а то больше на бабку нашу походишь любопытством."
    
    hide gg stay
    "после этих слов лицо Захара Ивановича утратило свою угрюмость, он слегка потупился, но потом невозмутимо продолжил"
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "Ты с дороги устал наверно, а после долго пути нет ничего приятнее, чем сходить в хорошую баньку"
    
    show gg stay at right:
        xsize 800
        ysize 600
    gg "Ох не нравится мне это"
    
    show ded stay at left:
        xsize 800
        ysize 600
    ded "А её сперва нужно заслужить"
    
    # дед резко хмуреет, косо смотрит, встаёт из-за стола
    show ded stay at left:
        xsize 800
        ysize 600
    ded "я тебя с дороги накормил, коль хочешь жить тут, будешь у меня тут за вместо юнги"
    ded "марш работать!"
    
    show gg stay at right:
        xsize 800
        ysize 600

    gg "Не было печали…"
    
    hide ded stay

    scene wood chopping


    hide gg stay
    
    show ded stay at left:
        xsize 1920
        ysize 1080

    "ну что, не разучился ещё топором орудовать?"

    hide ded stay
    
    
    show gg stay at right:
        xsize 1920
        ysize 1080
    gg "он во мне девочку совсем видит?"
    
    hide gg stay
    "НЕ РАЗОЧАРУЙ ДЕДА"
    

    # default minigame_score = 0
    
    init python:
        import random
        import pygame

        score = 0

        class ChoppingGameCDD(renpy.Displayable):
            def __init__(self):
                super(ChoppingGameCDD, self).__init__()
                
                # --- Загрузка графики ---
                self.sprite = renpy.displayable("images/minigames/image.png")
                self.hit_frames = [renpy.displayable(f"images/minigames/animation_set/hit/r{i}.png") for i in range(2)]
                self.miss_frames = [renpy.displayable(f"images/minigames/animation_set/miss/r{i}.png") for i in range(1)]
                
                # --- Состояние игры ---
                self.level = 1
                self.score = 0
                self.cursor_speed = 500.0  # Скорость (пикселей в секунду)
                self.cursor_x = 500.0
                
                self.win_zone_size = 40
                self.win_zone_x = self.generate_win_x()
                self.win_zone_moving = False
                self.win_zone_moving_rate = 0.0
                self.win_zone_direction = 1  # 1 - вправо, -1 - влево
                
                self.plays_counter = 0
                self.LEVEL_PLAYS = 3
                
                # --- Анимации ---
                self.current_anim = None
                self.anim_start_st = 0
                self.last_st = 0
                

            def generate_win_x(self):
                # 500 (начало бара) + отступ. 700 - длина бара.
                return 500 + random.randint(50, 650 - self.win_zone_size)

            def change_level(self):
                self.level += 1
                if self.level == 2:
                    self.win_zone_size = 20
                elif self.level == 3:
                    self.win_zone_size = 30
                    self.cursor_speed *= 1.4
                elif self.level == 4:
                    self.win_zone_size = 20
                    self.cursor_speed *= 1.1
                elif self.level == 5:
                    self.win_zone_moving = True
                    self.win_zone_moving_rate = 100.0 # Скорость зоны
                elif self.level == 6:
                    self.win_zone_moving_rate = 150.0
                    self.win_zone_size = 25
                elif self.level == 7:
                    return self.score
                
                return None

                self.win_zone_x = self.generate_win_x()
                renpy.restart_interaction()

            def render(self, width, height, st, at):
                render = renpy.Render(width, height)
                
                # Инициализация времени
                if self.last_st == 0:
                    self.last_st = st

                dt = st - self.last_st
                self.last_st = st

                # 1. Фон (основной спрайт)
                bg_render = renpy.render(self.sprite, width, height, st, at)
                render.blit(bg_render, (0, 0))

                # 2. Обновление позиций
                self.cursor_x += self.cursor_speed * dt
                if self.cursor_x > 1200: 
                    self.cursor_x = 500

                if self.win_zone_moving:
                    self.win_zone_x += self.win_zone_moving_rate * self.win_zone_direction * dt
                    if self.win_zone_x > 1100 or self.win_zone_x < 500:
                        self.win_zone_direction *= -1
                        # Гарантируем, что зона не выйдет за границы
                        self.win_zone_x = max(500, min(1100, self.win_zone_x))

                # 3. Логика анимации попадания/промаха
                if self.current_anim is not None:
                    anim_duration = 0.6  # 300 мс на всю анимацию
                    time_since_anim = st - self.anim_start_st
                    
                    if time_since_anim < anim_duration:
                        # Показываем анимацию
                        frame_idx = int((time_since_anim / anim_duration) * len(self.current_anim))
                        frame_idx = min(frame_idx, len(self.current_anim) - 1)
                        
                        anim_disp = self.current_anim[frame_idx]
                        fr_render = renpy.render(anim_disp, width, height, st, at)
                        render.blit(fr_render, (0, 0))
                        
                        # Запрашиваем перерисовку для следующего кадра
                        renpy.redraw(self, 0.01)
                    else:
                        # Анимация закончилась
                        self.current_anim = None

                # 4. Рисование игровых элементов
                canvas = render.canvas()
                
                # Серый бар (фон)
                canvas.rect("#909090", (500, 1000, 700, 30))
                
                # Зеленая зона успеха
                win_color = "#84fc00"
                if self.current_anim == self.hit_frames and time_since_anim < 0.3:
                    # Мигание при попадании
                    if int(st * 10) % 2 == 0:
                        win_color = "#ffffff"
                
                canvas.rect(win_color, (int(self.win_zone_x), 1000, self.win_zone_size, 30))
                
                # Курсор
                cursor_color = "#ffffff"
                if self.current_anim == self.miss_frames and time_since_anim < 0.3:
                    cursor_color = "#ff0000"  # Красный при промахе
                elif self.current_anim == self.hit_frames and time_since_anim < 0.3:
                    cursor_color = "#00ff00"  # Зеленый при попадании
                
                canvas.rect(cursor_color, (int(self.cursor_x), 1000, 3, 30))
                
                # Рамка вокруг зоны
                canvas.rect("#000000", (int(self.win_zone_x), 1000, self.win_zone_size, 30), width=2)


                if self.current_anim is None:
                    renpy.redraw(self, 1.0 / 90.0)  # 90 FPS для плавного движения
                else:
                    renpy.redraw(self, 0.01)  # Быстрая перерисовка для анимации


                return render

            def event(self, ev, x, y, st):
                # Всегда обрабатываем события для обновления состояния
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE:
                        # Проверка попадания
                        is_hit = self.win_zone_x <= self.cursor_x <= (self.win_zone_x + self.win_zone_size)
                        
                        if is_hit:
                            self.score += 10 * self.level
                            self.current_anim = self.hit_frames
                        else:
                            self.current_anim = self.miss_frames
                        
                        self.anim_start_st = st
                        self.plays_counter += 1
                        
                        # Логика уровней
                        if self.plays_counter >= self.LEVEL_PLAYS:
                            self.plays_counter = 0
                            score = self.change_level()

                            if score:
                                store.minigame_score = self.score
                                return score
                        else:
                            self.win_zone_x = self.generate_win_x()
                        
                        # Обновляем отображение
                        renpy.redraw(self, 0)
                    
                
                # ВАЖНО: Возвращаем None только если не хотим завершить экран
                # Это позволяет Ren'Py продолжать обновлять дисплей
                return None

            def visit(self):
                return [self.sprite] + self.hit_frames + self.miss_frames

    screen chopping_minigame():
        add ChoppingGameCDD()
        



    call screen chopping_minigame


    scene wood chopping

    show ded stay at center:
        xsize 1024
        ysize 720

    "You have [minigame_score] points."




    
    # завершение сценария
    return
