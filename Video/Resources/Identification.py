from fnmatch import fnmatch
from manim import *

HOME = "Icons/"

class Identification(Scene):

	def construct(self):
		default_buff = 0.5
        
		bob = ImageMobject(f"{HOME}Men.png").scale(1).to_edge(LEFT, buff=default_buff)
	


		admin_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(UP, buff=1.5)
		decompte_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(RIGHT, buff=1)

		urne_img = ImageMobject(f"{HOME}PollingBox.png").scale(0.5).to_edge(DOWN, buff=1)

		finger_print = ImageMobject(f"{HOME}Finger-Print.png").scale(0.3).next_to(bob, DOWN)

		#text
		client = Tex("Bob").next_to(bob.get_top(), UP)
		amdin = Tex("Administrateur").next_to(admin_img.get_top(), UP)
		decompte = Tex("Décompte").next_to(decompte_img.get_top(), UP)
		urne = Tex("Urne").next_to(urne_img.get_top(), UP)


		self.play(FadeIn(bob), Write(client))

		self.play(FadeIn(admin_img), FadeIn(decompte_img), FadeIn(urne_img), Write(amdin), Write(urne), Write(decompte))

		self.play(FadeIn(finger_print))
		self.play(finger_print.animate.next_to(admin_img.get_bottom(), DOWN), run_time=3)

		self.wait(5)