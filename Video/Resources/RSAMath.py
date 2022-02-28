from manim import *

class PrimeShow(Scene):
    def construct(self):
        self.eightIsNotPrime()
        self.wait(2)
        self.clear()
        self.fiveIsPrime()

    def eightIsNotPrime(self):
        n = Tex("$8$", color=RED)
        
        self.play(Write(n))

        f = Tex("$8$")
        fd = Tex("$( 8 * 1 )$")
        self.showFactor(n, f, fd, 3)

        f = Tex("$4$")
        fd = Tex("$( 4 * 2 )$")
        self.showFactor(n, f, fd, 1)

        f = Tex("$2$")
        fd = Tex("$( 2 * 4 )$")
        self.showFactor(n, f, fd, -1)

        f = Tex("$1$")
        fd = Tex("$( 1 * 8 )$")
        self.showFactor(n, f, fd, -3)

        self.wait(1)

    def fiveIsPrime(self):
        n = Tex("$5$", color=GREEN)
        
        self.play(Write(n))

        f = Tex("$5$")
        fd = Tex("$( 5 * 1 )$")
        self.showFactor(n, f, fd, 2)

        f = Tex("$1$")
        fd = Tex("$( 1 * 5 )$")
        self.showFactor(n, f, fd, -2)

        self.wait(1)

    def showFactor(self, n, f, fd, move):

        f.next_to(n, DOWN)
        self.play(Write(f))

        fd.next_to(f, DOWN)
        self.play(Write(fd))
        self.wait(0.5)

        g = VGroup(f, fd)
        g.generate_target()
        g.target.shift(2 * DOWN); g.target.shift(move * LEFT)
        self.play(MoveToTarget(g))
