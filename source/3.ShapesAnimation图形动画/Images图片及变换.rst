Images图片及变换
===================

Image图片及变换

.. code-block:: python
   :linenos:

   from manimlib.imports import *
    #png/jpg,manim版PPT
    class Images(Scene):
        def construct(self):
            img = ImageMobject(r'C:\files\2-2.png')#绝对路径
            img.scale(3)  # Resize to be twice as big
            img.shift(3*LEFT)  # Move the image
    
            self.play(ShowCreation(img))  # Display the image


.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/svg_Images/Images1.mp4" type="video/mp4">
   </video>



.. code:: 

    class Images(Scene):
        def construct(self):
            img = r'manimlib\\files\\2-2.png'#相对路径
            imMob = ImageMobject(img)  # Makes an image mobject of existing image
    
            imMob.scale(3)
            imMob.shift(3 * LEFT)
    
            self.play(ShowCreation(imMob))



.. raw:: html

   <video width="560" height="315" controls>
       <source src="../_static/svg_Images/Images2.mp4" type="video/mp4">
   </video>

