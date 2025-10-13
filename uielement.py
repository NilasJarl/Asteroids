import pygame


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Ariel", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(pygame.sprite.Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.mouse_over = False  # indicates if the mouse is over the element
        self._center_position = center_position
        self._text = text
        self._font_size = font_size
        self._bg_rgb = bg_rgb
        self._text_rgb = text_rgb
        self.action = action
        self._build_images()
        super().__init__()
    def _build_images(self):
        # create the default image
        default_image = create_surface_with_text(
            text=self._text, font_size=self._font_size, text_rgb=self._text_rgb, bg_rgb=self._bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=self._text, font_size=self._font_size * 1.2, text_rgb=self._text_rgb, bg_rgb=self._bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=self._center_position),
            highlighted_image.get_rect(center=self._center_position),
        ]

    def set_text_color(self, color):
        self._text_rgb = color
        self._build_images()
        

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over and self.action is not None else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over and self.action is not None else self.rects[0]
        
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)