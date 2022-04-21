"""Create shapes that separate out header and footer from the body."""

from decimal import Decimal

import borb.pdf as pdf
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
from borb_poster import color_palette


def header_shapes(
    page: pdf.Page,
    header_height: Decimal,
    margin_y: Decimal,
    width: Decimal,
    height: Decimal,
) -> None:
    """Create shapes for the header.

    Parameters
    ----------
    page : pdf.Page
        The page to draw on.
    header_height : Decimal
        The height of the header.
    margin_y : Decimal
        The margin at the top of the page.
    width : Decimal
        The total width of the page.
    height : Decimal
        The total height of the page.
    """
    square_side = Decimal(40)
    shape_vertical_alignment = height - header_height + margin_y + 8
    # Square (from bottom left, clockwise)
    pdf.Shape(
        points=[
            (Decimal(0), shape_vertical_alignment),
            (Decimal(0), shape_vertical_alignment + square_side),
            (square_side, shape_vertical_alignment + square_side),
            (square_side, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
    ).layout(
        page,
        Rectangle(Decimal(0), shape_vertical_alignment, square_side, square_side),
    )
    # Square
    pdf.Shape(
        points=[
            (square_side, shape_vertical_alignment),
            (square_side, shape_vertical_alignment + square_side),
            (2 * square_side, shape_vertical_alignment + square_side),
            (2 * square_side, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
    ).layout(
        page,
        Rectangle(square_side, shape_vertical_alignment, square_side, square_side),
    )
    # Triangle
    pdf.Shape(
        points=[
            (2 * square_side, shape_vertical_alignment),
            (2 * square_side, shape_vertical_alignment + square_side),
            (3 * square_side, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
    ).layout(
        page,
        Rectangle(2 * square_side, shape_vertical_alignment, square_side, square_side),
    )
    # Line
    r: Rectangle = Rectangle(
        Decimal(0),
        shape_vertical_alignment - 8,
        width,
        Decimal(8),
    )
    pdf.Shape(
        points=LineArtFactory.rectangle(r),
        stroke_color=pdf.HexColor(color_palette.MAIN_COLOR),
        fill_color=pdf.HexColor(color_palette.MAIN_COLOR),
    ).layout(page, r)


def footer_shapes(
    page: pdf.Page, header_height: Decimal, margin_y: Decimal, width: Decimal
) -> None:
    """Create shapes for the footer.

    Parameters
    ----------
    page : pdf.Page
        The page to draw on.
    header_height : Decimal
        The height of the header.
    margin_y : Decimal
        The margin at the top of the page.
    width : Decimal
        The total width of the page.
    """
    # Shapes
    square_side = Decimal(40)
    shape_vertical_alignment = 2 * margin_y + header_height
    # Square (from bottom left, clockwise)
    pdf.Shape(
        points=[
            (width - square_side, shape_vertical_alignment),
            (width - square_side, shape_vertical_alignment + square_side),
            (width, shape_vertical_alignment + square_side),
            (width, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
    ).layout(
        page,
        Rectangle(
            width - square_side, shape_vertical_alignment, square_side, square_side
        ),
    )
    # Square
    pdf.Shape(
        points=[
            (width - 2 * square_side, shape_vertical_alignment),
            (width - 2 * square_side, shape_vertical_alignment + square_side),
            (width - square_side, shape_vertical_alignment + square_side),
            (width - square_side, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
    ).layout(
        page,
        Rectangle(
            width - 2 * square_side, shape_vertical_alignment, square_side, square_side
        ),
    )
    # Triangle
    pdf.Shape(
        points=[
            (width - 3 * square_side, shape_vertical_alignment),
            (width - 2 * square_side, shape_vertical_alignment + square_side),
            (width - 2 * square_side, shape_vertical_alignment),
        ],
        stroke_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
        fill_color=pdf.HexColor(color_palette.SUPPORTCOLOR["blue"]),
    ).layout(
        page,
        Rectangle(
            width - 3 * square_side, shape_vertical_alignment, square_side, square_side
        ),
    )
    # Line
    r: Rectangle = Rectangle(
        Decimal(0), shape_vertical_alignment - 8, width, Decimal(8)
    )
    pdf.Shape(
        points=LineArtFactory.rectangle(r),
        stroke_color=pdf.HexColor(color_palette.MAIN_COLOR),
        fill_color=pdf.HexColor(color_palette.MAIN_COLOR),
    ).layout(page, r)
