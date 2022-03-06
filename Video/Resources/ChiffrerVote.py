from fnmatch import fnmatch
from signal import signal
from manim import *

HOME = "Icons/"

class ChiffrerVote(Scene):

    def construct(self):
        default_buff = 0.5
        
        bob = ImageMobject(f"{HOME}Men.png").scale(1).to_edge(LEFT, buff=default_buff)
	
        admin_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(UP, buff=1.5)
        decompte_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(RIGHT, buff=1)

        urne_img = ImageMobject(f"{HOME}PollingBox.png").scale(0.5).to_edge(DOWN, buff=1)


        enveloppe = ImageMobject(f"{HOME}LetterOpen.png").scale(0.3).next_to(bob.get_right(), RIGHT)

        signature = ImageMobject(f"{HOME}Signature.png").scale(0.3).next_to(enveloppe.get_right(), RIGHT)

        pack = ImageMobject(f"{HOME}Product-256.png").scale(0.5).next_to(enveloppe.get_right() - np.array([0, 1, 0]), DOWN)

        cadena_ouvert = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.3).next_to(pack.get_center() + np.array([0.5, 0.5, 0]), ORIGIN)

        cadena_ferme = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.3).next_to(cadena_ouvert.get_center(), ORIGIN)


		#text
        client = Tex("Bob").next_to(bob.get_top(), UP)
        amdin = Tex("Administrateur").next_to(admin_img.get_top(), UP)
        decompte = Tex("Décompte").next_to(decompte_img.get_top(), UP)
        urne = Tex("Urne").next_to(urne_img.get_top(), UP)

        self.play(FadeIn(bob), Write(client))

        self.play(FadeIn(admin_img), FadeIn(decompte_img), FadeIn(urne_img), Write(amdin), Write(urne), Write(decompte))

        self.play(FadeIn(enveloppe), FadeIn(signature))

        self.play(FadeIn(pack))

        self.play(enveloppe.animate.next_to(pack.get_center(), ORIGIN), signature.animate.next_to(pack.get_center(), ORIGIN))

        self.play(FadeOut(enveloppe), FadeOut(signature))

        self.play(FadeIn(cadena_ouvert))

        self.play(FadeOut(cadena_ouvert), FadeIn(cadena_ferme))

        self.play(pack.animate.next_to(urne_img.get_left(), LEFT), cadena_ferme.animate.next_to(urne_img.get_left() + np.array([0.3, 0.5, 0]), LEFT))

        self.wait(5)



