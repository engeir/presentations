"""Module for creating a poster with `borb`."""

import os
from decimal import Decimal
from pathlib import Path
from typing import List, Optional, Tuple, Union

import borb.pdf as pdf
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText
from borb.pdf.canvas.layout.text.chunks_of_text import HeterogeneousParagraph
from borb.pdf.page.page_size import PageSize
from borb_poster import color_palette, custom_plots, shapes
from borb.pdf.canvas.layout.emoji.emoji import Emoji, Emojis


def create_qr_code(layout: PageLayout) -> None:
    """Create a QR code."""
    qr_code = pdf.Barcode(
        data="https://www.borbpdf.com",
        width=Decimal(64),
        height=Decimal(64),
        type=pdf.BarcodeType.QR,
    )
    layout.add(
        pdf.FlexibleColumnWidthTable(number_of_columns=2, number_of_rows=1)
        .add(qr_code)
        .add(
            pdf.Paragraph(
                """
                500 South Buena Vista Street
                Burbank CA
                91521-0991 USA
                """,
                padding_top=Decimal(12),
                respect_newlines_in_text=True,
                font_color=pdf.HexColor("#666666"),
                font_size=Decimal(10),
            )
        )
        .no_borders()
    )
    layout.add(
        pdf.Paragraph(
            "Eirik Rolland Enger",
            font_color=pdf.HexColor("#6d64e8"),
            font_size=Decimal(20),
        )
    )


def _footer(
    page: pdf.Page,
    bounding_box: Rectangle,
    header_height: Decimal,
    margin_y: Decimal,
    width: Decimal,
) -> None:
    pdf.FixedColumnWidthTable(
        number_of_rows=1,
        number_of_columns=4,
        column_widths=[Decimal(0.15), Decimal(0.28), Decimal(0.29), Decimal(0.28)],
    ).add(
        # pdf.TableCell(
        pdf.Paragraph(
            "References",
            font="Helvetica-Bold",
            font_color=pdf.HexColor(color_palette.MAIN_COLOR),
            font_size=Decimal(25),
            vertical_alignment=Alignment.MIDDLE,
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(50),
        ),
    ).add(
        pdf.OrderedList()
        .add(
            pdf.Paragraph(
                """Lucy, L. B. (1974), An iterative technique for the rectification of
                observed distributions."""
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
        .add(
            pdf.Paragraph(
                "Maecenas vitae dui ac nisi aliquam malesuada in consequat sapien."
            )
        )
        .add(
            pdf.Paragraph(
                "Nam aliquet ex eget felis lobortis aliquet sit amet ut risus."
            )
        )
        .add(
            pdf.Paragraph(
                "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
    ).add(
        pdf.OrderedList(start_index=7)
        .add(
            pdf.Paragraph(
                "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
        .add(
            pdf.Paragraph(
                "Maecenas vitae dui ac nisi aliquam malesuada in consequat sapien."
            )
        )
        .add(
            pdf.Paragraph(
                "Nam aliquet ex eget felis lobortis aliquet sit amet ut risus."
            )
        )
        .add(
            pdf.Paragraph(
                "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
    ).add(
        pdf.OrderedList(start_index=13)
        .add(
            pdf.Paragraph(
                "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
        .add(
            pdf.Paragraph(
                "Maecenas vitae dui ac nisi aliquam malesuada in consequat sapien."
            )
        )
        .add(
            pdf.Paragraph(
                "Nam aliquet ex eget felis lobortis aliquet sit amet ut risus."
            )
        )
        .add(
            pdf.Paragraph(
                "Maecenas sit amet odio ut erat tincidunt consectetur accumsan ut nunc."
            )
        )
        .add(pdf.Paragraph("Phasellus eget magna et justo malesuada fringilla."))
    ).no_borders().layout(
        page, bounding_box
    )

    shapes.footer_shapes(page, header_height, margin_y, width)


def _header(
    page: pdf.Page,
    bounding_box: Rectangle,
    header_height: Decimal,
    margin_x: Decimal,
    margin_y: Decimal,
    width: Decimal,
    height: Decimal,
) -> None:
    scale_img = 0.12
    img_w = Decimal(2724 * scale_img)
    img_h = Decimal(500 * scale_img)
    pdf.Heading(
        "A long and completely meaningless title, but it is nice for testing!",
        font="Helvetica-Bold",
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        font_size=Decimal(35),
        vertical_alignment=Alignment.TOP,
        horizontal_alignment=Alignment.CENTERED,
    ).layout(page, bounding_box)
    pdf.Heading(
        "Author One, Author Two, Author Three",
        font="Helvetica-Bold",
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        font_size=Decimal(25),
        vertical_alignment=Alignment.MIDDLE,
        horizontal_alignment=Alignment.CENTERED,
    ).layout(page, bounding_box)
    pdf.Heading(
        "Department of Physics and Technology",
        font="Helvetica",
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        font_size=Decimal(25),
        vertical_alignment=Alignment.BOTTOM,
        horizontal_alignment=Alignment.CENTERED,
        padding_bottom=Decimal(10),
    ).layout(page, bounding_box)

    pdf.Image(
        Path(os.path.join(os.getcwd(), "assets", "UiT_Logo_Eng_2l_Bla_RGB.png")),
        width=img_w,
        height=img_h,
    ).layout(
        page,
        Rectangle(
            width - img_w - margin_x,
            height - img_h - header_height + 2 * margin_y,
            img_w,
            img_h,
        ),
    )
    shapes.header_shapes(page, header_height + img_h, margin_y, width, height)


def create_header_footer(page: pdf.Page, header_height: Decimal) -> None:
    """Create a header and a footer."""
    margin_x = Decimal(20)
    margin_y = Decimal(20)
    width = PageSize.A2_PORTRAIT.value[0]
    height = PageSize.A2_PORTRAIT.value[1]
    # fmt: off
    r_top: Rectangle = Rectangle(
        margin_x,  # x: 0 + page_margin
        Decimal(height - margin_y - header_height),  # y: page_height - page_margin - height_of_textbox
        Decimal(width - margin_x * 2),  # width: page_width - 2 * page_margin
        header_height,  # height
    )
    r_bot: Rectangle = Rectangle(
        margin_x,  # x: 0 + page_margin
        margin_y,  # y: page_height - page_margin - height_of_textbox
        Decimal(width - margin_x * 2),  # width: page_width - 2 * page_margin
        header_height,  # height
    )
    # fmt: on

    # # this is a quick hack to easily get a rectangle on the page
    # # which can be very useful for debugging
    # page.append_annotation(
    #     SquareAnnotation(r_top, stroke_color=pdf.HexColor("#ff0000"))
    # )
    # page.append_annotation(
    #     SquareAnnotation(r_bot, stroke_color=pdf.HexColor("#ff0000"))
    # )

    # Header ========================================================================= #
    _header(page, r_top, header_height, margin_x, margin_y, width, height)

    # Footer ========================================================================= #
    _footer(page, r_bot, header_height, margin_y, width)


def _paragraph_heading(text: str) -> HeterogeneousParagraph:
    paragraph = HeterogeneousParagraph([])
    volc: Emoji = Emojis.VOLCANO.value
    volc.set_font_size(Decimal(30))
    paragraph.add(volc)
    paragraph.add(ChunkOfText("    "))
    paragraph.add(
        ChunkOfText(
            text,
            font="Helvetica-Bold-Oblique",
            font_size=Decimal(30),
            # background_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
            border_color=pdf.HexColor(color_palette.SUPPORTCOLOR["red"]),
            border_width=Decimal(1),
            border_bottom=True,
            padding_bottom=Decimal(3),
            # border_radius_bottom_left=Decimal(10),
        )
    )
    return paragraph


def _paragraph_box() -> HeterogeneousParagraph:
    return HeterogeneousParagraph(
        [],
        background_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
        # border_top=True,
        # border_right=True,
        # border_bottom=True,
        # border_left=True,
        border_radius_top_left=Decimal(8),
        border_radius_top_right=Decimal(8),
        border_radius_bottom_right=Decimal(8),
        border_radius_bottom_left=Decimal(8),
        border_color=pdf.HexColor(color_palette.SUPPORTCOLOR["red"]),
        border_width=Decimal(1),
        padding_bottom=Decimal(9),
        padding_top=Decimal(5),
        padding_right=Decimal(9),
        padding_left=Decimal(9),
    )


def _paragraph_text(
    text: str, paragraph: Optional[HeterogeneousParagraph] = None
) -> HeterogeneousParagraph:
    if paragraph is None:
        paragraph = _paragraph_box()

    for line in text.split():
        paragraph.add(ChunkOfText(line + " "))
    return paragraph


def _paragraph_text_chunks(
    text: List[Tuple[str, str, bool]],
    paragraph: Optional[HeterogeneousParagraph] = None,
) -> HeterogeneousParagraph:
    font_dict = {
        "bold": "Helvetica-Bold",
        "italic": "Helvetica-Oblique",
        "code": "Courier",
    }
    back_color_dict = {
        "bold": pdf.HexColor("#000000"),
        "italic": pdf.HexColor("#000000"),
        # "code": pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
        "code": pdf.HexColor("#555555"),
    }
    if paragraph is None:
        paragraph = _paragraph_box()
        # paragraph = HeterogeneousParagraph(
        #     [],
        #     background_color=pdf.HexColor(color_palette.SUPPORTCOLOR["light blue"]),
        #     # border_top=True,
        #     # border_right=True,
        #     # border_bottom=True,
        #     # border_left=True,
        #     border_radius_top_left=Decimal(8),
        #     border_radius_top_right=Decimal(8),
        #     border_radius_bottom_right=Decimal(8),
        #     border_radius_bottom_left=Decimal(8),
        #     border_color=pdf.HexColor("000000"),
        #     # border_width=Decimal(0.1),
        #     padding_bottom=Decimal(5),
        #     padding_top=Decimal(1),
        #     padding_right=Decimal(5),
        #     padding_left=Decimal(5),
        # )
    for parts in text:
        if parts[0] not in font_dict:
            font = "Helvetica"
            back_color = pdf.HexColor("000000")
        else:
            font = font_dict[parts[0]]
            back_color = back_color_dict[parts[0]]
        chunk = parts[1]
        for i, w in enumerate(chunk.split()):
            if not parts[2] and i == len(chunk.split()) - 1:
                paragraph.add(ChunkOfText(w, font=font, font_color=back_color))
            else:
                paragraph.add(ChunkOfText(w + " ", font=font, font_color=back_color))
    return paragraph


def _paragraph_qr_code(link: str) -> pdf.Barcode:
    """Create a QR code."""
    return pdf.Barcode(
        data=link,
        width=Decimal(64),
        height=Decimal(64),
        type=pdf.BarcodeType.QR,
        horizontal_alignment=Alignment.CENTERED,
        vertical_alignment=Alignment.MIDDLE,
    )


def _paragraph_image(
    layout: PageLayout, path: str, shape: tuple[int, int], local: bool = True
) -> pdf.Image:
    if local:
        pth = Path(path)
    else:
        pth = path
    width, height = shape
    cw = layout._column_width
    if width > cw:
        width = cw
        height = int(cw / shape[0] * shape[1])
    return pdf.Image(
        pth,
        width=Decimal(width),
        height=Decimal(height),
        # margin_bottom=Decimal(-10),
    )


def _paragraph_chart(layout: PageLayout, shape: tuple[int, int]) -> pdf.Image:
    # Max 337 width
    width, height = shape
    cw = layout._column_width
    if width > cw:
        width = cw
        height = int(cw / shape[0] * shape[1])
    return pdf.Chart(
        custom_plots.get_plt(),
        width=Decimal(width),
        height=Decimal(height),
    )


def create_paragraphs(layout: PageLayout) -> None:
    """Create the paragraphs in the poster."""
    # INTRODUCTION ------------------------------------------------------------------- #
    layout.add(_paragraph_heading("Introduction"))
    layout.add(
        _paragraph_text(
            """Want to run CESM2 with synthetic volcanic eruptions. Want to recreate the
            forcing file loaded by CESM2, but first need to generate raw synthetic forcing
            data that is used to create the full forcing file. Example: Volcanic eruptions
            from the last 150 years are included in CESM2 via a file which, if we omit
            location in space, has volcanoes as shown below."""
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "/home/een023/Documents/work/cesm/model-runs/e_BASELINE/synthetic/data/output/synthetic_volcanoes_20220421_1126.png",
            (1011, 624),
        )
    )

    # CREATING VOLCANOES ------------------------------------------------------------- #
    layout.add(_paragraph_heading("Creating Volcanoes"))
    _paragraph_qr_code("https://github.com/engeir/volcano-cooking").layout(
        layout.get_page(),
        Rectangle(
            layout._previous_element.bounding_box.x
            + layout._previous_element.bounding_box.width
            + Decimal(10),
            layout._previous_element.bounding_box.y - Decimal(7.5),
            Decimal(64),
            Decimal(64),
        ),
    )
    volc_box = _paragraph_box()
    # layout.add(
    _paragraph_text_chunks(
        [
            (
                "normal",
                "Strategy is to use the already present forcing file and write over it. This resulted in ",
                True,
            ),
            ("code", " volcano-cooking", False),
            (
                "normal",
                ", a python library for generating valid CESM2 volcanic forcing files.",
                True,
            ),
        ],
        volc_box,
    )
    _paragraph_text_chunks(
        [
            ("bold", "volcanoes.nc ", True),
            ("normal", "are so very ", True),
            ("code", "cool", False),
            ("normal", ".", True),
        ],
        volc_box,
    )
    _paragraph_text(
        """Want to run CESM2 with synthetic volcanic eruptions. Want to recreate the
        forcing file loaded by CESM2, but first need to generate raw synthetic forcing
        data that is used to create the full forcing file. Example: Volcanic eruptions
        from the last 150 years are included in CESM2 via a file which, if we omit
        location in space, has volcanoes as shown below.""",
        volc_box,
    )
    layout.add(volc_box)
    layout.add(
        _paragraph_image(
            layout,
            "/home/een023/Documents/presentations-files/2022/chess-am/assets/paired-percentiles.png",
            shape=(2022, 624),
            local=True,
        )
    )
    # layout.add(
    #     _paragraph_image(
    #         layout,
    #         "https://github.com/engeir/presentations-files/raw/ce8078c1f469e75ed910118e2cd3a222077b3983/2022/chess-am/assets/TREFHT-strong_percentiles.png",
    #         shape=(int(1011 / 5), int(624 / 5)),
    #         local=False,
    #     )
    # )

    # FUTURE ------------------------------------------------------------------------- #
    layout.add(_paragraph_heading("Future work and use cases"))
    layout.add(
        _paragraph_text(
            """We can use this to look at how forcing at specific locations affect the
        global climate, as well as how a given region and neighbouring regions is
        affected. One particularly interesting region may be the arctic; we could then
        place a big eruption in Greenland and observe how the climate changes from
        there.
        """
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "https://github.com/engeir/presentations-files/raw/f71580dcb981c2e827b7f9bde3978390fe60840f/2022/chess-am/assets/AEROD_v20220404-composite.png",
            shape=(1191, 754),
            local=False,
        )
    )
    _paragraph_qr_code(
        "https://github.com/engeir/presentations-files/raw/14d24ee6343b4b80be8476eb9e2b76bbfadd8dc5/2022/chess-am/assets/AEROD_v20220404.mp4"
    ).layout(
        layout.get_page(),
        Rectangle(
            layout._previous_element.bounding_box.x
            # + layout._previous_element.bounding_box.width
            + Decimal(10),
            layout._previous_element.bounding_box.y + Decimal(65),
            Decimal(64),
            Decimal(64),
        ),
    )


def custom_layout(
    page: pdf.Page, header_height: Decimal, number_of_columns: int
) -> PageLayout:
    """Create a MultiColumnLayout with adjusted init method."""
    # Create the main layout
    layout = pdf.MultiColumnLayout(
        page,
        number_of_columns=number_of_columns,
        vertical_margin=header_height + Decimal(50),
        horizontal_margin=Decimal(30),
        fixed_paragraph_spacing=Decimal(15),
    )
    # Re-setting the column widths that are defined in the `__init__` method.
    # inter-column margin
    layout._inter_column_margin = Decimal(15)  # layout._page_width * Decimal(0.02)
    layout._number_of_columns = Decimal(number_of_columns)
    layout._column_width = (
        layout._page_width
        - Decimal(2) * layout._horizontal_margin
        - Decimal(number_of_columns - 1) * layout._inter_column_margin
    ) / Decimal(number_of_columns)
    return layout


def create_poster() -> None:
    """Create a poster with `borb`."""
    doc = pdf.Document()
    width = PageSize.A2_PORTRAIT.value[0]
    height = PageSize.A2_PORTRAIT.value[1]
    header_height = Decimal(150)
    page = pdf.Page(
        width=width,
        height=height,
    )
    doc.append_page(page)
    create_header_footer(page, header_height)

    layout = custom_layout(page, header_height, 2)
    create_paragraphs(layout)

    with open("poster.pdf", "wb") as pdf_file_handle:
        pdf.PDF.dumps(pdf_file_handle, doc)
