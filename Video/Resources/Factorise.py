from manim import *

HOME="Icons/"

class FactoriseShow(Scene):

    def construct(self):

        self.showFactoriseDanger()
        self.showFactoriseIsEasyForSmall()
        self.clear()
        self.showFactoriseIsHard()

    def showFactoriseIsHard(self):
        easy_calc = Tex("$384748747 \\times 278921381$", font_size=30)
        easy_calc.shift(3 * LEFT + 1 * UP)
        thumbs_up = ImageMobject(f"{HOME}Thumbs-Up-256.png").scale(0.4).to_edge(UP, buff=0.5)
        thumbs_up.next_to(easy_calc,RIGHT); thumbs_up.shift(1 * RIGHT)
        easy_t = Text("Facile pour un \n ordinateur !", font_size=30)
        easy_t.next_to(thumbs_up, RIGHT); easy_t.shift(1 * RIGHT)

        self.play(Write(easy_calc))
        self.add(thumbs_up)
        self.play(Write(easy_t))

        self.wait(1)

        hard_calc_text = Tex("Factoriser \\\\ $107314651851259607$ en ", font_size=30)
        hard_calc_text.shift(3 * LEFT + 1 * DOWN)
        hard_calc = Tex("$384748747 \\times 278921381$", font_size=30)
        hard_calc.next_to(hard_calc_text, DOWN)
        thumbs_down = ImageMobject(f"{HOME}Thumbs-Down-256.png").scale(0.4).to_edge(UP, buff=0.5)
        thumbs_down.next_to(hard_calc,RIGHT); thumbs_down.shift(1 * RIGHT)
        hard_t = Text("Très difficile \nmême pour un ordinateur \ntrès puissant !", font_size=25)
        hard_t.next_to(thumbs_down, RIGHT); hard_t.shift(1 * RIGHT)

        self.play(Write(hard_calc_text))
        self.play(Write(hard_calc))
        self.add(thumbs_down)
        self.play(Write(hard_t))

        self.wait(2)



    def showFactoriseIsEasyForSmall(self):
        easy_calc = Tex("$3 \\times 5$")
        easy_calc.shift(2 * LEFT + 1 * UP)
        thumbs_up = ImageMobject(f"{HOME}Thumbs-Up-256.png").scale(0.4).to_edge(UP, buff=0.5)
        thumbs_up.next_to(easy_calc,RIGHT); thumbs_up.shift(1 * RIGHT)
        easy_t = Text("Facile")
        easy_t.next_to(thumbs_up, RIGHT); easy_t.shift(1 * RIGHT)

        self.play(Write(easy_calc))
        self.add(thumbs_up)
        self.play(Write(easy_t))

        self.wait(1)

        easy_calc_text = Tex("Factoriser $15$ en ")
        easy_calc_text.shift(4.5 * LEFT + 1 * DOWN)
        easy_calc = Tex("$3 \\times 5$")
        easy_calc.next_to(easy_calc_text, RIGHT)
        thumbs_up = ImageMobject(f"{HOME}Thumbs-Up-256.png").scale(0.4).to_edge(UP, buff=0.5)
        thumbs_up.next_to(easy_calc,RIGHT); thumbs_up.shift(1 * RIGHT)
        easy_t = Text("Facile")
        easy_t.next_to(thumbs_up, RIGHT); easy_t.shift(1 * RIGHT)

        self.play(Write(easy_calc_text))
        self.play(Write(easy_calc))
        self.add(thumbs_up)
        self.play(Write(easy_t))

        self.wait(2)






    def showFactoriseDanger(self):
        N = Text("N")

        red_lock = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.5).to_edge(UP, buff=0.5)
        red_key  = ImageMobject(f"{HOME}KeyRed.png").scale(0.5).to_edge(UP, buff=0.5)
       
        rl_text = Text("e")
        rl_text.shift(4 * LEFT + 1 * UP)
        rleq = Text(" = ")
        rleq.next_to(rl_text, RIGHT)
        red_lock.next_to(rl_text, 4 * RIGHT)

        rk_text = Text("d")
        rk_text.shift(2 * RIGHT + 1 * UP)
        rkeq = Text(" = ")
        rkeq.next_to(rk_text, RIGHT)
        red_key.next_to(rk_text, 4 * RIGHT)

        self.add(red_lock, red_key)
        self.play(Write(rl_text), Write(rk_text), Write(rleq), Write(rkeq))
        g = VGroup(rl_text, rk_text)

        self.wait(2)
        self.remove(red_lock, red_key)
        self.remove(rleq, rkeq)
        self.wait(0.5)
        self.play(Transform(g, N))
        self.wait(1)
        self.clear()
        self.add(N)

        p = Text("p")
        p.shift(2 * LEFT)
        q = Text("q")
        q.shift(2 * RIGHT)

        g = VGroup(p, q)

        self.play(Write(Text("Factorisation de N").shift(2 * UP)))
        self.wait(1)
        self.play(Transform(N, g))
        self.wait(1)
        self.play(Write(Text("On connait maintenant les nombres secrets !", font_size=25).shift(2 * DOWN)))
        self.wait(2)
