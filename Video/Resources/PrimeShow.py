from manim import *

class PrimeShow(Scene):
    def construct(self):
        self.eightIsNotPrime()
        self.wait(1)
        self.twentyOneIsNotPrime()
        self.wait(1)
        self.fiveIsPrime()
        self.wait(1)

    def eightIsNotPrime(self):
        n = Tex("$8$", color=RED)
        n.shift(2*UP)
        text = Text("N'est pas un nombre premier", color=RED)
        text.next_to(n, 3 * DOWN)
        
        self.play(Write(n))

        fd = Tex("$( 2 \\times 4 )$")
        self.showFactor(n, fd, -1)

        self.wait(0.5)
        self.play(Write(text))
        self.wait(1)

        self.remove(text)
        fd.next_to(n, DOWN)
        g = VGroup(n, fd)
        self.play(g.animate.shift(5 * LEFT))

    def twentyOneIsNotPrime(self):
        n = Tex("$21$", color=RED)
        n.shift(2*UP)
        text = Text("N'est pas un nombre premier", color=RED)
        text.next_to(n, 4 * DOWN)
        
        self.play(Write(n))

        fd = Tex("$( 3 \\times 7 )$")
        self.showFactor(n, fd, -1)

        self.wait(0.5)
        self.play(Write(text))
        self.wait(1)

        self.remove(text)
        fd.next_to(n, DOWN)
        g = VGroup(n, fd)
        self.play(g.animate.shift(5 * LEFT + 2 * DOWN))



    def fiveIsPrime(self):
        n = Tex("$5$", color=GREEN)
        n.shift(2*UP)
        text = Text("Non ! Donc 5 est bien un nombre premier !", font_size=40, color=GREEN)
        text.next_to(n, 4 * DOWN)
        
        self.play(Write(n))

        f = Tex("Peut il se décomposer en un produit de nombres ?", font_size=30)
        f.next_to(n, 2 * DOWN)
        self.play(Write(f))
        self.wait(2)
        self.play(Unwrite(f), run_time=0.5)
        self.play(Write(text))
        self.wait(1)

        fd = Text(" ✓ ", color=GREEN)
        fd.next_to(n, 2 * DOWN)
        fd.shift(2 * DOWN)
        self.play(Write(fd))
        self.wait(0.25)

        self.remove(text)
        fd.next_to(n, DOWN)
        g = VGroup(n, fd)
        self.play(g.animate.shift(5 * RIGHT + 1 * DOWN))
        

    def showFactor(self, n, fd, move):
        fd.next_to(n, 2 * DOWN)
        fd.shift(2 * DOWN)
        self.play(Write(fd))
        self.wait(0.5)

