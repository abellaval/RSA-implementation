from manim import *

HOME = "Icons/"

class AliceToBobFullMessage(Scene):

    def construct(self):
        self.makeScene()

        msg   = ImageMobject(f"{HOME}LetterClosed.png").scale(0.5)
        self.play(FadeIn(msg))
        hello = Text("Hello").scale(0.6).next_to(msg, DOWN)
        self.play(Write(hello))
        self.play(hello.animate.next_to(msg, ORIGIN))
        self.play(FadeOut(hello))
        self.wait(0.5)
        self.play(msg.animate.next_to(self.alice_img, RIGHT))

        self.lock_open_green_alice.next_to(msg, UP + RIGHT)
        self.lock_open_green_alice.shift(0.7 * LEFT + 0.5 * DOWN)
        self.play(FadeIn(self.lock_open_green_alice))

        # Close lock
        self.lock_close_green_alice.shift(self.lock_open_green_alice.get_center())
        self.lock_open_green_alice.next_to(self.lock_close_green_alice, ORIGIN)
        self.play(FadeIn(self.lock_close_green_alice), FadeOut(self.lock_open_green_alice))
        self.wait(0.5)

        move = 3
        self.play(msg.animate.shift(move * RIGHT), self.lock_close_green_alice.animate.shift(move * RIGHT))
        self.wait(0.5)

        
        lookup = ImageMobject(f"{HOME}Look.png").scale(0.6)
        lookup.next_to(msg, DOWN)
        self.play(FadeIn(lookup))
        hello_encrypted = Text("7234126\n1234971\n8305710\n2845102\n8167517", font_size=24)
        hello_encrypted.next_to(lookup)
        self.play(FadeIn(hello_encrypted))
        self.wait(0.5)
        self.play(FadeOut(lookup), FadeOut(hello_encrypted))

        move = 3
        self.play(msg.animate.shift(move * RIGHT), self.lock_close_green_alice.animate.shift(move * RIGHT))
        self.play(self.key_green.animate.next_to(self.lock_close_green_alice))

        # Open lock
        self.lock_open_green_alice.shift(self.lock_close_green_alice.get_center())
        self.lock_open_green_alice.next_to(self.lock_close_green_alice, ORIGIN)
        self.play(FadeOut(self.lock_close_green_alice), FadeIn(self.lock_open_green_alice))

        self.play(self.key_green.animate.next_to(self.lock_close_green_alice))
        self.play(self.key_green.animate.next_to(self.bob_img, DOWN))
        self.play(self.key_green.animate.shift(0.5 * RIGHT), run_time=0.5)

        lookup.next_to(msg, DOWN)
        self.play(FadeIn(lookup))
        hello.next_to(lookup, RIGHT)
        self.play(FadeIn(hello))

        self.wait(2)



    def makeScene(self):
        buff_eye = 0.5
        eye = ImageMobject(f"{HOME}Eye.png").scale(0.5).to_edge(UP, buff=buff_eye)

        buff_img = 1
        self.alice_img = ImageMobject(f"{HOME}Woman.png").to_edge(LEFT, buff=buff_img)
        self.bob_img = ImageMobject(f"{HOME}Men.png").to_edge(RIGHT, buff=buff_img)


        self.lock_open_green_alice = ImageMobject(f"{HOME}Lock-Open-256.png").scale(0.3).next_to(self.alice_img, DOWN)
        self.lock_close_green_alice = ImageMobject(f"{HOME}Lock-256(1).png").scale(0.3)
        self.lock_open_green_alice.next_to(self.alice_img, UP)
        self.lock_open_green_alice.shift(0.5, RIGHT)
        lock_open_red = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.3).next_to(self.alice_img, DOWN)
        key_red = ImageMobject(f"{HOME}KeyRed.png").scale(0.3).next_to(self.alice_img, DOWN)
        key_red.shift(0.5 * RIGHT)
        lock_open_red.shift(0.5 * LEFT)

        lock_open_green = ImageMobject(f"{HOME}Lock-Open-256.png").scale(0.3).next_to(self.bob_img, DOWN)
        self.key_green = ImageMobject(f"{HOME}KeyGreen.png").scale(0.3).next_to(self.bob_img, DOWN)
        self.key_green.shift(0.5 * RIGHT)
        lock_open_green.shift(0.5 * LEFT)

        # Label 
        alice_name = Tex("Alice").next_to(self.alice_img.get_top(), UP)
        bob_name = Tex("Bob").next_to(self.bob_img.get_top(), UP)

        self.play(FadeIn(eye), Write(alice_name), FadeIn(self.alice_img), Write(bob_name), FadeIn(self.bob_img))
        # self.play(FadeIn(lock_open_red), FadeIn(key_red), FadeIn(lock_open_green), FadeIn(self.key_green), FadeIn(self.lock_open_green_alice))
        self.play(FadeIn(lock_open_red), FadeIn(key_red), FadeIn(self.key_green), FadeIn(self.lock_open_green_alice))
