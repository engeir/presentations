"""Module for creating a poster with `borb`."""

import os
import subprocess
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
        column_widths=[Decimal(0.12), Decimal(0.34), Decimal(0.33), Decimal(0.21)],
    ).add(
        # pdf.TableCell(
        pdf.Paragraph(
            "References",
            font="Helvetica-Bold",
            font_color=pdf.HexColor(color_palette.MAIN_COLOR),
            font_size=Decimal(25),
            vertical_alignment=Alignment.MIDDLE,
            horizontal_alignment=Alignment.LEFT,
            padding_bottom=Decimal(50),
        ),
    ).add(
        pdf.OrderedList()
        .add(
            pdf.Paragraph(
                """Bender, F. AM., Ekman, A. M. L., et al. (2010), Response to the
                eruption of Mount Pinatubo in relation to climate sensitivity in the
                CMIP3 models."""
            )
        )
        .add(
            pdf.Paragraph(
                """Boer, G. J., Stowasser, M., et al. (2007), Inferring
                climate sensitivity from volcanic events."""
            )
        )
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
        pdf.Paragraph(
            "View digital version!",
            font="Helvetica-Oblique",
            font_size=Decimal(20),
            font_color=pdf.HexColor(color_palette.SUPPORTCOLOR["yellow"]),
            horizontal_alignment=Alignment.RIGHT,
        )
    ).no_borders().layout(
        page, bounding_box
    )
    pdf.Barcode(
        data="https://github.com/engeir/presentations-files/raw/249364d90e7a42ccc690448bf408cc85d60708f4/2021/fysikermotet/beamer_fysikermotet.pdf",
        width=Decimal(128),
        height=Decimal(128),
        type=pdf.BarcodeType.QR,
        horizontal_alignment=Alignment.RIGHT,
        vertical_alignment=Alignment.BOTTOM,
    ).layout(
        page,
        Rectangle(
            bounding_box.x + bounding_box.width - Decimal(128),
            bounding_box.y - Decimal(10),
            Decimal(128),
            Decimal(128),
        ),
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
        "Climate sensitivity estimates from volcanoes in the CESM2",
        font="Helvetica-Bold",
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        font_size=Decimal(35),
        vertical_alignment=Alignment.TOP,
        horizontal_alignment=Alignment.CENTERED,
    ).layout(page, bounding_box)
    pdf.Heading(
        "Eirik Rolland Enger, Audun Theodorsen",
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


def _paragraph_box(padding_bottom: Decimal = Decimal(9)) -> HeterogeneousParagraph:
    h = HeterogeneousParagraph(
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
        padding_bottom=padding_bottom,
        padding_top=Decimal(5),
        padding_right=Decimal(9),
        padding_left=Decimal(9),
        fixed_leading=Decimal(10),
    )
    h._respect_newlines_in_text = True
    return h


def _paragraph_text(
    text: str, paragraph: Optional[HeterogeneousParagraph] = None
) -> HeterogeneousParagraph:
    if paragraph is None:
        paragraph = _paragraph_box()

    for line in text.split():
        paragraph.add(ChunkOfText(line + " ", font_size=Decimal(15)))
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
                paragraph.add(
                    ChunkOfText(
                        w, font=font, font_color=back_color, font_size=Decimal(15)
                    )
                )
            else:
                paragraph.add(
                    ChunkOfText(
                        w + " ", font=font, font_color=back_color, font_size=Decimal(15)
                    )
                )
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
    layout: PageLayout,
    path: str,
    shape: tuple[int, int],
    local: bool = False,
    padding_bottom: Decimal = Decimal(0),
    caption: Optional[Union[float, str]] = None,
) -> pdf.Image:
    if local:
        print(
            "WARNING: using local image file. Might cause problems when reproducing. "
            + "Consider uploading to GitHub or similar and use a permalink."
        )
        pth = Path(path)
    else:
        pth = path
    width, height = shape
    cw = layout._column_width
    align = Alignment.CENTERED
    if width > cw:
        width = cw
    match caption:
        case "left":
            width = cw * Decimal(0.8)
            align = Alignment.RIGHT
        case "bottom":
            # Try to make a sort of good fit, but can be adjusted with
            # padding_bottom anyway
            padding_bottom += Decimal(20)
        case float():
            if caption == 0 or abs(caption) > 1:
                raise AttributeError("Caption must be between -1 and 1, and non-zero.")
            elif caption < 0:
                align = Alignment.LEFT
            else:
                align = Alignment.RIGHT
            width = cw * Decimal(abs(1 - caption))
    height = int(width / shape[0] * shape[1])
    return pdf.Image(
        pth,
        width=Decimal(width),
        height=Decimal(height),
        horizontal_alignment=align,
        padding_bottom=padding_bottom,
        # margin_bottom=Decimal(-10),
    )


def _caption_previous_object(
    text: str, layout: PageLayout, location: str = "left", x_shift= Decimal(10), y_shift= Decimal(10), width2clm = Decimal(0.2),
) -> None:
    match location:
        case "left" | "right":
            x = (
                layout._horizontal_margin
                + layout._current_column_index
                * (layout._column_width + layout._inter_column_margin)
                + x_shift
            )
            y = layout._previous_element.bounding_box.y + y_shift
            width = layout._column_width * width2clm
            height = layout._previous_element.bounding_box.height - Decimal(20)
        case "bottom":
            x = layout._horizontal_margin + layout._current_column_index * (
                layout._column_width + layout._inter_column_margin
            )
            y = layout._previous_element.bounding_box.y + y_shift
            width = layout._column_width
            height = Decimal(20)
        case _:
            raise ValueError(
                f"location must be one of 'left', 'right', 'bottom', not {location}"
            )
    pdf.Paragraph(
        text,
        horizontal_alignment=Alignment.CENTERED,
        font="Helvetica-Oblique",
        font_color=pdf.HexColor("#555555"),
        font_size=Decimal(10),
    ).layout(
        layout.get_page(),
        Rectangle(x, y, width, height),
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
            """In order to estimate the global temperature response and climate
            sensitivity to radiative forcing, volcanic activity is an important testbed.
            This is done using a non-parametric approach, contrary to most previous
            attempts (e.g. [1, 2]). In order to have good datasets with high resolution
            and eruptions of correct physical properties and frequency, simulations with
            custom made synthetic volcanic data is run using the Community Earth System
            model, version 2 (CESM2)."""
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "https://github.com/engeir/presentations-files/raw/dbaf01e59f9061d3ec37f389682d46099af22ccc/2022/chess-am/assets/synthetic_volcanoes_historic_real_data.png",
            (1011, 624),
            caption=0.2,
        )
    )
    _caption_previous_object(
        """Emissions file used in CESM2 to simulate volcanic eruptions between 1850 and
        2016. Each bar represent the total emission for a given day, with emissions
        lasting six hours per day.""",
        layout,
        location="left",
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
    # volc_box = _paragraph_box()
    # _paragraph_text_chunks(
    #     [
    #         (
    #             "normal",
    #             "Strategy is to use the already present forcing file and write over it. This resulted in ",
    #             True,
    #         ),
    #         ("code", " volcano-cooking", False),
    #         (
    #             "normal",
    #             ", a python library for generating valid CESM2 volcanic forcing files.",
    #             True,
    #         ),
    #     ],
    #     volc_box,
    # )
    # _paragraph_text_chunks(
    #     [
    #         ("bold", "volcanoes.nc ", True),
    #         ("normal", "are so very ", True),
    #         ("code", "cool", False),
    #         ("normal", ".", True),
    #     ],
    #     volc_box,
    # )
    # _paragraph_text(
    #     """Want to run CESM2 with synthetic volcanic eruptions. Want to recreate the
    #     forcing file loaded by CESM2, but first need to generate raw synthetic forcing
    #     data that is used to create the full forcing file. Example: Volcanic eruptions
    #     from the last 150 years are included in CESM2 via a file which, if we omit
    #     location in space, has volcanoes as shown below.""",
    #     volc_box,
    # )
    # layout.add(volc_box)
    layout.add(
        _paragraph_image(
            layout,
            "volcano-cooking-flow.png",
            shape=(1792, 2218),
            caption=0.1,
            local=True,
        )
    )
    _caption_previous_object(
        """volcano-cooking generates synthetic data used as input to an NCL script, also
        present in volcano-cooking, which is generating the full forcing file. Raw
        emission data shown in the image titled "Real data" is extracted from the
        forcing file present in CESM2, while data shown in the image titled "Sythetic
        data" is generated with volcano-cooking. From the raw data, via an NCL script,
        the forcing is fed to CESM2.
        """,
        layout,
        location="left",
        width2clm=Decimal(0.3),
        # location="bottom",
        y_shift=-Decimal(100),
    )
    layout.add(
        _paragraph_text(
            """We are running CESM2.1.3 with the WACCM6 atmosphere model with middle
            atmosphere chemistry, which means that it calculates the evolution of
            stratospheric aerosols from SO2 emissions. The raw emissions file for the
            default historical run (1850 to 2016) is show below, where each eruption
            last for six hours per day, starting at noon."""
        )
    )
    # scale_down = 3
    # layout.add(
    #     _paragraph_image(
    #         layout,
    #         "https://github.com/engeir/presentations-files/raw/ce8078c1f469e75ed910118e2cd3a222077b3983/2022/chess-am/assets/AEROD_v-strong_percentiles.png",
    #         shape=(int(1011 / scale_down), int(624 / scale_down)),
    #         local=False,
    #     )
    # )
    # layout.add(
    #     _paragraph_image(
    #         layout,
    #         "https://github.com/engeir/presentations-files/raw/ce8078c1f469e75ed910118e2cd3a222077b3983/2022/chess-am/assets/TREFHT-strong_percentiles.png",
    #         shape=(int(1011 / scale_down), int(624 / scale_down)),
    #         local=False,
    #     )
    # )

    # RESULTS ------------------------------------------------------------------------ #
    layout.add(_paragraph_heading("Results"))
    layout.add(
        _paragraph_text(
            """Here we can mention (1) shape comparison between medium and strong (2)
            peak comes quite late, 1 to 2 years after the eruption.
            """
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "/home/een023/Documents/presentations-files/2022/chess-am/assets/compare-waveform-integrate.png",
            shape=(1011, 624),
            local=True,
            caption=0.2,
        )
    )
    _caption_previous_object(
        """Comparison between the waveform of the temperature response from the
        smaller and the larger volcanic eruption. The black lines are medians
        from ensembles of four simulations, while the shading cover from the
        5th to the 95th percentile. Both lines are coloured black for better
        visibility, with the more noisy signal corresponding to the red, wider
        shading.
        """,
        layout,
        location="left",
    )
    # FUTURE ------------------------------------------------------------------------- #
    layout.add(_paragraph_heading("Future work and use cases"))
    layout.add(
        _paragraph_text(
            """We can use this to look at how forcing at specific locations
            affect the global climate, as well as how a given region and
            neighbouring regions is affected. One particularly interesting
            region may be the arctic; we could then place a big eruption in
            Greenland and observe how the climate changes from there.
            """
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "https://github.com/engeir/presentations-files/raw/f71580dcb981c2e827b7f9bde3978390fe60840f/2022/chess-am/assets/AEROD_v20220404-composite.png",
            shape=(1191, 754),
            caption="bottom",
        )
    )
    _caption_previous_object(
        """Aerosol optical depth and temperature response obtained from four different
        simulations using identical volcanic eruptions, shifted in time by three month,
        placing one eruption in each season of the year. The black lines show the
        median, while the red shading lie between the 2.5th and 97.5th percentiles.
        """,
        layout,
        location="bottom",
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
    # Update diagrams
    # NOTE: This depends on Grapviz and imagemagick
    script = os.path.join(os.getcwd(), "borb_poster", "flow_diagrams.py")
    subprocess.call(["python", script])
    subprocess.call(
        [
            "convert",
            "-density",
            "300",
            "-trim",
            "volcano-cooking-flow.pdf",
            "-quality",
            "100",
            "volcano-cooking-flow.png",
        ]
    )

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
