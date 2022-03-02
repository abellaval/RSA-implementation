from manim import *

HOME = "Icons/"

class VoteRSA(Scene):

	def construct(self):
		default_buff = 0.5
		client_img1 = ImageMobject(f"{HOME}Men.png").scale(0.5).to_edge(LEFT, buff=default_buff)
		client_img2 = ImageMobject(f"{HOME}Men.png").scale(0.5).next_to(client_img1.get_top(), UP)
		client_img3 = ImageMobject(f"{HOME}Men.png").scale(0.5).next_to(client_img2.get_top(), UP)
		client_img4 = ImageMobject(f"{HOME}Men.png").scale(0.5).next_to(client_img1.get_bottom(), DOWN)
		client_img5 = ImageMobject(f"{HOME}Men.png").scale(0.5).next_to(client_img4.get_bottom(), DOWN)


		admin_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(UP, buff=1.5)
		decompte_img = ImageMobject(f"{HOME}Server.png").scale(0.5).to_edge(RIGHT, buff=1)

		urne_img = ImageMobject(f"{HOME}PollingBox.png").scale(0.5).to_edge(DOWN, buff=1)

		#text
		client = Tex("Votants").next_to(client_img3.get_top(), UP)
		amdin = Tex("Administrateur").next_to(admin_img.get_top(), UP)
		decompte = Tex("Décompte").next_to(decompte_img.get_top(), UP)
		urne = Tex("Urne").next_to(urne_img.get_top(), UP)

		key = ImageMobject(f"{HOME}KeyWhite.png").scale(0.3).next_to(decompte_img.get_bottom(), DOWN)
		lock_open = ImageMobject(f"{HOME}LockOpenWhite.png").scale(0.3).next_to(decompte_img.get_bottom(), DOWN)

		self.play(FadeIn(admin_img), FadeIn(decompte_img), FadeIn(urne_img), Write(amdin), Write(urne), Write(decompte))

		self.play(FadeIn(client_img1), FadeIn(client_img2), FadeIn(client_img3), FadeIn(client_img4), FadeIn(client_img5), Write(client))
		self.play(key.animate.next_to(admin_img.get_bottom(), DOWN), run_time=3)
		self.play(lock_open.animate.next_to(admin_img.get_bottom(), DOWN), run_time=3)