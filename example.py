from manimlib.imports import *

class ShowIncreasingSubsetsExample(Scene):
    def construct(self):
        text = TextMobject("ShowIncreasingSubsets")
        text.set_width(11)
        self.wait()
        self.play(ShowIncreasingSubsets(text[0], run_time=4))
        self.wait()


class ShowSubmobjectsOneByOneExample(Scene):
    def construct(self):
        text = TextMobject("ShowSubmobjectsOneByOne")
        text.set_width(11)
        self.wait()
        self.play(ShowSubmobjectsOneByOne(text[0], run_time=4))
        self.wait()


class FadeInFromPointExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.wait()
        self.play(
            *[FadeInFromPoint(mob, UP*3) for mob in mobjects]
        )
        self.wait()


class ChangingDecimalExample(Scene):
    def construct(self):
        number = DecimalNumber(0).scale(2)
        def update_func(t):
            return t * 10
        self.add(number)
        self.wait()
        self.play(ChangingDecimal(number, update_func), run_time=3)
        self.wait()


class ChangeDecimalToValueExample(Scene):
    def construct(self):
        number = DecimalNumber(0).scale(2)
        self.add(number)
        self.wait()
        self.play(ChangeDecimalToValue(number, 20), run_time=3)
        self.wait()


class UpdateFromFuncExample(Scene):
    def construct(self):
        square = Square().to_edge(UP)
        mobject = TextMobject("Text").scale(2).next_to(square, RIGHT)
        def update_func(mob):
            mob.next_to(square, RIGHT)

        self.add(square, mobject)
        self.wait()
        self.play(
            square.to_edge, DOWN,
            UpdateFromFunc(mobject, update_func)
        )
        self.wait()
    

class UpdateFromAlphaFuncExample(Scene):
    def construct(self):
        square = Square().to_edge(UP)
        mobject = TextMobject("Text").scale(2)
        mobject.next_to(square, RIGHT, buff=0.05)
        def update_func(mob, alpha):
            mob.next_to(square, RIGHT, buff=0.05 + alpha)

        self.add(square, mobject)
        self.wait()
        self.play(
            square.to_edge, DOWN,
            UpdateFromAlphaFunc(mobject, update_func)
        )
        self.wait()


class MaintainPositionRelativeToExample(Scene):
    def construct(self):
        square = Square().to_edge(UP)
        mobject = TextMobject("Text").scale(2)
        mobject.next_to(square, RIGHT)

        self.add(square, mobject)
        self.wait()
        self.play(
            square.to_edge, DOWN,
            MaintainPositionRelativeTo(mobject, square)
        )
        self.wait()
        

class AnimationGroupExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.wait()
        anims = AnimationGroup(
            *[GrowFromCenter(mob) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class SuccessionExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.wait()
        anims = Succession(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class LaggedStartExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.wait()
        anims = LaggedStart(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        self.play(anims)
        self.wait()


class LaggedStartMapExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.wait()
        anims = LaggedStartMap(
            FadeOut, mobjects
        )
        self.play(anims)
        self.wait()


class TransformExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3)
        C = TextMobject("C-Text").scale(3)

        self.add(A)
        self.wait()
        self.play(Transform(A, B))
        self.wait()
        self.play(Transform(A, C)) # notice here
        self.wait()


class ReplacementTransformExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3)
        C = TextMobject("C-Text").scale(3)

        self.add(A)
        self.wait()
        self.play(ReplacementTransform(A, B))
        self.wait()
        self.play(ReplacementTransform(B, C)) # notice here
        self.wait()


class TransformFromCopyExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(TransformFromCopy(A, B))
        self.wait()


class ClockwiseTransformExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(ClockwiseTransform(A, B))
        self.wait()


class CounterclockwiseTransformExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3).shift(UP*2)

        self.add(A)
        self.wait()
        self.play(CounterclockwiseTransform(A, B))
        self.wait()


class MoveToTargetExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.scale(3).shift(RIGHT*7+UP*2) # 操作A的target

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class SelfPlayExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)

        self.add(A)
        self.wait()
        self.play(
            A.scale, 3,
            A.shift, RIGHT*7+UP*2,
        )
        self.wait()


class ApplyMethodExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)

        self.add(A)
        self.wait()
        self.play(
            ApplyMethod(A.scale, 3), # 这个不会执行
            ApplyMethod(A.shift, RIGHT*7+UP*2),
        )
        self.wait()


class RestoreExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.save_state()  # 记录下现在状态，restore会回到此时
        A.scale(3).shift(RIGHT*7+UP*2)

        self.add(A)
        self.wait()
        self.play(Restore(A))
        self.wait()


class ApplyFunctionExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        def function(mob):
            return mob.scale(3).shift(RIGHT*7+UP*2)
            # 需要return一个mobject

        self.add(A)
        self.wait()
        self.play(ApplyFunction(function, A))
        self.wait()


class ApplyMatrixExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(2)
        mat = np.array([
            [1, 3, 1],
            [0.5, 1, 1],
            [1, 1, 1]
        ])

        self.add(A)
        self.wait()
        self.play(ApplyMatrix(mat, A))
        self.wait()


class CyclicReplaceExample(Scene):
    def construct(self):
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3)
        VGroup(A, B).arrange(RIGHT)

        self.add(A, B)
        self.wait()
        self.play(CyclicReplace(A, B)) # 或Swap(A, B)
        self.wait()
