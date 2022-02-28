from manim import *

HOME = "Icons/"

class KeyShow(Scene):

    def construct(self):
        self.p_times_q()
        self.wait(2)
        self.clear()

        red_lock = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.5).to_edge(UP, buff=0.5)
        red_key  = ImageMobject(f"{HOME}KeyRed.png").scale(0.5).to_edge(UP, buff=0.5)

        rl_text = Text("e = ")
        rl_text.shift(1 * LEFT)
        red_lock.next_to(rl_text, RIGHT)
        rl_num = Tex("$65537$")
        rl_num.next_to(red_lock, RIGHT)
        g = VGroup(rl_text, rl_num)
        self.play(FadeIn(g), FadeIn(red_lock))
        self.wait(0.5)


        rk_text = Text("d = ")
        rk_text.shift(2 * DOWN)
        rk_text.shift(3 * LEFT)
        red_key.next_to(rk_text, RIGHT)
        rk_num = Tex("$159936150020144387547873$")
        rk_num.next_to(red_key, RIGHT)
        g = VGroup(rk_text, rk_num)
        self.play(FadeIn(g), FadeIn(red_key))

        self.wait(3)

    def p_times_q(self):
        p  = Text("p")
        pn = Tex("$3458763929$")
        pn.next_to(p, DOWN)
        gp = VGroup(p, pn)
        gp.move_to(4*LEFT)

        self.play(Write(gp))
        self.wait(1)
        
        times = Tex("$\\times$")
        self.play(Write(times))

        self.wait(1)

        q  = Text("q")
        qn = Tex("$8257482139$")
        qn.next_to(q, DOWN)
        gq = VGroup(q, qn)
        gq.move_to(4*RIGHT)

        self.play(Write(gq))

        self.wait(2)

        n  = Text("N")
        nn = Tex("$28560681366734964131$")
        nn.next_to(n, DOWN)
        gn = VGroup(n, nn)
        gn.move_to(2*DOWN)

        self.play(Write(gn))

