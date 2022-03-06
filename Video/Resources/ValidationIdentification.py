from fnmatch import fnmatch
from manim import *

HOME = "Icons/"

class ValidationIdentification(Scene):

    def construct(self):
        default_buff = 0.5
        
        bob = ImageMobject(f"{HOME}Men.png").scale(1).to_edge(LEFT, buff=default_buff)
	


        admin_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(UP, buff=1.5)
        decompte_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(RIGHT, buff=1)

        urne_img = ImageMobject(f"{HOME}PollingBox.png").scale(0.5).to_edge(DOWN, buff=1)

        finger_print = ImageMobject(f"{HOME}Finger-Print.png").scale(0.3).next_to(bob, DOWN)

        check = ImageMobject(f"{HOME}Check-256.png").scale(0.3).next_to(admin_img.get_bottom(), RIGHT)

        cadena = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.3).next_to(admin_img.get_left(), LEFT)

        vote_choix = ImageMobject(f"{HOME}Vote-Choice.png").scale(0.3).next_to(cadena.get_left(), LEFT)

        card = ImageMobject(f"{HOME}Card.png").scale(0.3).next_to(vote_choix.get_left(), LEFT)

        pack = ImageMobject(f"{HOME}Product-256.png").scale(0.5).next_to(vote_choix.get_bottom(), DOWN)

		#text
        client = Tex("Bob").next_to(bob.get_top(), UP)
        amdin = Tex("Administrateur").next_to(admin_img.get_top(), UP)
        decompte = Tex("Décompte").next_to(decompte_img.get_top(), UP)
        urne = Tex("Urne").next_to(urne_img.get_top(), UP)


        self.play(FadeIn(bob), Write(client))

        self.play(FadeIn(admin_img), FadeIn(decompte_img), FadeIn(urne_img), Write(amdin), Write(urne), Write(decompte))

        self.play(FadeIn(finger_print))
        self.play(finger_print.animate.next_to(admin_img.get_bottom(), DOWN), run_time=3)
        
        self.play(FadeIn(check))
        self.wait(2)
        self.play(FadeOut(check), FadeOut(finger_print))


        self.play(FadeIn(card))

        self.play(FadeIn(vote_choix))

        self.play(FadeIn(cadena))

        self.wait(2)

        self.play(FadeIn(pack))

        self.wait(2)

        self.play(cadena.animate.next_to(pack.get_center(), ORIGIN), vote_choix.animate.next_to(pack.get_center(), ORIGIN), card.animate.next_to(pack.get_center(), ORIGIN))

        self.play(FadeOut(cadena), FadeOut(vote_choix), FadeOut(card))

        self.play(pack.animate.next_to(bob.get_right(), RIGHT))

        self.wait(2)

        self.play(FadeOut(pack))



        self.wait(5)