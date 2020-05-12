  class CoorPolygon(Scene):
      def construct(self):
          for x in range(-7, 8):
              for y in range(-4, 5):
                  self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
          polygon = Polygon(
              np.array([3, 2, 0]),
              np.array([1, -1, 0]),
              np.array([-5, -4, 0]),
              np.array([-4, 4, 0]))
          self.add(polygon)