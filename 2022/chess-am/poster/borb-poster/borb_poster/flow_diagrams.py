"""Create simple flow diagram.

The diagram displays the process of starting from the emissions file for the
historical period, creating a new and feeding it to `volcano-cooking` before
adding it to the CESM2 simulation.
"""
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram(
    "", show=False, filename="volcano-cooking-flow", direction="TB", outformat="pdf"
):
    # __outformats = ("png", "jpg", "svg", "pdf", "dot")

    # with Cluster("volcano-cooking", "TB"):

    github_url = "https://opengraph.githubassets.com/79cc447dbe0b99b662134b1e38c1cfece4a7f97c/engeir/volcano-cooking"
    github_icon = "github.png"
    urlretrieve(github_url, github_icon)

    github = Custom("Python project", github_icon)

    with Cluster("Raw emissions"):

        with Cluster("From CESM2 Input File"):
            # download the icon image file
            diagrams_url = "https://github.com/engeir/presentations-files/raw/7463c40eb08423ce7a22b423a84a2cdee7b3ce88/2022/chess-am/assets/synthetic_volcanoes_historic_real_data.png"
            diagrams_icon = "synth_real.png"
            urlretrieve(diagrams_url, diagrams_icon)

            synth_real = Custom("Real data", diagrams_icon)

        # download the icon image file
        diagrams_url = "https://github.com/engeir/presentations-files/raw/7463c40eb08423ce7a22b423a84a2cdee7b3ce88/2022/chess-am/assets/synthetic_volcanoes_strong.png"
        diagrams_icon = "synth_fake.png"
        urlretrieve(diagrams_url, diagrams_icon)

        synth_fake = Custom("Synthetic data", diagrams_icon)
        # synth_real - synth_fake
        # github >> [synth_real]

    with Cluster("CESM2 Input Forcing File"):
        with Cluster("CESM2 output"):

            rad_diff_temp_url = "https://github.com/engeir/presentations-files/raw/84e2b7adbe528f134c003f956d499b6aa3898b5f/2022/chess-am/assets/rad_diff-temp-percentiles-overlaid.png"
            rad_diff_temp_icon = "rad_diff_temp.png"
            urlretrieve(rad_diff_temp_url, rad_diff_temp_icon)

            rad_diff_temp = Custom("Response", rad_diff_temp_icon)

            two_d_plot_url = "https://github.com/engeir/presentations-files/raw/7463c40eb08423ce7a22b423a84a2cdee7b3ce88/2022/chess-am/assets/AEROD_v20220404-composite.png"
            two_d_plot_icon = "two_d_plot.png"
            urlretrieve(two_d_plot_url, two_d_plot_icon)

            two_d_plot = Custom("Aerosol 2D", two_d_plot_icon)


    github >> synth_fake
    # synth_real << two_d_plot
    synth_fake >> Edge(color="firebrick", style="dashed") >> rad_diff_temp
