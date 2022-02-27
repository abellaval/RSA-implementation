from manim import *

HOME = "Icons/"


class AliceToBobMess(Scene):

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
        # Label 
        alice_name = Tex("Alice").next_to(alice_img.get_top(), UP)
        bob_name = Tex("Bob").next_to(bob_img.get_top(), UP)

        self.play(FadeIn(eye), Write(alice_name), FadeIn(alice_img), Write(bob_name), FadeIn(bob_img))
        self.play(FadeIn(msg))
        runtime = 3
        self.play(msg.animate.next_to(bob_img.get_bottom() - np.array([0, spc_alice_bob_msg, 0]), DOWN), run_time=runtime)
        time_to_speak = 5
        self.wait(time_to_speak - runtime)