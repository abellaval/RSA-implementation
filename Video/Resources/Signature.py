from manim import *

HOME = "Icons/"


class Signature(Scene):

    def construct(self):
        self.exchange()

        msg   = ImageMobject(f"{HOME}LetterClosed.png").scale(0.5).next_to(self.alice_img, RIGHT)
        self.play(FadeIn(msg))

        self.lock_open_alice.next_to(msg, UP + RIGHT)
        self.lock_open_alice.shift(0.7 * LEFT + 0.5 * DOWN)
        self.play(FadeIn(self.lock_open_alice))


        # Close lock 
        self.lock_close_alice.shift(self.lock_open_alice.get_center())
        self.lock_open_alice.next_to(self.lock_close_alice, ORIGIN)
        self.play(FadeIn(self.lock_close_alice), FadeOut(self.lock_open_alice))
        self.wait(0.5)


        move = 6
        self.play(msg.animate.shift(move * RIGHT), self.lock_close_alice.animate.shift(move * RIGHT))
        self.wait(0.5)
        

        self.play(self.key_red_exch.animate.next_to(self.lock_close_alice))
        # self.play(self.key_green.animate.next_to(self.bob_img, DOWN))
        # self.play(self.key_green.animate.shift(0.5 * RIGHT), run_time=0.5)

        # Open lock
        self.lock_open_alice.shift(self.lock_close_alice.get_center())
        self.lock_open_alice.next_to(self.lock_close_alice, ORIGIN)
        self.play(FadeOut(self.lock_close_alice), FadeIn(self.lock_open_alice))

        tick = Text(" ✓ ", color=GREEN)
        tick.next_to(msg, DOWN)
        self.play(Write(tick))
        self.wait(1)



        
    def exchange(self):
        buff_eye = 0.5
        eye = ImageMobject(f"{HOME}Eye.png").scale(0.5).to_edge(UP, buff=buff_eye)

        # Alice et Bob
        buff_img = 1
        self.alice_img = ImageMobject(f"{HOME}Woman.png").to_edge(LEFT, buff=buff_img)
        self.bob_img = ImageMobject(f"{HOME}Men.png").to_edge(RIGHT, buff=buff_img)
        spc_alice_bob_cadena_clef = 0.5

        lock_open_red = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.3).next_to(self.alice_img.get_bottom() - np.array([0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        key_red = ImageMobject(f"{HOME}KeyRed.png").scale(0.3).next_to(self.alice_img.get_bottom() - np.array([-0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        self.lock_open_alice = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.3).next_to(self.alice_img, DOWN)
        self.lock_close_alice = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.3)
        self.lock_open_alice.next_to(self.alice_img, UP)
        self.lock_open_alice.shift(0.5, RIGHT)

        lock_open_green = ImageMobject(f"{HOME}Lock-Open-256.png").scale(0.3).next_to(self.bob_img.get_bottom() - np.array([0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        self.key_green = ImageMobject(f"{HOME}KeyGreen.png").scale(0.3).next_to(self.bob_img.get_bottom() - np.array([-0.5, spc_alice_bob_cadena_clef, 0]), DOWN)

        self.key_green_exch = ImageMobject(f"{HOME}KeyGreen.png").scale(0.3).next_to(self.bob_img.get_top() + np.array([-1, 0, 0]), UP)
        self.key_red_exch = ImageMobject(f"{HOME}KeyRed.png").scale(0.3).next_to(self.alice_img.get_top() + np.array([1, 0, 0]), UP)

        # Label 
        alice_name = Tex("Alice").next_to(self.alice_img.get_top(), UP)
        bob_name = Tex("Bob").next_to(self.bob_img.get_top(), UP)

        # play img principales
        self.play(FadeIn(eye), Write(alice_name), FadeIn(self.alice_img), Write(bob_name), FadeIn(self.bob_img))

        # play cadena
        self.play(FadeIn(lock_open_red), FadeIn(lock_open_green))
        # play clef
        self.play(FadeIn(key_red), FadeIn(self.key_green))

        # swap lock and key
        self.wait(0.5)
        self.play(lock_open_red.animate.shift(RIGHT), key_red.animate.shift(LEFT), lock_open_green.animate.shift(RIGHT), self.key_green.animate.shift(LEFT))

        # play cadena à échanger
        self.play(FadeIn(self.key_green_exch), FadeIn(self.key_red_exch))
        # play échange
        runtime = 2
        self.play(self.key_red_exch.animate.next_to(self.bob_img.get_top() + np.array([-1, 0, 0]), UP),
                self.key_green_exch.animate.next_to(self.alice_img.get_top() + np.array([1, 0, 0]), UP), run_time=runtime)
        self.wait(1)
        
