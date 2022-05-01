"""Module for creating a poster with `borb`."""

import math
import os
import subprocess
from decimal import Decimal
from pathlib import Path
from typing import List, Optional, Tuple, Union

import borb.pdf as pdf
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.pdf.canvas.layout.emoji.emoji import Emoji, Emojis
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.chunk_of_text import ChunkOfText
from borb.pdf.canvas.layout.text.chunks_of_text import HeterogeneousParagraph
from borb.pdf.page.page_size import PageSize
from borb_poster import color_palette, shapes

try:
    from rich import traceback

    traceback.install()
except ImportError:
    pass


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
    c1, c2, c3, c4 = 0.45, 0.22, 0.12, 0.21
    pdf.FixedColumnWidthTable(
        number_of_rows=1,
        number_of_columns=3,
        column_widths=[Decimal(c1 + c2), Decimal(c3), Decimal(c4)],
    ).add(
        pdf.OrderedList(vertical_alignment=Alignment.MIDDLE, padding_top=Decimal(15))
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
                """Lucy, L. B. (1974), An iterative technique for the rectification of observed distributions."""
            )
        )
        .add(
            pdf.Paragraph(
                """Richardson, W. H. (1972), Bayesian-Based Iterative Method of Image Restoration*."""
            )
        )
        .add(
            pdf.Paragraph(
                """Stevens, B., Sherwood, S. C., et al. (2016), Prospects for narrowing
                bounds on Earth's equilibrium climate sensitivity.
                """
            )
        )
        .add(
            pdf.Paragraph(
                """Dong, Y., Proistosescu, C., et al. (2019), Attributing Historical and
                Future Evolution of Radiative Feedbacks to Regional Warming Patterns
                using a Green's Function Approach: The Preeminence of the Western
                Pacific."""
            )
        )
    ).add(
        pdf.TableCell(
            pdf.Paragraph(
                "Contact:",
                font="Helvetica-Oblique",
                font_size=Decimal(20),
                font_color=pdf.HexColor(color_palette.SUPPORTCOLOR["yellow"]),
                horizontal_alignment=Alignment.LEFT,
            ),
            padding_left=Decimal(25),
        )
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
    pdf.Paragraph(
        "References",
        font="Helvetica-Bold",
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        font_size=Decimal(25),
        vertical_alignment=Alignment.TOP,
        horizontal_alignment=Alignment.LEFT,
        padding_bottom=Decimal(50),
    ).layout(
        page,
        Rectangle(
            bounding_box.x,
            bounding_box.y,
            Decimal(128),
            # 25 - 20, diff in font sizes ... +1 for the looks
            bounding_box.height + Decimal(6),
        ),
    )
    pdf.Paragraph(
        "*eirik.r.enger@uit.no",
        font="Courier",
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP,
        padding_left=Decimal(25),
    ).layout(
        page,
        Rectangle(
            bounding_box.x + bounding_box.width * Decimal(c1 + c2),
            bounding_box.y,
            Decimal(128),
            # 12 is the font size ...
            Decimal(128 - 12),
        ),
    )
    pdf.Barcode(
        data="mailto:eirik.r.enger@uit.no",
        width=Decimal(64),
        height=Decimal(64),
        type=pdf.BarcodeType.QR,
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP,
        padding_left=Decimal(25),
    ).layout(
        page,
        Rectangle(
            bounding_box.x + bounding_box.width * Decimal(c1 + c2),
            bounding_box.y - Decimal(10),
            Decimal(128),
            Decimal(128 - 2 * 12),
        ),
    )
    pdf.Barcode(
        data="https://github.com/engeir/presentations-files/raw/main/2022/chess-am/poster.pdf",
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
    scale_img = 0.1
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
        "Eirik Rolland Enger*, Audun Theodorsen, Martin Rypdal",
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

    pdf.Heading(
        "CHESS AM 2022",
        font="Helvetica-Bold-Oblique",
        font_size=Decimal(20),
        font_color=pdf.HexColor(color_palette.MAIN_COLOR),
        horizontal_alignment=Alignment.LEFT,
        vertical_alignment=Alignment.TOP,
        padding_left=Decimal(25),
    ).layout(
        page,
        Rectangle(
            Decimal(40 * 3),
            height - img_h - header_height + 2 * margin_y,
            bounding_box.width,
            Decimal(25),
        ),
    )
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
    margin_x = Decimal(15)
    margin_y = Decimal(15)
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


def _paragraph_heading(text: str, dark: bool = False) -> HeterogeneousParagraph:
    if dark:
        paragraph = HeterogeneousParagraph(
            [],
            background_color=pdf.HexColor(color_palette.MAIN_COLOR),
            padding_bottom=Decimal(10),
            padding_left=Decimal(10),
            padding_right=Decimal(10),
            margin_top=Decimal(0),
        )
        fs = 25
        pb, pl, pr = Decimal(7), Decimal(2), Decimal(5)
        background_color = pdf.HexColor(color_palette.MAIN_COLOR)
        font_color = pdf.HexColor("#ffffff")
    else:
        paragraph = HeterogeneousParagraph([])
        fs = 30
        pb, pl, pr = Decimal(3), Decimal(0), Decimal(0)
        font_color = pdf.HexColor("#000000")
        background_color = None
    volc: Emoji = Emojis.VOLCANO.value
    volc.set_font_size(Decimal(fs))
    paragraph.add(volc)
    paragraph.add(ChunkOfText("    "))
    paragraph.add(
        ChunkOfText(
            text,
            font="Helvetica-Bold-Oblique",
            font_size=Decimal(fs),
            font_color=font_color,
            background_color=background_color,
            border_color=pdf.HexColor(color_palette.SUPPORTCOLOR["red"]),
            border_width=Decimal(1),
            border_bottom=True,
            padding_bottom=pb,
            padding_left=pl,
            padding_right=pr,
        )
    )
    return paragraph


def _paragraph_box(
    padding_bottom: Decimal = Decimal(9), no_margins: bool = False
) -> HeterogeneousParagraph:
    if no_margins:
        return HeterogeneousParagraph(
            [],
            background_color=pdf.HexColor(color_palette.MAIN_COLOR),
            border_color=pdf.HexColor(color_palette.SUPPORTCOLOR["red"]),
            border_width=Decimal(1),
            fixed_leading=Decimal(6),
        )
    return HeterogeneousParagraph(
        [],
        background_color=pdf.HexColor(color_palette.MAIN_COLOR),
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
        fixed_leading=Decimal(6),
    )


def _paragraph_text(
    text: str,
    paragraph: Optional[HeterogeneousParagraph] = None,
    start_bold: bool = False,
    no_margins: bool = False,
) -> HeterogeneousParagraph:
    if paragraph is None:
        paragraph = _paragraph_box(no_margins=no_margins)

    for i, line in enumerate(text.split()):
        if start_bold:
            if i < 2:
                paragraph.add(
                    ChunkOfText(
                        line + " ",
                        font_size=Decimal(13),
                        font="Helvetica-Bold",
                        font_color=pdf.HexColor("#dddddd"),
                    )
                )
                continue
        paragraph.add(
            ChunkOfText(
                line + " ", font_size=Decimal(13), font_color=pdf.HexColor("#dddddd")
            )
        )
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


def _math_img(url: str, color: str = "#003349") -> str:
    img_id = 0
    while os.path.isfile(os.path.join(os.getcwd(), f"image{img_id}.png")):
        img_id += 1
    img_name = os.path.join(os.getcwd(), f"image{img_id}.png")
    subprocess.call(
        [
            "convert",
            url,
            "-background",
            color,
            "-layers",
            "flatten",
            img_name,
        ]
    )
    return img_name


def _paragraph_image(
    layout: PageLayout,
    path: str,
    shape: tuple[int, int],
    local: bool = False,
    padding_bottom: Decimal = Decimal(0),
    padding_top: Decimal = Decimal(0),
    caption: Optional[Union[float, str]] = None,
    scale: Union[Decimal, float] = 1.0,
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
    cw = layout._column_width * Decimal(scale)
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
        padding_top=padding_top,
        # margin_bottom=Decimal(-10),
    )


def _caption_previous_object(
    text: str,
    layout: PageLayout,
    location: str = "left",
    x_shift=Decimal(10),
    y_shift=Decimal(10),
    width2clm=Decimal(0.2),
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
            Estimates are to be made using a non-parametric approach, contrary to most
            previous attempts (e.g. [1, 2]). For this, datasets with high resolution and
            eruptions of well known physical properties and frequency are needed, and we
            therefore run simulations with custom made synthetic volcanic data in the
            Community Earth System model, version 2 (CESM2).
            """
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
    layout.add(
        _paragraph_text(
            """We are running CESM2.1.3 with the WACCM6 atmosphere model with middle
            atmosphere chemistry. Evolution of stratospheric aerosols are calculated
            from SO2 emissions obtained from emissions files, show in Figure 1. Figure 2
            show a simple diagram of how new forcing files are created and run in CESM2.
            The process of generating working forcing files is carried out fully by the
            python project volcano-cooking, which can be found on GitHub using the QR
            code in the heading.
            """
        )
    )
    layout.add(
        _paragraph_image(
            layout,
            "https://github.com/engeir/presentations-files/raw/dbaf01e59f9061d3ec37f389682d46099af22ccc/2022/chess-am/assets/synthetic_volcanoes_historic_real_data.png",
            (1011, 624),
            caption=0.30,
        )
    )
    _caption_previous_object(
        """Figure 1: Emissions file used in historical runs of CESM2 to simulate
        volcanic eruptions between 1850 and 2016. Each bar represent the total emission
        for a given day, with emissions lasting six hours per day.
        """,
        layout,
        location="left",
    )
    layout.add(
        _paragraph_image(
            layout,
            "volcano-cooking-flow.png",
            shape=(1792, 2218),
            caption=0.13,
            local=True,
        )
    )
    _caption_previous_object(
        """Figure 2: volcano-cooking generates synthetic data for the raw emissions used
        as input to an NCL script, also present in volcano-cooking, which is further
        generating the full forcing file. Raw emission data shown in the image titled
        "Real data" is extracted from the forcing file present in CESM2, while data
        shown in the image titled "Synthetic data" is generated with the volcano-cooking
        python package. After feeding the emissions file into an NCL script, forcing
        files with correct format for CESM2 to accept it is created. The images in the
        box "CESM2 output" are made from data generated by CESM2 using the forcing file
        "Synthetic data". "Response" show the shortwave minus longwave forcing in the
        lower left part, with the temperature response in the upper right part, while
        "Aerosol 2D" shows the aerosol optical depth the day of the eruption and six
        months after. You can view the full animation of the aerosol evolution by
        following the QR code in the bottom right of the figure!
        """,
        layout,
        location="left",
        width2clm=Decimal(0.35),
    )
    _paragraph_qr_code(
        "https://github.com/engeir/presentations-files/raw/14d24ee6343b4b80be8476eb9e2b76bbfadd8dc5/2022/chess-am/assets/AEROD_v20220404.mp4"
    ).layout(
        layout.get_page(),
        Rectangle(
            layout._previous_element.bounding_box.x
            + layout._previous_element.bounding_box.width * Decimal(0.7),
            layout._previous_element.bounding_box.y + Decimal(65),
            Decimal(64),
            Decimal(64),
        ),
    )

    # RESULTS ------------------------------------------------------------------------ #
    layout.add(_paragraph_heading("Results"))
    layout.add(
        pdf.FixedColumnWidthTable(
            border_radius_top_left=Decimal(8),
            border_radius_top_right=Decimal(8),
            border_radius_bottom_right=Decimal(8),
            border_radius_bottom_left=Decimal(8),
            number_of_rows=2,
            number_of_columns=1,
            background_color=pdf.HexColor(color_palette.MAIN_COLOR),
            padding_bottom=Decimal(9),
            padding_top=Decimal(5),
            padding_right=Decimal(9),
            padding_left=Decimal(9),
        )
        .add(
            pdf.TableCell(
                _paragraph_text(
                    """The shape of the temperature response to eruptions of different
                    magnitude is not the same. Temperature peaks later when the climate
                    system is forced with a larger eruption compared to the case of
                    forcing with a smaller eruption.
                    """,
                    start_bold=True,
                    no_margins=True,
                ),
                padding_bottom=Decimal(10),
            )
        )
        .add(
            _paragraph_text(
                """In both cases, the temperature has its strongest response after one
                to two years. Also, even after eight years the temperature has not yet
                fully recovered back to equilibrium.
                """,
                start_bold=True,
                no_margins=True,
            )
        )
        .no_borders(),
    )
    layout.add(
        _paragraph_image(
            layout,
            "https://github.com/engeir/presentations-files/raw/84e2b7adbe528f134c003f956d499b6aa3898b5f/2022/chess-am/assets/compare-waveform-integrate.png",
            shape=(1011, 624),
            caption="bottom",
            padding_bottom=Decimal(40),
        )
    )
    _caption_previous_object(
        """Figure 3: Comparison between the waveform of the temperature response from
        the smaller and the larger volcanic eruption. The black lines are medians from
        ensembles of four simulations, while the shading cover the 5th to the 95th
        percentile. All four simulations in the ensembles are identical, except from a
        three month delay of the eruption, placing the eruptions in the ensemble in all
        four seasons. This seasonal variability is also what cases the wide percentiles.
        The vertical line indicate the timing of the eruption.
        """,
        layout,
        location="bottom",
        y_shift=Decimal(43),
    )

    # MATHEMATICAL FRAMEWORK --------------------------------------------------------- #
    math_scaling = 0.3
    layout.add(_paragraph_heading("Mathematical framework"))
    layout.add(
        pdf.FixedColumnWidthTable(
            border_radius_top_left=Decimal(8),
            border_radius_top_right=Decimal(8),
            border_radius_bottom_right=Decimal(8),
            border_radius_bottom_left=Decimal(8),
            number_of_rows=4,
            number_of_columns=1,
            background_color=pdf.HexColor(color_palette.MAIN_COLOR),
            padding_bottom=Decimal(9),
            padding_top=Decimal(5),
            padding_right=Decimal(9),
            padding_left=Decimal(9),
        )
        .add(
            _paragraph_text(
                """The filtered Poisson process (FPP) is the phenomenological model used
                for the temperature response to volcanoes, shown below. It is a
                convolution equation, where forcing is convolved with a general shape
                representing a response function.
                """,
                no_margins=True,
            )
        )
        .add(
            _paragraph_image(
                layout,
                _math_img(
                    # T_K(t) = [\phi*f_K] \left( \frac{t}{\tau_{\mathrm{d}}} \right)
                    "https://latex2png.com/pngs/3d4b5efbe76266d9711e60698c45f3b4.png"
                ),
                (812, 200),
                scale=math_scaling,
                local=True,
                padding_bottom=Decimal(3),
                padding_top=Decimal(10),
            )
        )
        .add(
            _paragraph_text(
                """Knowing the forcing and temperature signals, we get to the response
                by deconvolving, provided we feed the algorithm with an initial guess of
                the response function [3, 4].
                """,
                no_margins=True,
            )
        )
        .add(
            _paragraph_image(
                layout,
                _math_img(
                    # \phi^{(n+1)}=\phi^{(n)} \frac{(T_K-\langle T_K\rangle)*\hat{f}_K+b}{\phi^{(n)}*f_K*\hat{f}_K+b}
                    "https://latex2png.com/pngs/30ce7c3df0f5c690f4e09dfe5183d92f.png"
                ),
                (1271, 225),
                scale=Decimal(1271 / 812 * math_scaling),
                local=True,
                padding_top=Decimal(10),
            )
        )
        .no_borders()
    )

    # FUTURE ------------------------------------------------------------------------- #
    layout.add(_paragraph_heading("Future work and use cases"))
    layout.add(
        pdf.FixedColumnWidthTable(
            border_radius_top_left=Decimal(8),
            border_radius_top_right=Decimal(8),
            border_radius_bottom_right=Decimal(8),
            border_radius_bottom_left=Decimal(8),
            number_of_rows=2,
            number_of_columns=1,
            background_color=pdf.HexColor(color_palette.MAIN_COLOR),
            padding_bottom=Decimal(9),
            padding_top=Decimal(5),
            padding_right=Decimal(9),
            padding_left=Decimal(9),
        )
        .add(
            pdf.TableCell(
                _paragraph_text(
                    """The deconvolution algorithm introduces the non-parametric
                    approach to estimating the temperature response. This does not need
                    volcanic eruptions that are isolated in time, although linearity is
                    assumed. Thus, volcanoes that overlap and cluster together in time
                    are no problem, allowing us to gain insight into whether they simply
                    superpose or not.
                    """,
                    start_bold=True,
                    no_margins=True,
                ),
                padding_bottom=Decimal(10),
            )
        )
        .add(
            _paragraph_text(
                """Studies argue that regional patterns may be important in relation to
                the outward radiation [5], with some studies looking more closely at the
                surface temperature patterns [6]. A different take to this may be to
                rather place volcanic eruptions in some key locations and compare the
                temperature responses obtained.
                """,
                start_bold=True,
                no_margins=True,
            )
        )
        .no_borders(),
    )
    # layout.add(
    #     _paragraph_image(
    #         layout,
    #         "https://github.com/engeir/presentations-files/raw/f71580dcb981c2e827b7f9bde3978390fe60840f/2022/chess-am/assets/AEROD_v20220404-composite.png",
    #         shape=(1191, 754),
    #         caption="bottom",
    #         scale=0.9,
    #     )
    # )
    # _caption_previous_object(
    #     """Figure 4: Aerosol optical depth and temperature response obtained from four
    #     different simulations using identical volcanic eruptions, shifted in time by
    #     three month, placing one eruption in each season of the year. The black lines
    #     show the median, while the red shading lie between the 2.5th and 97.5th
    #     percentiles.
    #     """,
    #     layout,
    #     location="bottom",
    # )
    # _paragraph_qr_code(
    #     "https://github.com/engeir/presentations-files/raw/14d24ee6343b4b80be8476eb9e2b76bbfadd8dc5/2022/chess-am/assets/AEROD_v20220404.mp4"
    # ).layout(
    #     layout.get_page(),
    #     Rectangle(
    #         layout._previous_element.bounding_box.x
    #         # + layout._previous_element.bounding_box.width
    #         + Decimal(10),
    #         layout._previous_element.bounding_box.y + Decimal(65),
    #         Decimal(64),
    #         Decimal(64),
    #     ),
    # )


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

    # Clean up png's from diagram image
    pngs = [i for i in os.listdir() if ".png" in i]
    subprocess.call(["rm", *pngs])
    subprocess.call(["rm", "volcano-cooking-flow.pdf"])
