from fnmatch import fnmatch
from signal import signal
from tkinter import Pack
from manim import *

HOME = "Icons/"

class ChiffrerVote(Scene):

    def construct(self):
        default_buff = 0.5
        
        bob_img = ImageMobject(f"{HOME}Men.png").scale(0.7).to_edge(LEFT, buff=default_buff)
	
        admin_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(UP, buff=1.5)
        decompte_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(RIGHT, buff=1)

        urne_img = ImageMobject(f"{HOME}PollingBox.png").scale(0.5).to_edge(DOWN, buff=1)


        enveloppe = ImageMobject(f"{HOME}LetterOpen.png").scale(0.3).next_to(bob_img.get_right(), RIGHT)

        vote_bob = Tex("a").next_to(enveloppe.get_center(), ORIGIN)

        signature = ImageMobject(f"{HOME}Signature.png").scale(0.3).next_to(enveloppe.get_right(), RIGHT)

        pack_1 = ImageMobject(f"{HOME}Product-256.png").scale(0.5).next_to(enveloppe.get_right() - np.array([0, 0.5, 0]), DOWN)

        cadena_ouvert_1 = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.3).next_to(pack_1.get_center() + np.array([0.5, 0.5, 0]), ORIGIN)

        cadena_ferme_1 = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.3).next_to(cadena_ouvert_1.get_center(), ORIGIN)

        pack_2 = ImageMobject(f"{HOME}Product-256.png").scale(0.5).next_to(pack_1.get_top(), UP)


		#text
        client_bob = Tex("Bob").next_to(bob_img.get_top(), UP)
        amdin = Tex("Administrateur").next_to(admin_img.get_top(), UP)
        decompte = Tex("Décompte").next_to(decompte_img.get_top(), UP)
        urne = Tex("Urne").next_to(urne_img.get_top(), UP)

        self.play(FadeIn(bob_img), Write(client_bob))

        self.play(FadeIn(admin_img), FadeIn(decompte_img), FadeIn(urne_img), Write(amdin), Write(urne), Write(decompte))

        self.play(FadeIn(enveloppe), Write(vote_bob), FadeIn(signature))

        self.play(FadeIn(pack_1))

        self.play(enveloppe.animate.next_to(pack_1.get_center(), ORIGIN), vote_bob.animate.next_to(pack_1.get_center(), ORIGIN), signature.animate.next_to(pack_1.get_center(), ORIGIN))

        self.play(FadeOut(enveloppe), FadeOut(vote_bob), FadeOut(signature))

        self.play(FadeIn(cadena_ouvert_1))

        self.play(FadeOut(cadena_ouvert_1), FadeIn(cadena_ferme_1))

        self.play(pack_1.animate.next_to(urne_img.get_left(), LEFT), cadena_ferme_1.animate.next_to(urne_img.get_left() + np.array([0.3, 0.5, 0]), LEFT))

        pack_2 = ImageMobject(f"{HOME}Product-256.png").scale(0.3).next_to(pack_1.get_top(), UP)

        cadena_ferme_2 = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.2).next_to(pack_2.get_center() + np.array([0.2, 0.2, 0]), ORIGIN)

        client_img = ImageMobject(f"{HOME}Woman.png").scale(0.5).next_to(client_bob.get_top(), UP)

        pack_3 = ImageMobject(f"{HOME}Product-256.png").scale(0.3).next_to(pack_1.get_bottom(), DOWN)

        cadena_ferme_3 = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.2).next_to(pack_3.get_center() + np.array([0.2, 0.2, 0]), ORIGIN)
                
        client_img_2 = ImageMobject(f"{HOME}Men.png").scale(0.5).next_to(bob_img.get_bottom(), DOWN)

        self.play(FadeIn(pack_2), FadeIn(pack_3), FadeIn(cadena_ferme_2), FadeIn(cadena_ferme_3), FadeIn(client_img), FadeIn(client_img_2))

        self.wait(2)

        pack_de_packs = ImageMobject(f"{HOME}Product-256.png").scale(0.7).next_to(urne.get_top(), UP)
        cadena_ferme_de_packs = ImageMobject(f"{HOME}LockClosedRed.png").scale(0.4).next_to(pack_de_packs.get_center() + np.array([0.5, 0.5, 0]), ORIGIN)

        self.play(FadeIn(pack_de_packs), FadeIn(cadena_ferme_de_packs))

        self.play(pack_1.animate.next_to(pack_de_packs.get_center(), ORIGIN), pack_2.animate.next_to(pack_de_packs.get_center(), ORIGIN), pack_3.animate.next_to(pack_de_packs.get_center(), ORIGIN), cadena_ferme_1.animate.next_to(pack_de_packs.get_center(), ORIGIN), cadena_ferme_2.animate.next_to(pack_de_packs.get_center(), ORIGIN), cadena_ferme_3.animate.next_to(pack_de_packs.get_center(), ORIGIN))

        self.play(FadeOut(pack_1), FadeOut(pack_2), FadeOut(pack_3), FadeOut(cadena_ferme_1), FadeOut(cadena_ferme_2), FadeOut(cadena_ferme_3))

        self.play(pack_de_packs.animate.next_to(decompte_img.get_left() - np.array([2.5, 0, 0]), LEFT), cadena_ferme_de_packs.animate.next_to(decompte_img.get_left() - np.array([2.3, -0.5, 0]), LEFT))

        pack_1.next_to(pack_de_packs.get_center(), ORIGIN)

        cadena_ferme_1.next_to(pack_de_packs.get_center() + np.array([0.5, 0.5, 0]), ORIGIN)

        pack_2.next_to(pack_de_packs.get_center(), ORIGIN)

        cadena_ferme_2.next_to(pack_de_packs.get_center() + np.array([0.2, 0.2, 0]), ORIGIN)

        pack_3.next_to(pack_de_packs.get_center(), ORIGIN)

        cadena_ferme_3.next_to(pack_de_packs.get_center() + np.array([0.2, 0.2, 0]), ORIGIN)

        self.play(FadeIn(pack_1), FadeIn(pack_2), FadeIn(pack_3), FadeIn(cadena_ferme_1), FadeIn(cadena_ferme_2), FadeIn(cadena_ferme_3))

        self.play(pack_1.animate.next_to(decompte_img.get_left() - np.array([0.5, 0, 0]), LEFT), pack_2.animate.next_to(decompte_img.get_left() - np.array([0.7, -0.5, 0]), UL), pack_3.animate.next_to(decompte_img.get_left() - np.array([0.7, 0.5, 0]), DL), cadena_ferme_1.animate.next_to(decompte_img.get_left() - np.array([0.3, -0.5, 0]), LEFT), cadena_ferme_2.animate.next_to(decompte_img.get_left() - np.array([0.5, -0.9, 0]), UL), cadena_ferme_3.animate.next_to(decompte_img.get_left() - np.array([0.5, 0.3, 0]), DL))

        self.play(FadeOut(pack_de_packs), FadeOut(cadena_ferme_de_packs))
        
        pos_init_clef = decompte_img.get_center()   
        clef = ImageMobject(f"{HOME}KeyWhite.png").scale(0.2).next_to(pos_init_clef, ORIGIN)

        cadena_ouvert_2 = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.3).next_to(cadena_ferme_1.get_center(), ORIGIN)
        cadena_ouvert_3 = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.2).next_to(cadena_ferme_2.get_center(), ORIGIN)
        cadena_ouvert_4 = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.2).next_to(cadena_ferme_3.get_center(), ORIGIN)
 
        self.play(FadeIn(clef))

        self.play(clef.animate.next_to(cadena_ferme_2.get_right(), ORIGIN))

        self.play(FadeOut(cadena_ferme_2), FadeIn(cadena_ouvert_3))

        self.play(clef.animate.next_to(pos_init_clef, ORIGIN))

        self.play(clef.animate.next_to(cadena_ferme_1.get_right(), ORIGIN))

        self.play(FadeOut(cadena_ferme_1), FadeIn(cadena_ouvert_2))

        self.play(clef.animate.next_to(pos_init_clef, ORIGIN))

        self.play(clef.animate.next_to(cadena_ferme_3.get_right(), ORIGIN))

        self.play(FadeOut(cadena_ferme_3), FadeIn(cadena_ouvert_4))

        self.play(clef.animate.next_to(pos_init_clef, ORIGIN))

        self.play(FadeOut(clef))

        self.wait(2)

        resultats = ImageMobject(f"{HOME}List.png").scale(0.5).next_to(decompte_img.get_left() - np.array([0.5,-1, 0]), LEFT)

        vote_a = Tex("$( 2 \\times \\ Option \\ a )$").scale(0.7).next_to(resultats.get_bottom(), DOWN)

        vote_b = Tex("$( 1 \\times \\ Option \\ b )$").scale(0.7).next_to(vote_a.get_bottom(), DOWN)

        self.play(FadeOut(pack_1), FadeOut(pack_2), FadeOut(pack_3), FadeOut(cadena_ouvert_2), FadeOut(cadena_ouvert_3), FadeOut(cadena_ouvert_4), FadeIn(resultats), FadeIn(vote_a), FadeIn(vote_b))

        self.wait(2)