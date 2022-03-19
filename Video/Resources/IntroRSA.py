from email import message
from socket import MsgFlag
from manim import *
from numpy import meshgrid

HOME = "Icons/"


class IntroRSA(Scene):

    def construct(self):
        # Img
        # Eye
        buff_eye = 0.5
        eye = ImageMobject(f"{HOME}Eye.png").scale(0.5).to_edge(UP, buff=buff_eye)
        # Alice et Bob
        buff_img = 1
        alice_img = ImageMobject(f"{HOME}Woman.png").to_edge(LEFT, buff=buff_img)
        bob_img = ImageMobject(f"{HOME}Men.png").to_edge(RIGHT, buff=buff_img)
        spc_alice_bob_msg = 0.5
        msg = ImageMobject(f"{HOME}LetterClosed.png").scale(0.5).next_to(alice_img.get_bottom() - np.array([0, spc_alice_bob_msg, 0]), DOWN)
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

        self.play(FadeIn(eye), Write(alice_name), FadeIn(alice_img), Write(bob_name), FadeIn(bob_img))
        self.play(FadeIn(msg))
        runtime = 3
        self.play(msg.animate.next_to(bob_img.get_bottom() - np.array([0, spc_alice_bob_msg, 0]), DOWN), run_time=runtime)
        tts1 = 5
        self.wait(tts1)
        self.play(FadeOut(msg))
        tts2 = 2
        self.wait(tts2)
        # play cadena
        self.play(FadeIn(lock_open_red), FadeIn(lock_open_green))
        # play clef
        self.play(FadeIn(key_red), FadeIn(key_green))
        tts3 = 3
        self.wait(tts3)
        # play cadena à échanger
        self.play(FadeIn(lock_open_green_ech), FadeIn(lock_open_red_ech))
        # play échange
        runtime = 2
        self.play(lock_open_red_ech.animate.next_to(bob_img.get_top() + np.array([-1, 0, 0]), UP), lock_open_green_ech.animate.next_to(alice_img.get_top() + np.array([1, 0, 0]), UP), run_time=runtime)

        self.wait(2)

        msg_alice = ImageMobject(f"{HOME}LetterClosed.png").scale(0.3).next_to(alice_img.get_right(), RIGHT)

        boite = ImageMobject(f"{HOME}Product-256.png").scale(0.6).next_to(msg_alice.get_right() + np.array([1, 0, 0]), RIGHT)

        self.play(FadeIn(msg_alice))

        self.play(FadeIn(boite))

        self.play(msg_alice.animate.next_to(boite.get_center(), ORIGIN))

        self.play(FadeOut(msg_alice))

        self.play(FadeIn(lock_open_green_ech))

        self.play(lock_open_green_ech.animate.next_to(boite.get_right(), UP))

        lock_close = ImageMobject(f"{HOME}Lock-256(1).png").scale(0.3).next_to(lock_open_green_ech.get_center(), ORIGIN)

        self.play(FadeOut(lock_open_green_ech), FadeIn(lock_close))

        msg_ouvert = ImageMobject(f"{HOME}LetterOpen.png").scale(0.3).next_to(bob_img.get_left(), LEFT)

        self.play(boite.animate.next_to(msg_ouvert.get_left() - np.array([1, 0, 0]), LEFT), lock_close.animate.next_to(msg_ouvert.get_left() - np.array([0.7, -0.5, 0]), LEFT))

        self.play(FadeIn(key_green))

        self.play(key_green.animate.next_to(lock_close.get_right(), ORIGIN))

        lock_open_green_ech.next_to(lock_close.get_center(), ORIGIN)

        self.play(FadeOut(lock_close), FadeIn(lock_open_green_ech))

        self.play(key_green.animate.next_to(bob_img.get_bottom() - np.array([-0.5, spc_alice_bob_cadena_clef, 0]), DOWN))

        msg_alice.next_to(boite.get_center(), ORIGIN)

        self.play(FadeIn(msg_alice))

        self.play(msg_alice.animate.next_to(msg_ouvert.get_center(), ORIGIN))

        self.play(FadeOut(msg_alice), FadeIn(msg_ouvert))