"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jonah Yates.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():

    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow()
    c1 = rg.Point(75, 75)
    c2 = rg.Point(225, 200)

    f1 = rg.Circle(c1, 60)
    f2 = rg.Circle(c2, 100)

    f2.fill_color = "MistyRose"

    f1.attach_to(window)
    f2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window = rg.RoseWindow()

    center = rg.Point(35, 35)
    sph = rg.Circle(center, 25)
    sph.fill_color = 'blue'
    sph.attach_to(window)

    tlc = rg.Point(100, 100)
    brc = rg.Point(250, 200)
    rect = rg.Rectangle(tlc, brc)
    rect.attach_to(window)

    print('Outline Thickness:', sph.outline_thickness)
    print('Fill Color:', sph.fill_color)
    print('Center:', sph.center)
    print('Center X Value:', center.x)
    print('Center Y Value:', center.y)

    print('Outline Thickness:', rect.outline_thickness)
    print('Fill Color:', rect.fill_color)
    print('Center: (', (tlc.x+brc.x)/2, ',', (tlc.y+brc.y)/2, ')' )
    print('Center X Value:', (tlc.x+brc.x)/2)
    print('Center Y Value:', (tlc.y+brc.y)/2)

    window.render()

    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow()

    p1 = rg.Point(5, 10)
    p2 = rg.Point(25, 100)
    p3 = rg.Point(100,40)
    p4 = rg.Point(150,2)



    l1 = rg.Line(p1, p2)
    l2 = rg.Line(p3, p4)

    l1.attach_to(window)
    l2.attach_to(window)

    l2.thickness = 7

    print(l2.get_midpoint())
    l2mid = l2.get_midpoint()
    print(l2mid.x)
    print(l2mid.y)

    window.render()

    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
