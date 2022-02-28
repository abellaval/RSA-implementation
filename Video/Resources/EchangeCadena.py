from manim import *

HOME = "Icons/"


class EchangeCadena(Scene):

    def construct(self):
        # Img
        # Eye
        buff_eye = 0.5
        eye = ImageMobject(f"{HOME}Eye.png").scale(0.5).to_edge(UP, buff=buff_eye)
        # Alice et Bob
        buff_img = 1
        alice_img = ImageMobject(f"{HOME}Woman.png").to_edge(LEFT, buff=buff_img)
        bob_img = ImageMobject(f"{HOME}Men.png").to_edge(RIGHT, buff=buff_img)
        spc_alice_bob_cadena_clef = 0.5
        lock_open_red = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.3).next_to(alice_img.get_bottom() - np.array([0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        key_red = ImageMobject(f"{HOME}KeyRed.png").scale(0.3).next_to(alice_img.get_bottom() - np.array([-0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        lock_open_green = ImageMobject(f"{HOME}Lock-Open-256.png").scale(0.3).next_to(bob_img.get_bottom() - np.array([0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        key_green = ImageMobject(f"{HOME}KeyGreen.png").scale(0.3).next_to(bob_img.get_bottom() - np.array([-0.5, spc_alice_bob_cadena_clef, 0]), DOWN)
        lock_open_green_ech = ImageMobject(f"{HOME}Lock-Open-256.png").scale(0.3).next_to(bob_img.get_top() + np.array([-1, 0, 0]), UP)
        lock_open_red_ech = ImageMobject(f"{HOME}lockOpenRed.png").scale(0.3).next_to(alice_img.get_top() + np.array([1, 0, 0]), UP)
        # Label 
        alice_name = Tex("Alice").next_to(alice_img.get_top(), UP)
        bob_name = Tex("Bob").next_to(bob_img.get_top(), UP)
        # play img principales
        self.play(FadeIn(eye), Write(alice_name), FadeIn(alice_img), Write(bob_name), FadeIn(bob_img))
        # play cadena
        self.play(FadeIn(lock_open_red), FadeIn(lock_open_green))
        # play clef
        self.play(FadeIn(key_red), FadeIn(key_green))
        # play cadena à échanger
        self.play(FadeIn(lock_open_green_ech), FadeIn(lock_open_red_ech))
        # play échange
        runtime = 2
        self.play(lock_open_red_ech.animate.next_to(bob_img.get_top() + np.array([-1, 0, 0]), UP), lock_open_green_ech.animate.next_to(alice_img.get_top() + np.array([1, 0, 0]), UP), run_time=runtime)

        self.wait(5)
        