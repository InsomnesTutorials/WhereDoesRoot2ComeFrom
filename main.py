from manim import *

class Part1(Scene):
    def construct(self):
        text_sqrt = MathTex("\sqrt{2}")
        text_question = MathTex("?")
        title = Text("Where does root \n  2 come from?", font_size=36).to_edge(UP).shift(0.3*DOWN).set_color_by_gradient(RED, GREEN)
        
        self.play(Write(title), run_time =0.001) 
        self.play(Write(text_sqrt)) # 1s
        self.wait(1) # 2s
        
        self.play(Transform(text_sqrt, text_question)) # 3s
        self.wait(1.2) # 4.2s 
        
        triangle = Polygon(LEFT+UP, LEFT+DOWN, RIGHT+DOWN)
        side_a_label = MathTex("1").next_to(triangle, LEFT, buff=0.1)
        side_b_label = MathTex("1").next_to(triangle, DOWN, buff=0.1)
        side_c_label = MathTex("?").next_to(triangle.get_center(), RIGHT+UP, buff=0.1)
        
        
        self.play(FadeOut(text_sqrt), run_time=0.001)
        self.play(FadeOut(title),Create(triangle), Transform(text_question, side_c_label)) # 5.2s
        self.play(Write(side_a_label), Write(side_b_label), run_time=0.8) # 6s
        self.wait(1.2) # 7.2s
        
        pyth = MathTex("? = \sqrt{1^2 + 1^2}")
        pyth.shift(UP * 2)
        self.play(Write(pyth)) # 8.2
        self.wait(0.8) # 9s
        text_sqrt = MathTex("\sqrt{2}").next_to(triangle.get_center(), RIGHT+UP, buff=0.1)
        self.play(Transform(pyth, text_sqrt), FadeOut(text_question)) #10s
        self.wait(2) #12s
        
        p_over_q = MathTex("\\frac{p}{q}").move_to(ORIGIN)
        description = Tex("where p,q $\in \mathbb{Z}$", font_size=28).next_to(p_over_q, DOWN)
        
        all_objects = VGroup(pyth, triangle, text_sqrt, side_a_label, side_b_label)
        self.play(Transform(all_objects, p_over_q)) #13s
        self.wait(1) # 14s
        self.play(Write(description)) # 15s
        self.wait(1) # 16s
        
        p_over_q_group = VGroup(all_objects, description) 
        
        self.wait(3) # 19s
        
        self.play(FadeOut(p_over_q_group)) # 20s
        
        
class Part2(Scene):
    def construct(self):
        rectangle = Rectangle(height=2.8, width=2, color=WHITE)
        rectangle.move_to(ORIGIN)

        top_brace = Brace(rectangle, UP)
        right_brace = Brace(rectangle, RIGHT)

        top_label = MathTex("b").next_to(top_brace, UP)
        right_label = MathTex("a").next_to(right_brace, RIGHT)

        self.play(Create(rectangle)) #1s
        self.play(GrowFromCenter(top_brace), Write(top_label))
        self.play(GrowFromCenter(right_brace), Write(right_label)) #3s

        self.wait(2) #5s
        
        ratio_one = MathTex("\\frac{a}{b}").to_edge(UP).shift(LEFT + 0.1*DOWN)
        
        self.play(Indicate(right_label), run_time=0.7) # 6s
        self.play(Indicate(top_label), run_time=0.7) # 7s
        self.play(Write(ratio_one),run_time=0.9) #8s
        
        half_rectangle = Rectangle(height=1.4,width=2)
        half_rectangle.move_to(ORIGIN)
        
        half_top_brace = Brace(half_rectangle, UP)
        half_right_brace = Brace(half_rectangle, RIGHT)
        
        half_top_label = MathTex("b").next_to(half_top_brace, UP)
        half_right_label = MathTex("\\frac{a}{2}").next_to(half_right_brace, RIGHT)
        
        self.play(Transform(rectangle, half_rectangle), Transform(top_brace, half_top_brace), Transform(top_label, half_top_label), Transform(right_brace, half_right_brace), Transform(right_label,half_right_label)) #8s
        
        ratio_two = MathTex("\\frac{b}{\\frac{a}{2}}").to_edge(UP).shift(RIGHT + 0.1*DOWN)
        
        self.play(Indicate(half_top_label)) #9s
        self.play(Indicate(half_right_label)) #10s
        self.play(Write(ratio_two)) #11s
        
        self.wait(2) # 14s
        
        ratio_equal = MathTex("=").to_edge(UP).shift(0.5*DOWN)
        self.play(Write(ratio_equal)) # 15s
        self.wait(2) # 17s
        
        equation_terms = VGroup(ratio_one, ratio_two, ratio_equal)
        eliminate_remaining_mobjects = VGroup(rectangle, top_brace, top_label, half_top_label, right_brace, half_right_label, right_label)
         
        equation = MathTex("\\frac{a}{b}=\\frac{2b}{a}").move_to(ORIGIN)
        equation_one = MathTex("\\frac{a^2}{b^2}=2")
        equation_two = MathTex("(\\frac{a}{b})^2=2")
        equation_final = MathTex("\\frac{a}{b}=\sqrt{2}")
        
        self.play(Transform(equation_terms, equation), Write(equation), FadeOut(eliminate_remaining_mobjects))
        self.wait(0.5)
        self.play(FadeOut(equation_terms))
        self.play(Transform(equation, equation_one))
        self.wait(0.5)
        self.play(Transform(equation, equation_two))
        self.wait(0.5)
        self.play(Transform(equation, equation_final))

        self.wait(3) 
        
        